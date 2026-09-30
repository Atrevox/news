# KAT-S 1.0 — YouTube videosu planı

Bu klasörde:

| Dosya | Ne |
|---|---|
| `kat-s_intro_60s.mp4` | 10 dakikalık videonun kurgulanmış ilk dakikası (1080p60, sessiz; seslendirme ve müzik sonradan eklenecek) |
| `seslendirme_ilk_dakika.srt` | İlk dakikanın seslendirme metni, kurguyla saniye saniye eşleşik (kayıtta tempo rehberi + YouTube altyazısı) |
| `build_intro.py` | İlk dakikayı kaynak klipten yeniden üreten script (yalnızca ffmpeg gerekir) |

```bash
pip install imageio-ffmpeg        # ya da sistemde libass'li bir ffmpeg
python3 video/build_intro.py kaynak_klip.mp4 video/kat-s_intro_60s.mp4
```

---

## 1. Kaliteli bir model videosu için neler önemli

### Güvenilirlik her şeyden önce gelir
Fiyat tahmini videolarına izleyici baştan şüpheyle bakar. Videonun kalitesini en çok bu belirler:

- **Iskaları göster.** İlk dakikada bilerek 08/08'deki ıskayı koydum. Bir ıska göstermek, isabetleri inandırıcı yapar.
- **Örneklerin nasıl seçildiğini söyle.** "8 rastgele an" mı, "en iyi 8 an" mı? Rastgele değilse izleyici bunu fark eder.
- **Basit bir kıyas (baseline) koy.** "Fiyat 50 dk boyunca hiç değişmez" (naive) tahmini ve düz trend uzatması. KAT-S bunları geçemiyorsa hiçbir grafik ikna etmez; geçiyorsa videonun zirvesi bu an olur.
- **Tek bir sayı değil, birkaç ölçü göster:**
  - yön isabeti (%),
  - ortalama hata (naive tahmine oranla),
  - **kalibrasyon**: model "P↑ 0.53" dediğinde fiyat gerçekten ~%53 oranda yükseliyor mu? Klipteki P↑ değerleri 0.43–0.54 aralığında, yani model genelde yazı-tura civarında konuşuyor. Bu çok iyi bir anlatı konusu: "Model ne zaman emin, ne zaman değil?"
- **Test verisini açıkça ayır.** Eğitim / doğrulama / test zaman sırasına göre ayrılmalı ve gelecekten sızıntı (look-ahead) olmamalı. Bunu bir cümleyle bile söylemek güven verir.
- **Ölçeği görünür yap.** Mevcut render'da fiyat ekseni yok, izleyici hatanın 5 $ mı 500 $ mı olduğunu bilemiyor. Sağa küçük bir fiyat ekseni ya da "±0,2 %" gibi bir ölçek ekle. Referans: σ 0,03 %/dk ise 50 dakikalık tipik hareket ≈ √50 × 0,03 % ≈ 0,21 %.
- **Sona kısa bir uyarı ekle:** "Yatırım tavsiyesi değildir."

### Görsel dil
- **Renkleri hiç değiştirme.** Parlak camgöbeği/amber her zaman tahmin, gri her zaman gerçek. Bunu ilk 10 saniyede öğret, sonra her sahnede aynı kalsın.
- **Her sahnede tek fikir.** Bir karede en fazla bir yeni etiket olsun. "Ekranı okuyalım" bölümü bu yüzden 4 adıma bölündü.
- **Kritik anı yavaşlat ya da dondur.** Klipte her tahmin ~1,2 sn ekranda kalıyor, izleyici için çok hızlı. Kurguda bu karelerde 4–19 sn duruluyor.
- **Ekranda 3–6 saniyede bir değişiklik olsun:** yeni etiket, yakın plan ya da kesme.
- **Telefonda okunabilirlik.** 1080p'de gövde yazıları ≥ 34 px, başlıklar ≥ 46 px olmalı. Alt ~%10'luk alanı YouTube oynatıcı çubuğu kapatır, önemli bilgiyi oraya koyma.
- **İnce çizgiler sıkıştırmada ölür.** 1 px'lik mum fitilleri YouTube'da bulanıklaşır. İki önlem:
  1. Model görselini doğrudan **4K** render et, çizgileri biraz kalınlaştır.
  2. 1080p kurguyu bile **4K'ya büyütüp yükle.** YouTube 4K yüklemelere daha yüksek bitrate'li VP9/AV1 kodlama verir; ince çizgiler 1080p izlemede bile belirgin şekilde keskinleşir.

### Ses (görüntüden daha önemli)
- İzleyici kötü görüntüyü affeder, kötü sesi affetmez. Sessiz bir oda, ağza 15–20 cm mesafe ve düzgün bir USB/XLR mikrofon yeterli.
- Kayıttan sonra gürültü azaltma, hafif kompresör ve toplam ses seviyesi ≈ −14 LUFS (YouTube normu).
- Müzik sesin altında kalsın: konuşma varken ~−20 dB, konuşma yokken kısmen yükselsin (ducking).
- Her tahmin "reveal" anına kısa, tutarlı bir ses efekti (whoosh/tık) ekle. Tekrarlanan bir ses efekti izleyiciye "önemli an" sinyali verir.

### Paketleme
- **Kapak:** tek bir örnek (tahmin ve gerçek yan yana) + en fazla 3–4 kelime. Örnek: "YZ Bitcoin'i Tahmin Etti?"
- **Başlık** merak uyandırsın ama yalan söylemesin. Sonuç zayıfsa "Bitcoin'i tahmin eden model yaptım — işte gerçek sonuçlar" dürüst ve tıklanabilir bir başlık.
- **Bölümler (chapters):** açıklamaya zaman damgaları ekle (aşağıdaki plan hazır).
- **Shorts:** Her reveal anı dikey (9:16) bir kısa video olabilir. Grafiğin sağ tarafını kırpıp "Tahmin mi, gerçek mi?" sorusuyla yayınla ve ana videoya link ver.

### Araçlar
- **Kurgu:** DaVinci Resolve (ücretsiz). Kurgu, renk ve Fairlight ile ses tek programda.
- **Programatik animasyon:** grafikler zaten kodla üretildiği için en temiz sonuç, sahneleri de kodla üretmek. Seçenekler:
  - `build_intro.py` gibi ffmpeg + ASS yaklaşımı (sıfır bağımlılık),
  - Python'da **Manim**,
  - TypeScript'te **Motion Canvas** ya da **Remotion**.
- **Seslendirme:** kendi sesin en inandırıcısı. TTS kullanacaksan bunu açıklamada belirt.

---

## 2. 10 dakikalık bölüm planı

| Zaman | Bölüm | İçerik |
|---|---|---|
| 0:00–1:00 | **Açılış** | Soru, bir isabet, bir ıska, başlık, ekranı okuma, 8 örnek, yol haritası *(hazır: `kat-s_intro_60s.mp4`)* |
| 1:00–2:15 | **Neden zor?** | 1 dakikalık BTC verisi neredeyse rastgele yürüyüş gibi davranır. σ 0,03 %/dk → 50 dk'da ±0,2 %. Gürültü ile sinyal farkını tek bir animasyonla göster. |
| 2:15–3:45 | **KAT-S neye bakıyor?** | Girdi penceresi (kaç mum, hangi özellikler), çıktı: 50 barlık yol + P↑ + σ. Bir örneği adım adım izle. |
| 3:45–5:00 | **Nasıl eğitildi?** | Veri aralığı; eğitim/doğrulama/test zaman çizelgesi (renkli bir şerit animasyonu); sızıntıdan nasıl kaçınıldı. |
| 5:00–7:15 | **Sonuçlar** | Yüzlerce test örneği: yön isabeti, hata / naive oranı, kalibrasyon grafiği. Naive ve trend kıyasları yan yana. *Videonun doruk noktası.* |
| 7:15–8:30 | **Nerede yanılıyor?** | En kötü 3 örnek: ani haber/spike, trend dönüşleri. 08/08 buraya geri dönüyor. |
| 8:30–9:30 | **Ne öğrendim, sırada ne var?** | KAT-S 2.0 fikirleri; izleyiciye soru (yorumlara). |
| 9:30–10:00 | **Kapanış** | Özet cümle, "yatırım tavsiyesi değildir", abone ol / sonraki video. |

---

## 3. İlk dakika: sahne akışı ve seslendirme

| Zaman | Görüntü | Seslendirme |
|---|---|---|
| 0:00–0:05 | 08:02 anı; tahmin bölgesi maskeli, kesikli "ŞİMDİ" çizgisi, "?" | *Bitcoin, 20 Haziran sabahı, saat 08:02. Sonraki elli dakikada ne olacak?* |
| 0:05–0:11 | Maske kayar; tahmin ve gerçek görünür; renk açıklaması ve "50 dk" parantezi | *Bu parlak mumları bir model çizdi, sağdaki elli dakikanın hiçbirini görmeden. Gri olanlar gerçekte olan.* |
| 0:11–0:15 | 2× yakın plan | *Ve bu örnekte neredeyse üst üste.* |
| 0:15–0:21 | 13:46 anı (08/08): model yukarı, fiyat aşağı | *Ama dürüst olalım, her zaman böyle değil. Burada model yükseliş bekledi, fiyat önce sert düştü.* |
| 0:21–0:28 | Başlık kartı, bulanık grafik üstünde "KAT-S 1.0" daktilo efekti | *Bu model KAT-S. Bu videoda tek bir soruya cevap arıyoruz: gerçekten işe yarıyor mu?* |
| 0:28–0:47 | "Ekranı okuyalım": ① geçmiş ② tahmin anı ③ 50 bar ④ durum satırı | *Önce ekranı okuyalım. Soldaki mumlar geçmiş: modelin gördüğü tek şey bu, bir dakikalık Bitcoin fiyatları. Kesikli çizgi tahmin anı; model burada durur ve ileriyi çizer. Sağ taraf elli bar, yani elli dakika ileri. Alttaki satırda P-yukarı: elli dakika sonra fiyatın daha yukarıda olma olasılığı, burada yüzde elli üç. Sigma da modelin beklediği oynaklık.* |
| 0:47–0:55 | 8 örneğin hepsi, 2,3× hızlı | *Aynı günden sekiz farklı an. Bazılarında isabetli, bazılarında değil. Peki kaçında haklı çıktı?* |
| 0:55–1:00 | "Bu videoda" yol haritası → "Başlayalım." | *Bunu yüzlerce örnekle ve basit yöntemlerle kıyaslayarak test edeceğiz. Başlayalım.* |

Kurgu ve seslendirme bilerek aynı anda başlıyor: seslendirmeyi `.srt` dosyasına bakarak kaydet, sonra Resolve'da videonun altına yerleştir. Müzik girişi için en iyi an 0:05, yani maskenin kaydığı an.

### Doğrulanması gerekenler
Videoya yazdığım bazı etiketler klipten yaptığım okumalara dayanıyor. Yanlışsa `build_intro.py` içindeki metni değiştir:

- **P↑ h50:** "50 bar sonra fiyatın daha yukarıda olma olasılığı" olarak yorumladım.
- **σ:** "modelin beklediği (bar başı) oynaklık" olarak yorumladım.
- **1 dakikalık mumlar:** kaydırma hızından ölçtüm. Grafik zaman damgası başına ~4 px kayıyor, bar genişliği de ~4 px.
- **Maskeleme:** 08:02'de kesikli çizginin sağında kalan her şey (tahmin + gerçek) maskeleniyor. Çizgi, `NOW_X = 1675` değeriyle elle konumlandı.
