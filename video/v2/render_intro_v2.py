#!/usr/bin/env python3
"""Ay-kafa anlatıcılı 60 sn'lik giriş (10 dakikalık videonun açılışı).

    python3 video/v2/render_intro_v2.py <kaynak_klip.mp4> <avatar_dizini> [çıktı.mp4]

Kareler numpy ile birleştirilir, yazı/şekiller libass ile basılır, ses numpy ile
sentezlenir. Gereken tek şey libass'li bir ffmpeg (FFMPEG ortam değişkeni,
imageio-ffmpeg ya da PATH).

Kaynak klip varsayımları: bkz. video/build_intro.py (parlak = tahmin, gri =
gerçekleşen, 1 dk mumlar, tahmin anı x≈1675, 08/08 duruşu ≈17.8-19.5 sn).
"""
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np

W, H, FPS, DUR = 1920, 1080, 60, 60.0
SR = 48000
NOW_X = 1675
BG = np.array([3, 4, 7], np.float32)


def find_ffmpeg():
    if os.environ.get("FFMPEG"):
        return os.environ["FFMPEG"]
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg") or sys.exit("ffmpeg bulunamadı")


FF = find_ffmpeg()


def ff(*args, **kw):
    return subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *args], check=True, **kw)


def read_rgb(path, w, h, t=None, vf=None):
    args = (["-ss", str(t)] if t is not None else []) + ["-i", path, "-frames:v", "1"]
    chain = [vf] if vf else []
    chain.append(f"scale={w}:{h}:flags=lanczos")
    out = ff(*args, "-vf", ",".join(chain), "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
             capture_output=True).stdout
    return np.frombuffer(out, np.uint8).reshape(h, w, 3).astype(np.float32)


def smooth(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)


def ramp(t, a, b):
    return smooth((t - a) / (b - a)) if b > a else float(t >= a)


def box_blur(m, r):
    """Ayrılabilir kutu bulanıklığı (2 geçiş ≈ gauss)."""
    for _ in range(2):
        for ax in (0, 1):
            c = np.cumsum(np.pad(m, [(r + 1, r) if i == ax else (0, 0) for i in range(2)], mode="edge"), axis=ax)
            m = (np.take(c, range(2 * r + 1, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - 2 * r - 1), axis=ax)) / (2 * r + 1)
    return m


# ---------------------------------------------------------------- varlıklar

def clean_chart(img):
    """Kaynaktaki başlık, durum satırı ve sayaç yazılarını arka planla örter."""
    img = img.copy()
    img[0:150, 0:760] = BG
    img[985:H, 0:760] = BG
    return img


def darken_future(img, k):
    out = img.copy()
    out[:, NOW_X:] = BG + (out[:, NOW_X:] - BG) * k
    return out


class Avatar:
    """Dairesel rozet ya da vinyetli portre; ay ışığı üç varyant arasında karışır."""

    def __init__(self, path, size, round_mask, vignette=False):
        rgb = read_rgb(path, size, size)
        yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
        d = np.hypot(xx - size / 2, yy - size / 2) / (size / 2)
        if round_mask:
            alpha = np.clip((0.985 - d) / 0.02, 0, 1)
        elif vignette:
            alpha = np.clip((1.0 - d) / 0.35, 0, 1) ** 1.5
        else:
            alpha = np.ones_like(d)
        luma = rgb @ np.array([0.3, 0.59, 0.11], np.float32)
        moon = np.clip((luma - 120) / 60, 0, 1) * (rgb[..., 0] > 140)
        glow = box_blur(moon, max(3, size // 40))
        halo = np.clip(box_blur(moon, max(6, size // 12)) * 1.6, 0, 1)
        cream = np.array([255, 236, 190], np.float32)
        self.normal = rgb
        self.dim = rgb * (1 - 0.62 * glow[..., None])
        self.bright = np.clip(rgb + halo[..., None] * cream * 0.35 + glow[..., None] * 25, 0, 255)
        self.alpha = alpha[..., None]
        self.size = size

    def draw(self, frame, x, y, mood=0.0, opacity=1.0):
        """mood: -1 sönük … 0 normal … +1 parlak."""
        if opacity <= 0:
            return
        if mood < 0:
            img = self.normal + (self.dim - self.normal) * (-mood)
        else:
            img = self.normal + (self.bright - self.normal) * mood
        s = self.size
        x0, y0 = max(0, int(x)), max(0, int(y))
        x1, y1 = min(W, int(x) + s), min(H, int(y) + s)
        if x1 <= x0 or y1 <= y0:
            return
        sx, sy = x0 - int(x), y0 - int(y)
        a = self.alpha[sy:sy + y1 - y0, sx:sx + x1 - x0] * opacity
        region = frame[y0:y1, x0:x1]
        region += (img[sy:sy + y1 - y0, sx:sx + x1 - x0] - region) * a


def night_background():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.hypot((xx - 520) / W, (yy - 560) / H)
    k = np.clip(1 - d * 1.9, 0, 1)[..., None]
    purple = np.array([36, 18, 72], np.float32)
    return BG + (purple - BG) * k ** 1.6


# ---------------------------------------------------------------- ASS

ASS_HEADER = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,46,&H00FFFFFF,&H00FFFFFF,&H00070403,&H50070403,0,0,0,0,100,100,0,0,3,14,0,2,0,0,0,1
Style: Head,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00070403,&H96070403,1,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Mono,DejaVu Sans Mono,30,&H00FFFFFF,&H00FFFFFF,&H00070403,&H96070403,0,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Shape,DejaVu Sans,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Line,DejaVu Sans,20,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,4,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

WHITE, GREY, DIM = "&HFFFFFF&", "&HA8A8A8&", "&H707070&"
CREAM = "&HBEECFF&"        # ay ışığı (#FFECBE)
CYAN = "&HE0E37F&"         # tahmin mumları
PURPLE = "&HFF5A8C&"       # avatar halkası (#8C5AFF)
GREEN, RED = "&H8FD98A&", "&H7A6FE0&"
COIN = "&H4FC6F2&"         # altın (#F2C64F)


def ts(sec):
    cs = int(round(sec * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


class Ass:
    def __init__(self):
        self.lines = []

    def add(self, t0, t1, text, style="Head", layer=1):
        self.lines.append(f"Dialogue: {layer},{ts(t0)},{ts(t1)},{style},,0,0,0,,{text}")

    def text(self, t0, t1, x, y, s, style="Head", color=WHITE, an=7, size=None, fade=(250, 250), extra=""):
        fs = rf"\fs{size}" if size else ""
        self.add(t0, t1, rf"{{\an{an}\pos({x},{y})\c{color}{fs}\fad({fade[0]},{fade[1]}){extra}}}{s}", style)

    def cap(self, t0, t1, s):
        """Anlatım altyazısı (seslendirme metni)."""
        self.add(t0, t1, rf"{{\an2\pos(960,1030)\fad(180,180)}}{s}", "Cap", 5)

    def shape(self, t0, t1, x, y, path, color, alpha="&H00&", fade=(0, 0), extra="", layer=2):
        self.add(t0, t1, rf"{{\an7\pos({x},{y})\p1\bord0\shad0\c{color}\alpha{alpha}\fad({fade[0]},{fade[1]}){extra}}}{path}",
                 "Shape", layer)

    def rect(self, t0, t1, x1, y1, x2, y2, color, alpha="&H00&", fade=(0, 0), extra="", layer=2):
        w, h = x2 - x1, y2 - y1
        self.shape(t0, t1, x1, y1, f"m 0 0 l {w} 0 {w} {h} 0 {h}", color, alpha, fade, extra, layer)

    def circle(self, t0, t1, cx, cy, r, color, alpha="&H00&", fade=(0, 0), extra="", layer=2):
        self.shape(t0, t1, cx - r, cy - r, circle_path(r, r, r), color, alpha, fade, extra, layer)

    def ring(self, t0, t1, cx, cy, r, color, width=4, fade=(0, 0), layer=2):
        path = circle_path(r, r, r)
        self.add(t0, t1, rf"{{\an7\pos({cx - r},{cy - r})\p1\1a&HFF&\bord{width}\shad0\3c{color}\fad({fade[0]},{fade[1]})}}{path}",
                 "Line", layer)

    def dashed_v(self, t0, t1, x, y1, y2, color=WHITE, fade=(0, 0)):
        y = y1
        while y < y2:
            self.rect(t0, t1, x - 1, y, x + 2, min(y + 14, y2), color, fade=fade)
            y += 24

    def moon_phase(self, t0, t1, cx, cy, r, f, fade=(200, 200), label=None, layer=3):
        """P↑ göstergesi: aydınlık kesir f (0 yeni ay … 1 dolunay), sağ taraftan dolar."""
        self.circle(t0, t1, cx, cy, r, "&H2A1E1A&", fade=fade, layer=layer)
        self.ring(t0, t1, cx, cy, r, "&H6A5A55&", 3, fade=fade, layer=layer)
        if f > 0.005:
            self.shape(t0, t1, cx - r, cy - r, phase_path(r, f), CREAM, fade=fade, layer=layer + 1)
        if label:
            self.text(t0, t1, cx, cy + r + 14, label, "Mono", CREAM, an=8, size=int(r * 0.42) + 12, fade=fade)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ASS_HEADER + "\n".join(self.lines) + "\n")


def circle_path(cx, cy, r, n=48):
    pts = [(cx + r * np.cos(a), cy + r * np.sin(a)) for a in np.linspace(0, 2 * np.pi, n, endpoint=False)]
    return "m " + " l ".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def phase_path(r, f, n=40):
    """Aydınlık bölge: sağ yarım çember (limb) + terminatör elipsi."""
    ys = np.linspace(-r, r, n)
    half = np.sqrt(np.maximum(r * r - ys * ys, 0))
    limb = [(r + h, r + y) for y, h in zip(ys, half)]
    term = [(r + (1 - 2 * f) * h, r + y) for y, h in zip(ys[::-1], half[::-1])]
    pts = limb + term
    return "m " + " l ".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def coin(a, t0, t1, cx, cy, r, flip_from=None, flip_to=None, fade=(250, 250)):
    """Yazı-tura parası; flip aralığında \fscx ile döner."""
    ex = ""
    if flip_from is not None:
        a0, a1 = int((flip_from - t0) * 1000), int((flip_to - t0) * 1000)
        seg, steps = 90, []
        for k, st in enumerate(range(a0, a1, seg)):
            steps.append(rf"\t({st},{st + seg},\fscx{8 if k % 2 == 0 else 100})")
        ex = "".join(steps) + rf"\t({a1},{a1 + 60},\fscx100)"
    org = rf"\org({cx},{cy})"
    a.add(t0, t1, rf"{{\an5\pos({cx},{cy}){org}\p1\bord0\shad0\c{COIN}\fad({fade[0]},{fade[1]}){ex}}}"
                  f"{circle_path(r, r, r)}", "Shape", 3)
    a.add(t0, t1, rf"{{\an5\pos({cx},{cy}){org}\p1\bord0\shad0\c&H2F8AB8&\fad({fade[0]},{fade[1]}){ex}}}"
                  f"{circle_path(r * 0.8, r * 0.8, r * 0.8)}", "Shape", 4)
    a.add(t0, t1, rf"{{\an5\pos({cx},{cy}){org}\c&H7FE0FF&\fs{int(r * 0.9)}\b1\bord0\fad({fade[0]},{fade[1]}){ex}}}₺",
          "Head", 5)


# ---------------------------------------------------------------- zaman çizelgesi (ASS)

# 8 örneğin P↑ değerleri (kaynağın durum satırından okundu) ve montajdaki başlangıç anları
SAMPLES = [("08:02", .53, 1.25), ("09:04", .53, 3.8), ("09:23", .49, 5.75), ("09:59", .44, 7.75),
           ("11:24", .45, 11.0), ("12:10", .45, 13.25), ("12:45", .50, 15.25), ("13:46", .53, 17.75)]
M0, M1, SRC0, SRC1 = 23.0, 33.0, 1.3, 19.7          # montaj: çıktı 23-33 sn ← kaynak 1.3-19.7 sn
SPEED = (SRC1 - SRC0) / (M1 - M0)
BADGE = (70, 690, 260)                               # rozet x, y, boyut


def build_ass():
    a = Ass()
    # --- 0-6  soru ------------------------------------------------------------
    a.dashed_v(0.6, 15.0, NOW_X, 170, 960, fade=(300, 0))
    a.text(0.8, 15.0, NOW_X - 16, 160, "ŞİMDİ · 13:46", "Mono", WHITE, an=9, fade=(300, 0))
    a.cap(0.4, 3.0, "20 Haziran, 13:46. Bitcoin.")
    a.cap(3.0, 6.1, "Sizce sonraki 50 dakikada ne olur?")
    for i, (lab, col, x) in enumerate([("▲  YUKARI", GREEN, 700), ("▼  AŞAĞI", RED, 1010)]):
        t = 3.3 + i * 0.15
        a.rect(t, 6.1, x, 820, x + 250, 900, "&H1A1210&", "&H20&", (200, 150), layer=2)
        a.rect(t, 6.1, x, 896, x + 250, 900, col, fade=(200, 150), layer=3)
        a.text(t, 6.1, x + 125, 860, lab, "Head", col, an=5, size=40, fade=(200, 150))
    for k, n in enumerate("321"):
        t = 3.5 + k
        a.text(t, t + 0.9, (NOW_X + W) // 2, 560, n, "Head", CREAM, an=5, size=150,
               fade=(80, 300), extra=r"\t(0,900,\fscx70\fscy70)")
    # --- 6-15  cevap ve ıska ---------------------------------------------------
    a.cap(6.3, 9.9, "Modelimin cevabı: yukarı.")
    a.rect(7.0, 15.0, 1330, 52, 1380, 58, CYAN, fade=(250, 0))
    a.text(7.0, 15.0, 1395, 36, "modelin tahmini", "Mono", CYAN, fade=(250, 0))
    a.rect(10.6, 15.0, 1330, 100, 1380, 106, GREY, fade=(250, 0))
    a.text(10.6, 15.0, 1395, 84, "gerçekleşen", "Mono", GREY, fade=(250, 0))
    a.cap(10.3, 12.7, "Gerçekte olan: önce sert bir düşüş.")
    a.cap(12.7, 15.0, "Tam bir ıska.")
    # --- 15-23  %53 ------------------------------------------------------------
    a.cap(15.2, 18.4, "Ama dürüst olayım: model “yukarı” dememişti.")
    a.moon_phase(15.6, 23.0, 620, 470, 130, 0.53, fade=(400, 250))
    a.text(15.9, 23.0, 820, 330, "P↑", "Mono", CREAM, size=64, fade=(300, 250))
    a.text(16.2, 23.0, 816, 390, "0.53", "Head", WHITE, size=150, fade=(300, 250))
    a.text(16.8, 23.0, 822, 570, "50 dakika sonra daha yukarıda olma olasılığı", "Mono", GREY, size=30,
           fade=(300, 250))
    a.cap(18.4, 23.0, "%53 demişti. Yani neredeyse… yazı-tura.")
    coin(a, 19.6, 23.0, 1500, 470, 95, 19.8, 20.7, fade=(200, 250))
    a.text(20.9, 23.0, 1500, 600, "≈ %50", "Mono", COIN, an=8, size=36, fade=(200, 250))
    # --- 23-33  sekiz an, ay evresi göstergesi ----------------------------------
    bx, by, bs = BADGE
    mx, my = bx + bs + 90, by + 70
    for i, (clock, p, st) in enumerate(SAMPLES):
        t0 = max(M0, M0 + (st - SRC0) / SPEED)
        t1 = M0 + (SAMPLES[i + 1][2] - SRC0) / SPEED if i + 1 < len(SAMPLES) else M1
        a.moon_phase(t0, t1, mx, my, 62, p, fade=(0, 0), label=f"P↑ {p:.2f}")
        a.text(t0, t1, mx + 90, my - 22, f"{i + 1}/8 · {clock}", "Mono", GREY, size=30, fade=(0, 0))
    a.cap(23.2, 27.4, "Aynı gün, sekiz farklı an.")
    a.cap(27.4, 30.9, "Ay ne doldu, ne karardı.")
    a.cap(30.9, 33.0, "Hep yarım kaldı.")
    # --- 33-45  anlatıcı ve soru ------------------------------------------------
    a.cap(33.8, 37.2, "Ben bu modeli yaptım.")
    a.cap(37.2, 40.8, "Bu videoda ona tek bir soru soracağım:")
    a.text(41.0, 55.0, 1000, 330, "Yazı-turadan", "Head", CREAM, size=110,
           fade=(250, 300), extra=r"\fscx115\fscy115\t(0,260,\fscx100\fscy100)")
    a.text(41.15, 55.0, 1000, 460, "iyi mi?", "Head", CREAM, size=110,
           fade=(250, 300), extra=r"\fscx115\fscy115\t(0,260,\fscx100\fscy100)")
    a.text(42.6, 45.2, 1004, 620, "Bu bir deney. Yatırım tavsiyesi değil.", "Mono", GREY, size=32, fade=(300, 250))
    # --- 45-55  ölçüm merdiveni --------------------------------------------------
    items = ["Yönü yazı-turadan sık bilebiliyor mu?",
             "%53 dediğinde, gerçekten %53 mü?",
             "Nerede, neden yanılıyor?"]
    for i, s in enumerate(items):
        t = 46.0 + i * 2.0
        cy = 660 + i * 105
        a.moon_phase(t, 55.0, 1030, cy, 30, 0.25 + 0.25 * i, fade=(250, 300))
        a.text(t, 55.0, 1090, cy - 26, s, "Head", WHITE, size=44, fade=(250, 300),
               extra=r"\fsp4\t(0,300,\fsp0)")
    a.cap(45.4, 50.3, "Bunu tahminle değil, ölçerek bulacağız.")
    a.cap(50.5, 54.9, "Sonuç ne çıkarsa çıksın, göstereceğim.")
    # --- 55-60  model vs yazı-tura -----------------------------------------------
    coin(a, 55.0, 59.3, 640, 450, 150, 55.3, 56.6, fade=(200, 600))
    a.text(55.4, 59.3, 960, 450, "vs", "Head", DIM, an=5, size=80, fade=(200, 600))
    a.text(55.6, 59.3, 960, 680, "Model  vs.  Yazı-Tura", "Head", WHITE, an=8, size=72, fade=(200, 600))
    a.cap(56.3, 58.2, "Başlayalım.")
    a.text(58.2, 59.3, 960, 790, "BÖLÜM 1 · Model neye bakıyor?", "Mono", CREAM, an=8, size=34, fade=(250, 600))
    return a


# ---------------------------------------------------------------- kareler

def render_video(src, avatars_dir, out_path, work):
    stills = {}
    full = clean_chart(read_rgb(src, W, H, t=19.0))
    f = full
    sat = f.max(2) - f.min(2)
    grey = (sat < 22) & (f.max(2) > 28)
    grey[:, :NOW_X - 5] = False
    pred = f.copy()
    pred[grey] = BG
    stills["dark"] = darken_future(pred, 0.0)
    stills["pred"] = pred
    stills["full"] = full
    dim_full = BG + (full - BG) * 0.28
    night = night_background()

    badge = Avatar(os.path.join(avatars_dir, "avatar_C_profil_mor-halka.webp"), BADGE[2], True)
    badge_big = Avatar(os.path.join(avatars_dir, "avatar_C_profil_mor-halka.webp"), 380, True)
    portrait = Avatar(os.path.join(avatars_dir, "avatar_D_onden_mor-kapusonlu.webp"), 760, False, vignette=True)

    mont = subprocess.Popen([FF, "-hide_banner", "-loglevel", "error", "-ss", str(SRC0), "-t", str(SRC1 - SRC0),
                             "-i", src, "-vf", f"setpts=(PTS-STARTPTS)/{SPEED},fps={FPS}",
                             "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    ass_path = os.path.join(work, "intro.ass")
    build_ass().save(ass_path)
    enc = subprocess.Popen([FF, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                            "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-vf", f"ass={ass_path},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                            "-crf", "17", out_path], stdin=subprocess.PIPE)
    last_mont = None
    cream = np.array([255, 236, 190], np.float32)
    cols = np.arange(W, dtype=np.float32)
    bx, by, bs = BADGE

    for n in range(int(DUR * FPS)):
        t = n / FPS
        if t < 15.0:                                             # grafik sahneleri
            if t < 6.3:
                fr = stills["dark"].copy()
            elif t < 10.3:
                edge = NOW_X + (W - NOW_X + 80) * ramp(t, 6.3, 7.4)
                lit = (cols < edge)[None, :, None]
                fr = np.where(lit, stills["pred"], stills["dark"]).astype(np.float32)
                band = np.exp(-((cols - edge) / 34.0) ** 2) * 0.28 * (t < 7.6)
                fr += band[None, :, None] * (cream - fr) * (cols >= NOW_X)[None, :, None]
            else:
                k = ramp(t, 10.3, 10.75)
                fr = stills["pred"] + (stills["full"] - stills["pred"]) * k
                if 10.3 <= t < 10.7:                              # darbe
                    fr = np.roll(fr, int(9 * np.sin(t * 90) * (10.7 - t) / 0.4), axis=1)
            fr = fr * ramp(t, 0.0, 0.5) + BG * (1 - ramp(t, 0.0, 0.5))
            if t >= 6.0:
                mood = 0.0 if t < 10.6 else -ramp(t, 10.6, 11.2)
                badge.draw(fr, bx - 40 * (1 - ramp(t, 6.0, 6.5)), by, mood, ramp(t, 6.0, 6.5))
        elif t < M0:                                             # %53
            k = ramp(t, 15.0, 15.6)
            fr = stills["full"] + (dim_full - stills["full"]) * k
            badge.draw(fr, bx, by, -1.0 + ramp(t, 18.4, 19.4) * 0.6)
        elif t < M1:                                             # montaj
            raw = mont.stdout.read(W * H * 3)
            if len(raw) == W * H * 3:
                last_mont = np.frombuffer(raw, np.uint8).reshape(H, W, 3).astype(np.float32)
            fr = clean_chart(last_mont)
            fr = BG + (fr - BG) * (1 - 0.8 * ramp(t, 32.6, 33.0))
            badge.draw(fr, bx, by, -0.4 + 0.3 * np.sin(t * 1.3), 1 - ramp(t, 32.6, 33.0))
        else:                                                    # anlatıcı bölümleri
            fr = night.copy()
            if t < 55.0:
                glow = 0.15 + 0.12 * np.sin(t * 2.0)
                if t >= 41.0:
                    glow = 1.0 - 0.6 * ramp(t, 41.0, 43.0) + 0.1 * np.sin(t * 2.0)
                grow = ramp(t, 33.0, 34.2)
                shift = 40 * ramp(t, 45.0, 46.0)
                portrait.draw(fr, 150 - shift, 170 + 30 * (1 - grow), glow, grow)
            else:
                pulse = 0.5 + 0.5 * ramp(t, 55.3, 56.6)
                badge_big.draw(fr, 1090, 260, pulse, ramp(t, 55.0, 55.4))
            fade_out = 1 - ramp(t, 59.2, 60.0)
            fade_in = ramp(t, 33.0, 33.5) if t < 34 else 1.0
            fr = BG + (fr - BG) * fade_out * fade_in
        enc.stdin.write(np.clip(fr, 0, 255).astype(np.uint8).tobytes())
        if n % 600 == 0:
            print(f"  kare {n}/{int(DUR * FPS)}", flush=True)
    enc.stdin.close()
    enc.wait()
    mont.kill()
    mont.wait()


# ---------------------------------------------------------------- ses

def render_audio(path):
    n = int(DUR * SR)
    t = np.arange(n) / SR
    mix = np.zeros(n, np.float32)
    rng = np.random.default_rng(7)

    def env(a, b, att=0.01, rel=0.3):
        e = np.clip((t - a) / att, 0, 1) * np.clip(1 - (t - b) / rel, 0, 1)
        return e * (t >= a)

    def add(sig, a, gain):
        i = int(a * SR)
        seg = sig[: n - i]
        mix[i:i + len(seg)] += seg * gain

    # zemin: iki bölümlü yumuşak akor (Am → F), yavaş tremolo
    for freqs, a, b in [((110.0, 164.81, 261.63, 329.63), 0.0, 33.4), ((87.31, 130.81, 220.0, 329.63), 33.0, 60.0)]:
        e = env(a, b, 2.0, 1.6)
        for k, fq in enumerate(freqs):
            mix += (np.sin(2 * np.pi * fq * t + k) + 0.3 * np.sin(2 * np.pi * fq * 2.003 * t)) \
                   * e * (0.55 + 0.45 * np.sin(2 * np.pi * (0.07 + 0.02 * k) * t)) * 0.022
    mix[t > 59.0] *= np.clip((60.0 - t[t > 59.0]), 0, 1)

    def tick(fq=1500, d=0.05):
        tt = np.arange(int(d * SR)) / SR
        return np.sin(2 * np.pi * fq * tt) * np.exp(-tt * 70)

    def whoosh(d=1.1):
        tt = np.arange(int(d * SR)) / SR
        noise = rng.standard_normal(len(tt)).astype(np.float32)
        lp = np.convolve(noise, np.ones(40) / 40, mode="same")
        return lp * np.sin(np.pi * tt / d) ** 2

    def thud(d=0.8):
        tt = np.arange(int(d * SR)) / SR
        fq = 75 * np.exp(-tt * 2.5) + 35
        return np.sin(2 * np.pi * np.cumsum(fq) / SR) * np.exp(-tt * 4.5)

    def ting(d=1.2):
        tt = np.arange(int(d * SR)) / SR
        return (np.sin(2 * np.pi * 2350 * tt) + 0.5 * np.sin(2 * np.pi * 3530 * tt)) * np.exp(-tt * 5)

    def boom(d=2.2):
        tt = np.arange(int(d * SR)) / SR
        return np.sin(2 * np.pi * 55 * tt) * np.exp(-tt * 2.2) + 0.25 * np.sin(2 * np.pi * 880 * tt) * np.exp(-tt * 3)

    for k in range(3):
        add(tick(1400 if k < 2 else 1900), 3.5 + k, 0.35)
    add(whoosh(1.2), 6.2, 0.55)
    add(thud(), 10.3, 0.9)
    for k in range(10):
        add(tick(2600, 0.02), 19.8 + k * 0.09, 0.12)
    add(ting(), 20.7, 0.3)
    for _, _, st in SAMPLES[1:]:
        add(tick(900, 0.08), M0 + (st - SRC0) / SPEED, 0.25)
    add(whoosh(0.8), 32.6, 0.35)
    add(boom(), 41.0, 0.55)
    for k in range(3):
        add(tick(1100 + 250 * k, 0.1), 46.0 + 2 * k, 0.3)
    add(whoosh(1.0), 54.9, 0.4)
    for k in range(14):
        add(tick(2600, 0.02), 55.3 + k * 0.09, 0.12)
    add(ting(), 56.6, 0.3)
    add(boom(), 58.2, 0.35)

    mix /= max(1e-6, np.abs(mix).max()) / 0.7
    stereo = np.stack([mix, mix], 1).astype(np.float32)
    ff("-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", path, input=stereo.tobytes())


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, avatars = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    out = os.path.abspath(sys.argv[3] if len(sys.argv) > 3 else "intro_v2.mp4")
    work = tempfile.mkdtemp(prefix="introv2_")
    vid, wav = os.path.join(work, "v.mp4"), os.path.join(work, "a.wav")
    print("görüntü…")
    render_video(src, avatars, vid, work)
    print("ses…")
    render_audio(wav)
    ff("-i", vid, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest",
       "-movflags", "+faststart", out)
    shutil.rmtree(work)
    print("→", out)


if __name__ == "__main__":
    main()
