#!/usr/bin/env python3
"""KAT-S 1.0 tanıtım videosunun ilk 60 saniyesini kaynak klipten kurgular.

Kullanım:
    python3 video/build_intro.py <kaynak.mp4> [çıktı.mp4]

Gereken tek şey bir ffmpeg ikilisi (libass + libx264 destekli). FFMPEG ortam
değişkeniyle verilebilir; yoksa imageio-ffmpeg'in ikilisi, o da yoksa PATH'teki
ffmpeg kullanılır.

Kaynak klip varsayımları (21 sn, 1920x1080, 60 fps):
  * Parlak (camgöbeği/amber) mumlar = KAT-S tahmini, gri içi boş mumlar = gerçekleşen.
  * 1 dakikalık mumlar; tahmin ufku 50 bar = 50 dakika.
  * Tahmin anı x≈1675 px, tahmin bölgesi x≈1675-1880 px.
  * 8 örnek; 01/08 duruşu ≈1.3-2.6 sn (08:02), 08/08 duruşu ≈17.8-19.5 sn (13:46).
"""
import os
import shutil
import subprocess
import sys
import tempfile

W, H, FPS = 1920, 1080, 60

# Renkler ASS formatında (&HBBGGRR&). Arka plan kaynaktaki #030407.
BG = "&H070403&"
WHITE = "&HFFFFFF&"
CYAN = "&HE0E37F&"      # tahmin mumlarının tonu
AMBER = "&H7FC8F0&"
GREY = "&HA0A0A0&"
DIM = "&H6E6E6E&"

NOW_X = 1675           # tahmin anı
PRED_X2 = 1880         # tahmin bölgesinin sağ kenarı


def find_ffmpeg():
    if os.environ.get("FFMPEG"):
        return os.environ["FFMPEG"]
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        pass
    exe = shutil.which("ffmpeg")
    if not exe:
        sys.exit("ffmpeg bulunamadı (FFMPEG=/yol/ffmpeg ile verin)")
    return exe


FF = find_ffmpeg()


def run(args):
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


# ---------------------------------------------------------------- ASS yardımcıları

ASS_HEADER = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Head,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00070403,&H96070403,1,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Body,DejaVu Sans,40,&H00FFFFFF,&H00FFFFFF,&H00070403,&H96070403,0,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Mono,DejaVu Sans Mono,30,&H00FFFFFF,&H00FFFFFF,&H00070403,&H96070403,0,0,0,0,100,100,0,0,1,3,0,7,0,0,0,1
Style: Shape,DejaVu Sans,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(sec):
    cs = int(round(sec * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


class Ass:
    def __init__(self):
        self.lines = []

    def add(self, t0, t1, text, style="Body", layer=1):
        self.lines.append(f"Dialogue: {layer},{ts(t0)},{ts(t1)},{style},,0,0,0,,{text}")

    def text(self, t0, t1, x, y, s, style="Body", color=WHITE, an=7, size=None,
             fade=(250, 250), extra=""):
        fs = rf"\fs{size}" if size else ""
        self.add(t0, t1, rf"{{\an{an}\pos({x},{y})\c{color}{fs}\fad({fade[0]},{fade[1]}){extra}}}{s}", style)

    def rect(self, t0, t1, x1, y1, x2, y2, color=BG, alpha="&H00&", fade=(0, 0),
             extra="", layer=0):
        path = f"m 0 0 l {x2 - x1} 0 {x2 - x1} {y2 - y1} 0 {y2 - y1}"
        self.add(t0, t1, rf"{{\an7\pos({x1},{y1})\p1\bord0\shad0\c{color}\alpha{alpha}"
                         rf"\fad({fade[0]},{fade[1]}){extra}}}{path}", "Shape", layer)

    def line(self, t0, t1, x1, y1, x2, y2, color=WHITE, width=3, fade=(200, 200), alpha="&H00&"):
        if x1 == x2:
            self.rect(t0, t1, x1 - width // 2, y1, x1 + (width + 1) // 2, y2, color, alpha, fade, layer=2)
        else:
            self.rect(t0, t1, x1, y1 - width // 2, x2, y1 + (width + 1) // 2, color, alpha, fade, layer=2)

    def dashed_v(self, t0, t1, x, y1, y2, color=WHITE, dash=14, gap=10):
        y = y1
        while y < y2:
            self.line(t0, t1, x, y, x, min(y + dash, y2), color, 3)
            y += dash + gap

    def typewrite(self, t0, t1, x, y, s, style="Mono", color=WHITE, size=None, cps=14):
        """Harf harf yazılan metin (sondaki imleç blok yanıp söner)."""
        fs = rf"\fs{size}" if size else ""
        step = 1.0 / cps
        for i in range(1, len(s) + 1):
            a = t0 + (i - 1) * step
            b = t0 + i * step if i < len(s) else t1
            cursor = "█" if i < len(s) else ""
            self.add(a, b, rf"{{\an7\pos({x},{y})\c{color}{fs}}}{s[:i]}{cursor}", style)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ASS_HEADER + "\n".join(self.lines) + "\n")


def legend(a, t0, t1):
    """Sağ üst köşede renk açıklaması."""
    a.rect(t0, t1, 1380, 40, 1890, 160, BG, "&H30&", (250, 250))
    a.rect(t0, t1, 1405, 82, 1455, 88, CYAN, fade=(250, 250), layer=2)
    a.text(t0, t1, 1470, 62, "KAT-S tahmini", "Mono", CYAN)
    a.rect(t0, t1, 1405, 127, 1455, 133, GREY, fade=(250, 250), layer=2)
    a.text(t0, t1, 1470, 107, "Gerçekleşen fiyat", "Mono", GREY)


def lower_third(a, t0, t1, s, color=WHITE, size=52, sub=None, sub_t0=None, top=False):
    """Yarı saydam bant üzerinde başlık (+ isteğe bağlı ikinci satır)."""
    y = 60 if top else 830
    a.rect(t0, t1, 0, y, W, y + (150 if sub else 125), BG, "&H40&", (250, 250))
    a.text(t0, t1, 80, y + 25, s, "Head", color, size=size)
    if sub:
        a.text(sub_t0 or t0, t1, 82, y + 92, sub, "Body", GREY, size=34)


# ---------------------------------------------------------------- sahneler
# Her sahne: (süre, ffmpeg girdi argümanları, video filtresi, ass nesnesi, fade)


def scene_hook(src, stills):
    """0:00-0:05  Tahmin bölgesi maskeli: 'Sonraki 50 dakikada ne olacak?'"""
    d = 5.0
    a = Ass()
    a.rect(0, d, NOW_X + 6, 120, W, 990, BG)                          # maske
    a.dashed_v(0.3, d, NOW_X, 150, 960, WHITE)
    a.text(0.5, d, NOW_X - 12, 110, "ŞİMDİ · 08:02", "Mono", WHITE, an=9)
    a.text(1.0, d, (NOW_X + W) // 2, 560, "?", "Head", CYAN, an=5, size=180,
           extra=r"\t(1000,2000,\alpha&H40&)")
    a.text(0.8, d, 80, 180, "Bitcoin · 1 dakikalık mumlar", "Mono", DIM, fade=(300, 0))
    lower_third(a, 1.5, d, "Sonraki 50 dakikada ne olacak?")
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c1"]], None, a, (0.4, 0)


def scene_reveal(src, stills):
    """0:05-0:11  Maske kayar; tahmin ve gerçek birlikte görünür."""
    d = 6.0
    a = Ass()
    a.rect(0, 0.7, NOW_X + 6, 120, W, 990, BG,
           extra=rf"\move({NOW_X + 6},120,{W},120,0,700)")
    a.dashed_v(0, d, NOW_X, 180, 960, WHITE)
    legend(a, 0.8, d)
    # 50 dakikalık ufuk parantezi
    a.line(1.6, d, NOW_X, 380, PRED_X2, 380, WHITE, 3)
    a.line(1.6, d, NOW_X, 368, NOW_X, 392, WHITE, 3)
    a.line(1.6, d, PRED_X2, 368, PRED_X2, 392, WHITE, 3)
    a.text(1.6, d, (NOW_X + PRED_X2) // 2, 355, "50 dk", "Mono", WHITE, an=2)
    lower_third(a, 3.2, d, "Model bu 50 mumu hiç görmeden çizdi.")
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c1"]], None, a, (0, 0)


def scene_hit(src, stills):
    """0:11-0:15  Yakın plan: tahmin gerçeğin üstüne oturuyor."""
    d = 4.0
    a = Ass()
    lower_third(a, 0.3, d, "Bu örnekte neredeyse üst üste.", CYAN, top=True)
    # 2x yakın plan: tahmin bölgesini çevreleyen 960x540 pencere
    vf = f"crop=960:540:{1920 - 960}:{400},scale={W}:{H}:flags=lanczos"
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c1"]], vf, a, (0, 0)


def scene_miss(src, stills):
    """0:15-0:21  08/08: model yükseliş çizdi, fiyat önce sert düştü."""
    d = 6.0
    a = Ass()
    a.dashed_v(0, d, NOW_X, 230, 960, WHITE)
    a.text(0.2, d, NOW_X - 12, 185, "ŞİMDİ · 13:46", "Mono", WHITE, an=9)
    legend(a, 0, d)
    lower_third(a, 0.4, d, "Ama her zaman değil.",
                sub="Model yükseliş çizdi — fiyat önce sert düştü.", sub_t0=2.2)
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c8"]], None, a, (0, 0)


def scene_title(src, stills):
    """0:21-0:28  Başlık kartı, bulanık grafik arka planı üzerinde."""
    d = 7.0
    a = Ass()
    a.typewrite(0.4, d, 170, 330, "KAT-S 1.0", "Mono", WHITE, size=150, cps=10)
    a.text(1.8, d, 175, 540, "Bitcoin'in sonraki 50 dakikasını tahmin eden bir model", "Body",
           WHITE, size=46)
    a.text(3.4, d, 175, 620, "Gerçekten işe yarıyor mu?", "Head", CYAN, size=58)
    vf = "gblur=sigma=18,eq=brightness=-0.02:saturation=0.6,colorlevels=romax=0.45:gomax=0.45:bomax=0.45"
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c8"]], vf, a, (0.35, 0.35)


def scene_read(src, stills):
    """0:28-0:47  Ekranı okuyalım: geçmiş, tahmin anı, ufuk, durum satırı."""
    d = 19.0
    a = Ass()
    a.rect(0, d, 1440, 40, 1890, 100, BG, "&H30&")
    a.text(0, d, 1865, 52, "EKRANI OKUYALIM", "Mono", CYAN, an=9)
    # 1) geçmiş
    a.rect(0.5, 4.8, NOW_X - 4, 110, W, 985, BG, "&H40&", (300, 300))
    a.rect(0.5, 4.8, 40, 850, 1060, 975, BG, "&H30&", (300, 300))
    a.text(0.6, 4.8, 70, 870, "① Geçmiş: modelin gördüğü veri", "Head", WHITE, size=46, fade=(300, 300))
    a.text(1.4, 4.8, 70, 930, "1 dakikalık BTC mumları", "Mono", GREY, fade=(300, 300))
    # 2) tahmin anı
    a.dashed_v(4.8, d, NOW_X, 150, 960, WHITE)
    a.rect(4.9, 12.6, 1030, 150, NOW_X - 8, 285, BG, "&H30&", (250, 250))
    a.text(4.9, 9.0, NOW_X - 20, 170, "② Tahmin anı · 08:02", "Head", WHITE, an=9, size=42)
    a.text(5.6, 9.0, NOW_X - 20, 230, "model burada durur ve ileriyi çizer", "Mono", GREY, an=9)
    # 3) ufuk
    a.line(8.8, d, NOW_X, 380, PRED_X2, 380, WHITE, 3)
    a.line(8.8, d, NOW_X, 368, NOW_X, 392, WHITE, 3)
    a.line(8.8, d, PRED_X2, 368, PRED_X2, 392, WHITE, 3)
    a.text(9.1, 12.6, NOW_X - 20, 170, "③ 50 bar = 50 dakika ileri", "Head", CYAN, an=9, size=42)
    a.text(9.8, 12.6, NOW_X - 20, 230, "parlak: tahmin · gri: gerçekleşen", "Mono", GREY, an=9)
    # 4) durum satırı
    a.rect(12.6, d, 0, 110, W, 985, BG, "&H70&", (300, 0))
    a.rect(12.6, d, 0, 990, 700, 1022, CYAN, "&HC0&", (300, 0), layer=2)
    a.line(12.9, d, 330, 960, 330, 988, CYAN, 3)
    a.text(12.9, d, 60, 700, "④ Durum satırı", "Head", WHITE, size=46, fade=(300, 0))
    a.text(13.6, d, 60, 780, "P↑ h50 0.53 → 50 bar sonra fiyatın daha yukarıda olma olasılığı ≈ %53",
           "Mono", WHITE, size=32, fade=(300, 0))
    a.text(15.0, d, 60, 840, "σ 0.030% → modelin beklediği oynaklık", "Mono", WHITE, size=32,
           fade=(300, 0))
    a.text(16.4, d, 60, 900, "01/08 → aynı gün içinden 8 farklı an", "Mono", WHITE, size=32,
           fade=(300, 0))
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c1"]], None, a, (0, 0.3)


def scene_montage(src, stills):
    """0:47-0:55  8 örneğin tamamı, 2.3x hızlı."""
    t0, t1, speed = 1.3, 19.7, 2.3
    d = (t1 - t0) / speed
    a = Ass()
    a.rect(0, d, 1380, 40, 1890, 160, BG, "&H30&", (250, 250))
    a.text(0, d, 1865, 55, "8 AN · HER BİRİ 50 DK İLERİ", "Mono", CYAN, an=9)
    a.text(0, d, 1865, 105, f"{speed:.1f}× hız", "Mono", GREY, an=9)
    lower_third(a, d - 3.6, d, "Kaçında haklı çıktı?", WHITE)
    vf = f"setpts=(PTS-STARTPTS)/{speed},fps={FPS}"
    return d, ["-ss", str(t0), "-t", str(t1 - t0), "-i", src], vf, a, (0.3, 0.3)


def scene_roadmap(src, stills):
    """0:55-1:00  Videonun geri kalanı."""
    d = 5.0
    a = Ass()
    a.text(0.1, d, 170, 170, "BU VİDEODA", "Mono", CYAN, size=40)
    items = [
        "Model neye bakıyor, neyi tahmin ediyor?",
        "Yüzlerce örnekte isabet oranı",
        "Basit yöntemlere karşı: hiç değişmez / trend",
        "Nerede yanılıyor — ve neden",
    ]
    for i, s in enumerate(items):
        t = 0.35 + i * 0.45
        a.text(t, d, 170, 260 + i * 95, f"{i + 1:02d}", "Mono", DIM, size=44)
        a.text(t, d, 260, 256 + i * 95, s, "Body", WHITE, size=48)
    a.text(2.9, d, 170, 720, "Başlayalım.", "Head", CYAN, size=64)
    vf = "gblur=sigma=18,eq=saturation=0.6,colorlevels=romax=0.35:gomax=0.35:bomax=0.35"
    return d, ["-loop", "1", "-framerate", str(FPS), "-t", str(d), "-i", stills["c1"]], vf, a, (0, 0.6)


SCENES = [scene_hook, scene_reveal, scene_hit, scene_miss, scene_title,
          scene_read, scene_montage, scene_roadmap]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "kat-s_intro_60s.mp4")
    work = tempfile.mkdtemp(prefix="kats_")
    stills = {"c1": os.path.join(work, "c1.png"), "c8": os.path.join(work, "c8.png")}
    run(["-ss", "2.2", "-i", src, "-frames:v", "1", stills["c1"]])
    run(["-ss", "19.0", "-i", src, "-frames:v", "1", stills["c8"]])

    parts, total = [], 0.0
    for i, scene in enumerate(SCENES):
        d, inputs, vf, ass, (fin, fout) = scene(src, stills)
        ass_path = os.path.join(work, f"s{i}.ass")
        ass.save(ass_path)
        chain = [vf] if vf else []
        chain += [f"scale={W}:{H}", f"fps={FPS}", "format=yuv420p",
                  f"ass={ass_path}", f"trim=duration={d}", "setpts=PTS-STARTPTS"]
        if fin:
            chain.append(f"fade=t=in:st=0:d={fin}")
        if fout:
            chain.append(f"fade=t=out:st={d - fout:.3f}:d={fout}")
        part = os.path.join(work, f"s{i}.mp4")
        run([*inputs, "-vf", ",".join(chain), "-an", "-c:v", "libx264", "-preset", "medium",
             "-crf", "16", "-pix_fmt", "yuv420p", part])
        parts.append(part)
        print(f"{scene.__name__:<15} {total:5.1f}s → {total + d:5.1f}s")
        total += d

    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{p}'\n" for p in parts)
    # Seslendirme ve müzik sonradan eklenecek; YouTube uyumu için sessiz stereo iz.
    run(["-f", "concat", "-safe", "0", "-i", lst, "-f", "lavfi", "-i",
         "anullsrc=channel_layout=stereo:sample_rate=48000", "-shortest",
         "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
         "-r", str(FPS), "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out])
    shutil.rmtree(work)
    print(f"toplam {total:.1f}s → {out}")


if __name__ == "__main__":
    main()
