# Giriş v2: ay-kafa anlatıcılı ilk dakika

`intro_v2.mp4`: 60 sn, 1080p60, altyazılı (seslendirme metni ekranda), sentezlenmiş müzik zemini ve ses efektleri.
`seslendirme_v2.srt`: aynı metin, kayıt için zamanlı.
`render_intro_v2.py`: yeniden üretmek için:

```bash
python3 video/v2/render_intro_v2.py kaynak_klip.mp4 research/avatar video/v2/intro_v2.mp4
```

## Akış

| Zaman | Olay | Neden (bkz. `research/arastirma_krafer_kat-s_video.md`) |
|---|---|---|
| 0:00–0:06 | 13:46 anı, gelecek karanlıkta. "Sizce ne olur?" YUKARI/AŞAĞI seçenekleri ve 3-2-1 sayacı | İzleyiciyi tahmine davet (Primer). Gelecek siyah kutuyla değil karanlıkla gizleniyor (Krafer'ın "cover up" metaforundan ayrışma) |
| 0:06–0:10 | Ay ışığı soldan sağa geçer, yalnızca **modelin tahminini** aydınlatır: yukarı. Ay rozeti girer | Avatara özgü görsel: ay ışığı = tahmin |
| 0:10–0:15 | Gerçekleşen fiyat belirir: sert düşüş. Ekran sarsılır, ayın ışığı söner | Gerçek bir ıska; mizah ve anlatı motoru bu (Krafer'daki "cheating" işlevi, uydurmasız) |
| 0:15–0:23 | P↑ 0.53 = yarım ay; "neredeyse yazı-tura", para döner | Anlatıcı kendini düzeltiyor, dürüst niteleme (Stuff Made Here) |
| 0:23–0:33 | 8 örnek hızlı; her birinde ay evresi göstergesi (0.44–0.53) | "Ay ne doldu, ne karardı": klibin gerçek verisinden çıkan, karaktere özgü tespit |
| 0:33–0:45 | Anlatıcı açığa çıkar: "Ben bu modeli yaptım." Soru: **Yazı-turadan iyi mi?** + "Yatırım tavsiyesi değil" | Anlatıcı kimliği, videonun asıl sorusu, erken ve içten uyarı (Barış Özcan) |
| 0:45–0:55 | Ölçüm merdiveni: yön isabeti, kalibrasyon, hatalar (ay evreleri büyüyerek) | Kademeli vaat (Lague). **Sonuç değil, yöntem** vaat ediliyor |
| 0:55–1:00 | Model vs. Yazı-Tura → "BÖLÜM 1 · Model neye bakıyor?" | 10 dakikalık videoya geçiş |

## Bilinçli tercihler
- **Model adı gösterilmiyor.** Klipteki "KAT-S 1.0" başlığı kapatıldı, anlatımda "modelim" deniyor. Sebep: Krafer'ın KAT™ ürünüyle karışma riski (araştırma §0.3). Ad kararı verilince eklenebilir.
- **Hiçbir sonuç uydurulmadı.** Gösterilen her şey klipte var: 13:46 ıskası ve 8 P↑ değeri (0.53, 0.53, 0.49, 0.44, 0.45, 0.45, 0.50, 0.53). Merdivendeki üç soru henüz cevaplanmadı.
- **Ay evresi göstergesi:** aydınlık kesir = P↑ (0 yeni ay = kesin düşüş, 1 dolunay = kesin yükseliş).
- Avatar görsellerinden yalnızca mevcut olanlar kullanıldı. Profil rozeti (mor halka) dairesel maskeyle, önden portre vinyetle kullanıldı. Ay ışığının parlaması ve sönmesi görselden çıkarılan maskeyle yapıldı; yeni poz çizilmedi.

## Yayından önce gerekenler
1. **Seslendirme:** `seslendirme_v2.srt` ile kendi sesini kaydet. Altyazı sesle birlikte kalabilir ya da kaldırılabilir (`a.cap` satırları).
2. **Müzik:** Sentez zemin geçici. Lisanslı bir ambient parçayla değiştirmek iyi olur. Ses efektleri korunabilir.
3. **Ad kararı** ve gerekirse ekrana eklenmesi.
4. Merdivendeki üç ölçümün gerçekten yapılması. Video bunları vaat ediyor.
5. Klipteki 20 Haziran verisinin test verisi olduğunun doğrulanması.
