# Araştırma: KAT-S videosunun anlatı ve kurgu dili

*Hazırlanma tarihi: 30 Eylül 2026. Bu dosya, konuşmanın geri kalanını görmeyen bir model ya da kişi tarafından da kullanılabilecek şekilde yazıldı.*

---

## 0. Önce okunması gerekenler

### 0.1 Konu ve bu dosyanın amacı
- **Konu:** Kanal sahibinin kendi Bitcoin tahmin modeli **"KAT-S 1.0"** hakkında yaklaşık 10 dakikalık, Türkçe, özgün bir YouTube videosu.
  - Brief'te "konuyu bu açıklamadan al" deniyor ama ayrı bir konu açıklaması gelmedi, yalnızca avatar görselleri geldi. Konu bu yüzden aynı konuşmanın önceki bölümünden alındı. Orada kullanıcı, "BTC grafiği tahmin modellerinden birinin" 21 sn'lik bir kaydını paylaştı.
  - **Bu bir varsayımdır; kullanıcının onaylaması gerekir.**
- **Amaç:** Videonun anlatı yaklaşımına, açılışına, mizahın rolüne ve görsel diline dair somut yaratıcı kararlar verebilecek kadar derin bir zemin kurmak. İlk dakikanın üretimine geçmek için neyin hazır, neyin eksik olduğunu belirlemek.
- **Hazır bir senaryo formülü uygulanmadı.** Aşağıdaki öneriler bulgulardan türetildi ve alternatifli bırakıldı.

### 0.2 Erişim sınırları (sonuçların güvenilirliğini doğrudan etkiler)

| Ne | Durum | Etkisi |
|---|---|---|
| Krafer videosunun **konuşma metni** | ✅ Exa üzerinden otomatik altyazı metni alındı (`kaynaklar/krafer_0yNfaixWyf4_transkript.txt`, 3.045 kelime) | Anlatı analizi metin üzerinden yapılabildi |
| Başlık ve kanal | ✅ YouTube oEmbed ile doğrulandı: **"I made an AI learn Stock Market Patterns" — Krafer (@Krafer)** | — |
| Yayın tarihi, açıklama | ✅ socialcounts.org: 1 Eylül 2025; açıklamada `krafercrypto.com/kat` linki | — |
| **Zaman kodları** | ❌ Altyazı zaman damgasız geldi, video süresi hiçbir kaynakta bulunamadı | Aşağıdaki zamanlar **tahmindir**; metindeki konumdan (%) ve konuşma hızından türetildi |
| **Görüntü** (kurgu, kesme, zoom, avatar, meme'ler) | ❌ İzlenemedi; bu ortamdan youtube.com, i.ytimg.com ve krafercrypto.com'a doğrudan erişim ağ politikasıyla engelli | Görsel kurguya dair **hiçbir gözlem** yapılmadı; görsel işlevler yalnızca konuşmanın ima ettiği yerlerde "olası" diye yazıldı |
| **Ses** (müzik, SFX, duraksama, vurgu) | ❌ Dinlenemedi | Altyazıdaki `[Music]` işaretleri dışında ses gözlemi yok |
| Karşılaştırma videoları | ✅ Transkript metinleri Exa ile alındı (zaman damgasız); görüntü/ses yok | Aynı sınırlar geçerli |
| İzleyici tutma (retention) verisi | ❌ Hiçbir video için bulunamadı | Hiçbir tercih "izleyiciyi tuttu" diye sunulmadı |

**Sonuç:** Bu araştırma bir **anlatı/metin araştırmasıdır**. Kurgu ritmi ve görsel dil hakkındaki her şey ya kaynağa dayanır (üreticinin kendi sözü, resmî site, GitHub) ya da açıkça **[doğrulanmadı]** diye işaretlenmiştir.
- **Üretime geçmeden önce yapılması gereken bir iş var:** Kullanıcının (ya da görüntüye erişimi olan birinin) Krafer videosunun **ilk 60 saniyesini** izleyip bölüm 2.3'teki "görsel doğrulama listesini" doldurması.

### 0.3 En kritik bulgu: "KAT" adı Krafer'a ait bir ürün adı
Bunu en başa koydum, çünkü özgünlük ve olası hukuki risk açısından bütün yaratıcı kararlardan önce geliyor.

**Kaynakta açıkça olanlar:**
- Otomatik altyazının "cat 1.3", "CAT 2", "CAT 1.4" diye yazdığı modellerin gerçek adı **KAT**. Video açıklamasındaki link `https://krafercrypto.com/kat`.
- Site başlığı: **"KAT™ - Krafer Agent Trader"** (™ işaretiyle).
- Model ailesi: Panther, Bobcat, Lion, Tiger.
  - Bobcat: "Short-term precision up to ~30 bars. Built for the 1-min timeframe."
  - Tiger: "Predicts 200 bars ahead."
  - Kaynak: https://krafercrypto.com
- Krafer Crypto kanalındaki "Using My KAT Models on Real Markets" videosunda (2 Nisan 2026) şöyle diyor: Lion modelinin tahmini "used to go up to only 50 bars … if you are a Bobcat subscriber, it is that way". Kaynak: https://www.youtube.com/watch?v=A9SuiU2vvuE
- Sitede şu ifadeler var: "Research purposes only — not financial advice". Doğruluk kartı: "Avg 64.8% … Random Walk (+/- 0.025%) KAT™ Lion".

**Kullanıcının klibi (aynı konuşmada incelendi):**
- Başlık "KAT-S 1.0".
- 1 dakikalık BTC mumları.
- "Pred 50 bars | … | P↑ h50 0.53 | σ 0.030%" durum satırı.
- Tahmin parlak mumlarla, gerçekleşen fiyat gri içi boş mumlarla gösteriliyor.
- Tarih 20 Haziran 2026.

**Yorum (kanıt değil):**
- Ad (KAT), zaman dilimi (1 dk BTC) ve ufuk (50 bar) Krafer'ın ürünüyle örtüşüyor.
- Bu, kullanıcının modelinin Krafer'dan bağımsız olmadığı anlamına **gelmez**. Ama izleyici bunu hemen fark edecektir, çünkü Krafer videosu ~324 bin görüntülenmeye sahip. Rakam socialcounts.org'dan; etiket belirsiz.
- Açılmadan bırakılırsa videonun özgünlüğünü ilk dakikada zayıflatır.

**Karar gerektiren sorular (kullanıcıya):**
1. KAT-S adı Krafer'ın KAT'ına bir gönderme mi, tesadüf mü, yoksa KAT sitesinden/kodundan türetilmiş bir çalışma mı?
2. Klipteki görselleştirme tamamen kullanıcının kendi kodu mu?
3. Önerim: Ad değişmeli ya da ilişki videoda açıkça söylenmeli ("Krafer'ın KAT'ından ilham aldım, ama …").
   - Hukuki değerlendirme bu araştırmanın kapsamı dışında.
   - Yine de ™ işaretli bir ürün adının türevini kullanmak önlem gerektiren bir risk.

---

## 1. Krafer: "I made an AI learn Stock Market Patterns"

- **Bağlantı:** https://www.youtube.com/watch?v=0yNfaixWyf4
- **Kanal:** Krafer (@Krafer). Krafer'ın ayrı bir Krafer Crypto kanalı (@KraferCrypto) ile oyun, animasyon, matematik ve müzik kanalları da var (https://krafercrypto.com/youtube).
- **Yayın:** 1 Eylül 2025 (socialcounts.org).
- **Açıklama (alıntı):** "That's right. I made an AI to predict Bitcoin's price action, at the 1-minute level. There is so much left to do…"
- **Doğrudan önceki video:** "I made a Market Simulation to see if Patterns are Real" (https://www.youtube.com/watch?v=oWheof70O9g). Referans video bunun devamı olarak açılıyor ("Last time we figured out…").

### 1.1 Zaman kodlarını nasıl okumalı
Süre bilinmediği için her olayı **transkriptteki kelime konumu (%)** ile veriyorum. Yanına iki tahmin koydum:

| Hız | Toplam süre | Açıklama |
|---|---|---|
| 165 kelime/dk | ≈ 18,5 dk | Tipik anlatım hızı |
| 280 kelime/dk | ≈ 11 dk | Anlatıcının sonda "It's already over 10 minutes" demesi gerçek süreyse (şaka olabilir) |

**Gerçek zaman kodları için videoyu açıp doğrulamak gerekiyor.** Kesin bilinen tek şey sıra.

### 1.2 Olay dizisi (videodan türetilmiş anlatı akışı)

| % (kelime) | ~165 wpm | Olay (kaynak: transkript) | Anlatıdaki işlevi (yorum) |
|---|---|---|---|
| 0 | 0:00 | "A pretty crazy question that no one has asked before is can you predict the stock market? … I think I might be the first person to ask it." | **İronik kanca.** Herkesin sorduğu klişe soru, "kimsenin sormadığı" diye sunuluyor. Konuyla birlikte anlatıcının ses tonu da ilk cümlede kuruluyor: kendinin ve türün farkında, alaycı. |
| 1,8 | ~0:20 | "I made an AI that can predict the stock market." | **Büyük vaat**, hiçbir niteleme olmadan. İzleyicinin bütün video boyunca taşıyacağı soru: *"Gerçekten mi?"* |
| 2,1 | ~0:23 | "Last time we figured out that patterns really do show up in stock charts and it's because of math, not psychology." | **Seri bağlamı ve tez.** Önceki videodaki simülasyon bulgusu, bu videonun öncülü oluyor. |
| 2–7 | 0:23–1:15 | "Head and shoulders" / kendini gerçekleştiren kehanet eleştirisi; "which came first, the pattern or the trader?" | Karşı görüşü çürütme. Bilgi yoğun, ama tavuk-yumurta esprisiyle hafifletiliyor. |
| 7–11 | 1:15–2:00 | Order book, "gap" kavramı. Absürt benzetme: havuç almak isteyen "saber-tooth tiger", küçük kardeşin harçlığı | **Teknik kavram + absürt benzetme.** Gap'i somut bir alışverişe çeviriyor. |
| 10,9 | ~2:00 | "What's this, Tino? My mom wants her gap. Please, bro. No gap fills." | **Skeç.** "Tino" adlı bir karakterle kısa diyalog. [doğrulanmadı: görüntüde ne olduğu, kimin seslendirdiği bilinmiyor] |
| 12,6 | ~2:20 | "Now, most of this isn't super important. I go into more detail on this on my Crayfer Crypto channel" | **Teknik yükü kendisi kesiyor.** Derin bilgi başka kanala yönlendiriliyor. |
| 16 | ~2:57 | "Powell says up, Powell says down. Think you can win? Then you're a clown. Sorry, I um let it shrivel. I don't know what came over me there." | **Kafiye şakası ve anlatıcının kendini düzeltmesi.** "let it shrivel" otomatik altyazıda muhtemelen yanlış duyulmuş bir ifade [doğrulanmadı]. |
| 18,4 | ~3:20 | Bir quant trader ile konuşma: firmalar yapay zekâyı "only … on the shorter time frames" kullanıyor | **Otorite kanıtı.** Neden 1 dakikalık grafik seçildiğini gerekçelendiriyor. Kaynak doğrulanamaz, anekdot. |
| 22,4 | ~4:05 | "I guess that means that we should [Music] And then they started cheating. Uh, here, let me back up." | **İleri atlama ve geri sarma.** Cümle yarıda müzikle kesiliyor, ileriden bir an ("hile yapmaya başladılar") gösteriliyor, sonra "geri saralım". İzleyiciye yeni bir soru bırakıyor: *Kim, neden hile yaptı?* |
| 22,8 | ~4:10 | "…from playing snake to playing snake to playing Tetris to playing Snake." | **Tür şakası.** "AI öğreniyor" YouTube türünün klişesiyle dalga geçiyor. İzleyicinin bu türü bildiğini varsayıyor. |
| 23–28 | 4:10–5:15 | Nöral ağ = "input random numbers… voodoo magic… spit out random numbers" | Bilerek aşırı basitleştirilmiş, esprili teknik açıklama. |
| 28,4 | ~5:15 | "Now, piggies, you good, piggy? What What even is this?" | **Görsel gag olması muhtemel** [doğrulanmadı]. "Flappy Bird" cümlesi hemen ardından geliyor. |
| 30–40 | 5:40–7:30 | **Deney 1:** kendi market simülasyonunda genetik algoritma. Girdi ~150 bar + order book, çıktı al/sat/bekle, P&L grafiği | Deneyin kuralları sade, adım adım anlatılıyor. |
| 40,7 | ~7:30 | "After about a 100 generations, they actually looked like they were doing pretty good." | **Sahte zafer.** |
| 41–45 | 7:30–8:20 | "I was only tracking their realized P&L." Poker fişi benzetmesi. "Ow, it went to zero. The bots basically learned to hide their losses." | **Dönüm noktası.** 22,4%'teki "cheating" teaser'ı burada karşılığını buluyor. Hata hem komedi hem gerçek bir trading dersi: gerçekleşmiş/gerçekleşmemiş kâr-zarar. |
| 45–50 | 8:20–9:15 | Genetik algoritmanın neden verimsiz olduğu ("millions of years") | Başarısızlık teşhisi, yön değiştirme gerekçesi. |
| 50,4 | ~9:15 | "Aha, we're booting up Python. Uh, I hate Python." | **Yeni perde.** Tavır şakasıyla açılıyor. |
| 50,7 | ~9:20 | "Hypothetically, let's just say hypothetically…" Jupyter, Keras, "past 4 months" 1 dk BTC verisi, "about 50,000 lines", sunucu, API, web sitesi | **Zaman atlama montajı.** Haftalarca süren iş, "varsayalım ki" ironisiyle tek paragrafa sıkıştırılıyor. |
| 54,4 | ~10:05 | "All right, so what's going on here? The cat [KAT] 1.3 model… trained on about 51,773 minutes… 35 complete days… all that the model tries to guess is the close of exactly one candle." | **Önce sonuç, sonra açıklama.** Ekranda bir şey gösteriliyor, ardından açıklanıyor. Ayrıca iç tutarsızlık var: "4 months" ↔ "35 days". |
| 56–63 | 10:25–11:40 | Genetik algoritma ↔ gözetimli öğrenme: "Plinko with 200 AIs" ↔ "a textbook… study for a test". "fine-tuning a radio with a million different knobs" | **Teknik açıklama, ihtiyaç duyulduğu anda** geliyor ve iki benzetmeyle taşınıyor. |
| 63,3 | ~11:40 | "if I take a Bitcoin price chart and cover up the right side and ask the AI to predict it, there is technically a right answer." | **Merkezi görsel metafor:** grafiğin sağını kapatmak. |
| 64–67 | 11:45–12:20 | "I'm using 17 megabytes of data to predict one number." | Anti-klimaks şakası; sonraki fikre zemin hazırlıyor. |
| 67–75 | 12:20–13:50 | ChatGPT benzetmesi: bir sonraki kelime ↔ bir sonraki mum; "what if I made a chat GPT of my own… predicts the next Bitcoin price" | **Sorunun dönüşümü.** "Tek mum tahmini" → "otoregresif üretim: istediğin kadar ileri". |
| 75,7 | ~13:50 | "And would you look at that? This is the CAT 2… running on test data… I want you to pay attention to these freeze frames. Surprisingly, these predictions are not far off." | **Kanıt anı:** dondurulmuş kareler ve izleyiciye doğrudan "dikkat edin" talimatı. Görsel [doğrulanmadı]. **Sayısal ölçüt verilmiyor.** |
| 76–79 | 13:50–14:35 | "there's no way the bot has ever seen this data… which means we did it." | Zafer ilanı. Test verisinin eğitimde kullanılmadığı vurgulanıyor. |
| 78,8 | ~14:35 | "Uh uh what what is that? Blows my mind. Oh, yeah." | **Tepki anı**, muhtemelen görsel bir sürprize [doğrulanmadı]. |
| 79,3 | ~14:40 | "if you want to see the rest of this video and other models I've made, then check out my Cray for Crypto channel." | **Karşılığın bir kısmı başka kanala erteleniyor.** |
| 80–87 | 14:50–16:00 | Difüzyon modeli (yapılmadı); KAT 1.3/1.4 web sitesinde, **abonelikle**; "They are not the most spectacular models in existence" | Beklentiyi düşürme ve ürün yönlendirmesi. |
| 95,5 | ~17:30 | "It's already over 10 minutes… Videos don't grow on trees." Patreon, "quit my job at Walmart", Discord | Kapanış şakaları ve çağrılar (CTA). |

### 1.3 İzleyicinin bilgisi: ne zaman neyi biliyor?
- **İlk ~20 saniye (metne göre):**
  - İzleyici **konuyu** (piyasayı tahmin etmek), **anlatıcının tonunu** (alaycı, kendinin farkında) ve **vaadi** ("tahmin eden bir yapay zekâ yaptım") biliyor.
  - **Bilmedikleri:** Nasıl yapıldığı, ne kadar iyi çalıştığı, "tahmin"in neyi kapsadığı (yön mü, fiyat mı, kaç dakika).
- **İlk ~1 dakika:** Seri bağlamı ve teorik tez ekleniyor (desenler = order book matematiği). Bu, yapay zekânın **neden kısa zaman diliminde** çalışacağını söyleyen bir ön kabul. Yani açılış yalnızca merak uyandırmıyor, sonraki deneylerin kurallarını da kuruyor.
- **Teknik açıklamaların zamanlaması:** Neredeyse her zaman bir **deneyden hemen önce** ya da **bir görüntü gösterildikten hemen sonra** geliyor:
  - Nöral ağ temeli, genetik algoritma deneyinden önce.
  - Gözetimli öğrenme, KAT 1.3 gösterildikten sonra.
  - LLM benzetmesi, KAT 2 gösterilmeden önce.
  - Teori yükü ağırlaştığında anlatıcı kendisi kesiyor: "most of this isn't super important".
- **Takip edilen soru dönüşüyor:**
  1. "Piyasa tahmin edilebilir mi?"
  2. "Psikolojinin az olduğu kısa zaman diliminde desen yakalanabilir mi?"
  3. "Botlar para kazanmayı öğrenebilir mi?" → **başarısızlık** (kayıpları saklıyorlar)
  4. "Bir model tek bir mumu tahmin edebilir mi?"
  5. "ChatGPT gibi mum mum ileriyi üretebilir mi?"
  6. "Test verisinde fena değil" → web sitesi ve kanal

  Her dönüşümü **somut bir olay** tetikliyor: bir başarısızlık, bir teşhis ya da bir benzetme.

### 1.4 Vaat ve karşılık muhasebesi

| Açılışta kurulan | Sonradan karşılığı | Değerlendirme (yorum) |
|---|---|---|
| "I made an AI that can predict the stock market" | KAT 2'nin dondurulmuş kareleri: "not far off" | **Kısmi.** Transkriptte hiçbir sayısal ölçüt, basit yöntemle kıyas ya da isabet oranı yok. Sitedeki "%64,8" iddiası videoda geçmiyor. |
| "patterns … math, not psychology" (önceki video) | Order book'un genetik algoritmaya girdi olması; kısa zaman dilimi gerekçesi | Öncül işlevi görüyor. Nihai modelin order book kullanıp kullanmadığı söylenmiyor. |
| "And then they started cheating" (ileri atlama) | Gerçekleşmiş P&L hatası, "learned to hide their losses" | **Tam karşılık.** Videonun en sağlam kurulum → karşılık çifti. |
| "playing snake…" tür şakası | "trading and Flappy Bird … same amount of brain power" | Tür mizahı iki kez geri dönüyor. |
| "cover up the right side" | Dondurulmuş kareler | Metafor, kanıt anının görsel dilini hazırlıyor (görüntü doğrulanmadı). |
| Merak: "gerçekten çalışıyor mu?" | "check out my … Crypto channel", abonelikli site | **Bir kısmı video dışına erteleniyor.** Bu, rakip bir video için açık bir boşluk bırakıyor (bkz. §5). |

### 1.5 Anlatıcı ve mizah (metinden anlaşılanlar)
**Kişilik:**
- Alaycı, kendini tiye alan, türün klişelerinin farkında.
- İzleyiciyle "biz" kuruyor: "Last time we figured out", "let's get cracking".
- Kendi yetkinliğini hem öne çıkarıyor ("I am the first person to make a market simulation…") hem de yıkıyor ("I hate Python", "They are not the most spectacular models").

**Mizah kaynakları:**
1. **İroni ve abartı:** açılış cümlesi, "For centuries, people and YouTubers…", "hyperdimensional calculus".
2. **Absürt benzetme:** kılıç dişli kaplan ve havuç, poker fişi, Plinko, radyo düğmeleri. Bunlar yalnızca şaka değil, **teknik kavramı taşıyor**.
3. **Gerçek başarısızlık:** kayıplarını saklayan botlar. En güçlü mizah, deneyin kendisinden çıkıyor.
4. **Anlatıcının tepkisi ve kendini düzeltmesi:** "Sorry… I don't know what came over me there", "what what is that? Blows my mind".
5. **Kültürel referans:** Powell (FED), ChatGPT/Gemini, Snake/Tetris/Flappy Bird, Walmart.
6. **Skeç ve karakterler:** Tino, "piggies", "Chris". Görsel ya da sesli bir karşılıkları olması muhtemel, ama doğrulanmadı.

**Mizahın anlatıya etkisi (yorum):**
- Şakalar teori yoğunluğunun olduğu bölgelerde sıklaşıyor (~%7–%30).
- Deney ve sonuç bölümlerinde **tepkiye** dönüşüyor.
- En işlevsel şaka, anlatının dönüm noktasıyla aynı olay: "cheating".

**Doğruluk notu:** Bazı teknik ifadeler bilerek ya da bilmeyerek hatalı:
- "ChachiBT3 used 70 billion neurons": GPT-3 175 milyar parametre; nöron ile parametre de aynı şey değil.
- "4 months" ↔ "35 days" tutarsızlığı.

Bir Türkçe video, bu tür gevşekliği **ayırt edici bir fark** olarak kullanabilir (bkz. §5).

**Ses:** Transkriptte yalnızca `[Music]` işaretleri var. Biri %22,4'teki kesmede (ileri atlama anı), biri sonda.
- Müziğin dramatik bir kesme olarak kullanıldığı bu tek noktadan çıkarılabilir.
- Vurgu, duraksama, ses efekti ve müzik seçimi hakkında **gözlem yok**.

### 1.6 Görsel anlatım: metinden çıkarılabilenler ve doğrulanması gerekenler
Konuşmanın doğrudan görüntüye atıf yaptığı yerler şunlar. Bu cümleler ekranda bir şey olduğunu gösteriyor, ama **ne olduğunu göstermiyor**:
- "and then you get this" (%25)
- "What even is this?" (%28)
- "this is how they did" (%40)
- "Ow, it went to zero" (%45)
- "So what's going on here?" (%54)
- "would you look at that? This is the CAT 2" (%76)
- "pay attention to these freeze frames" (%76)
- "what is that?" (%79)
- "Ooh, look, my next video" (%96)

**Bağlamdan gelen, kısmen kaynaklı bilgiler:**
- Krafer market simülasyonunu **Unity'de, GPU shader'larıyla** yazdığını önceki videoda söylüyor: "In Unity, the shader scripts end up using the GPU". Referans videoda: "Unity is not a great place to code up AI".
- Yani ekranda büyük olasılıkla kendi simülasyon arayüzü ve grafikleri var. Görüntü doğrulanmadı.
- Krafer'ın ayrı bir **animasyon kanalı** var (@therearetwoofusinhere). Tino ve piggies skeçlerinin animasyonlu olması **olası**, ama doğrulanmadı.

### 1.7 Görsel doğrulama listesi (üretimden önce doldurulmalı)
Krafer videosunun ilk 60–90 sn'sini izleyip her satır için zaman kodu ve gözlem yazın:
1. İlk kare: Anlatıcı görünüyor mu (avatar, yüz, hiçbiri)? Başlık kartı var mı?
2. "can you predict the stock market?" cümlesinde ekranda ne var? İroni görüntüyle mi destekleniyor (ör. bir arama sonucu, sahte gazete)?
3. "I made an AI…" cümlesinde model çıktısı gösteriliyor mu, yoksa vaat yalnızca sözlü mü?
4. "Last time…" bölümünde önceki videodan görüntü var mı?
5. Head & shoulders / order book açıklamasında animasyonlu diyagram mı, ekran kaydı mı var?
6. Havuç ve kaplan benzetmesi ile Tino skeçinde çizim, animasyon ya da meme kullanılıyor mu? Ne kadar sürüyor?
7. Ortalama kesme sıklığı (ilk dakikada kaç kesme, zoom, yazı var).
8. Müzik ne zaman giriyor ve ne zaman susuyor? Ses efektleri şakalarda mı, sonuçlarda mı?
9. %76'daki "freeze frames" nasıl gösterilmiş: renk kodu, tahmin ve gerçek ayrımı, ekranda kalma süresi?

---

## 2. Karşılaştırmalı araştırma
Amaç "ortalama iyi video" çıkarmak değil. Aynı türden teknik bir konunun farklı yaratıcı tercihlerle nasıl **farklı izleme deneyimlerine** dönüştüğünü görmek.

- Tüm başlıklar Exa transkript alımıyla doğrulandı.
- Alıntılar otomatik altyazıdan, zaman damgası yok.
- Görüntü ve ses incelenmedi.
- Bir alt araştırmacının (aynı ortamda çalışan ayrı bir model oturumu) raporundan derlendi; ayrıntılı alıntılar orada kontrol edilerek aktarıldı.

### 2.1 Neden bu örnekler?

| Üretici ve video | Seçilme nedeni | Temsil ettiği yaklaşım |
|---|---|---|
| **Code Bullet** — "A.I. LEARNS to Play Hill Climb Racing" (https://www.youtube.com/watch?v=SO7FFteErWs) | "AI öğreniyor" türünün komedi kutbu. Krafer'ın "playing snake" şakası bu türe atıf | Başarısızlıktan komedi, yüzsüz avatar |
| **b2studios** — "AI Learns To Swing Like Spiderman" (https://www.youtube.com/watch?v=Y48Vk77MoYg) | Sonucu en başta gösterip açıklamayı sonradan kazanan yapı | Önce sonuç, sonra uzun teori |
| **Pezzza's Work** — "AI Cat Learns to Run" (https://www.youtube.com/watch?v=aBp-3pmKNBY) | Neredeyse mizahsız mühendislik günlüğü; aynı türün sakin kutbu | Süreç ve sayılarla güvenilirlik |
| **Michael Reeves** — "I Gave My Goldfish $50,000 to Trade Stocks" (https://www.youtube.com/watch?v=USKD3vPD6ZA) | Konuya en yakın örnek (borsa ve otomasyon); absürt temel çizgi | Karakter çatışmasıyla benchmark |
| **Sebastian Lague** — "I Tried Coding a Neural Network to Identify Doodles" (https://www.youtube.com/watch?v=hfMk-kjRv4c) | Kademeli vaat ve dürüst tavan; nöral ağı sıfırdan anlatma | Sakin merak, başarısızlığı kabul |
| **Stuff Made Here** — "My curved basketball hoop always goes in" (https://www.youtube.com/watch?v=vtN4tkvcBMA) | "Her zaman giriyor" vaadinin videonun sonunda nitelenmesi; finans vaadine birebir benzer sorun | Sihir numarası gibi açılış ve nitelenmiş iddia |
| **Primer** — "Simulating Natural Selection" (https://www.youtube.com/watch?v=0ZGbIKd0XrM) | İzleyiciyi tahmine davet eden sakin anlatıcı; ürün zaten bir "tahmin" | Katılım: "sen ne tahmin ederdin?" |

### 2.2 Bulgular

**Code Bullet**
- **Kaynak:**
  - Açılış rahat bir özürle başlıyor ("Long time no see… That's my bad"). Vaat ~30 sn içinde geliyor: "Time to AI the [ __ ] out of it".
  - Başarısızlık slapstick olarak anlatılıyor ("Silly car. Where are your wheels?"). Kendini aşağılayan bir anlatıcı ("a oneman fail compilation").
  - Teknik bloklar ilk denemeden **sonra** ve kısa geliyor. Terimlerde şüphe payı bırakıyor: "incremental learning. At least I think it is".
  - Nesil 17'deki tıkanma gerçek bir çözüme götürüyor: toplu öğrenme ve daha büyük popülasyon.
  - Kimliğini gizlediği ve bir avatarla tanındığı belirtiliyor (https://ntptalent.com.au/community-spotlight-interview-with-code-bullet/). Bir wiki "often wearing a black hoodie" diyor (https://en.everybodywiki.com/Code_Bullet, güvenilirliği düşük).
- **Yorum:**
  - İşlev: başarısızlık eğlencenin kaynağı ve izleyici anlatıcıdan daha zeki hissediyor.
  - Fiyat modelinde düşen bedenler yok, bu yüzden başarısızlığın **görünür kılınması** gerekiyor. Örnek: kendinden emin ama yanlış yöne giden bir tahmin, P↑ 0.51'in "kesin hüküm" gibi sunulması.
  - **Risk:** "Kapüşonlu yüzsüz kodcu" imgesi Code Bullet'la ilişkilendirilebilir. Kimliği ay kafası taşımalı.

**b2studios**
- **Kaynak:**
  - Sonuç en önde: "this Spider-Man is not human It's actually an AI… went from falling flat on its face to swinging… over a hundred kilometers an hour" → "let's go back to the beginning".
  - Anlatıcı bir kişi olarak hiç tanıtılmıyor. Sürenin büyük kısmı ön plana alınmış RL/PPO açıklaması.
  - Küçük şakalar tekniğin içine örülmüş ("about 10 of the neurons inside a jellyfish… the dumbest Spider-Man").
  - Zorluğu dürüstçe kabul ediyor ("a little too complicated for this video"). Sonuçta kesin rakamlar veriyor ("11 hours training", "topping 150 kilometers an hour").
- **Yorum:** Sonuç önde verildiği için uzun teori katlanılabilir oluyor. KAT-S için sonuç önde verilebilir, ama P↑/σ açıklaması b2'den daha küçük parçalara bölünmeli.

**Pezzza's Work**
- **Kaynak:**
  - Sakin, prosedürel bir anlatım; kişilik oyunu yok.
  - Hatalar yönlendirici: kendi fizik motorundaki bug ajanları "literally fly off" yapıyor → Box2D'ye geçiş; hız sorunu → 14 dünyaya paralelleştirme (12×).
  - Sonuç mütevazı: "This is the best result I've managed…".
  - C++ simülasyon kodları GitHub'da (https://github.com/johnBuffer).
- **Yorum:** Mühendislik yolculuğu hikâyenin omurgası olabilir: veri, eğitim süresi, neyin kırıldığı. Tek başına düz kalabilir; mizah katmanı başka yerden gelmeli.

**Michael Reeves**
- **Kaynak:**
  - Sahte "trader'ın bir günü" parodisiyle açılıyor, gerçek öncüle çöküyor ("i lost all my money on robin hood").
  - Absürt öncül: bir japon balığı hisse alıp satıyor. Aşırı mühendislikle kendini tiye alıyor.
  - Balık ile r/wallstreetbets yarışıyor: "the fish won".
  - 15:19, 13,5 milyon görüntülenme (Rosetta, https://rosetta.to/u/michaelreeves/i-gave-my-goldfish-50-000-to-trade-stocks). Görüntülenme sayısı izleyici tutma kanıtı değildir.
- **Yorum:**
  - İşlev: rastgele ya da absürt bir **karşılaştırma tabanı**, kuru bir benchmark'ı karakter çatışmasına çeviriyor. Bu aynı zamanda bilimsel olarak doğru bir hamle: yazı-tura temel çizgisi, bir olasılık iddiasının zaten ihtiyaç duyduğu şey.
  - Reeves'in sert ve provokatif kişiliği sakin bir ay karakterine uymuyor.

**Sebastian Lague**
- **Kaynak:**
  - Açıkça kurulmuş bir hedef merdiveniyle açılıyor: rakamlar → moda → karalamalar → renkli görüntüler ("if it proves too baffling… we'll have to return in the future").
  - Kavramlar kodun ihtiyaç duyduğu anda, oyuncak bir örnekten inşa ediliyor.
  - Son test "about 53%… a pretty underwhelming result" ile bitiyor. Vaat dürüstçe, kısmi başarısızlık dahil karşılanıyor.
  - Unity ve C# (https://github.com/SebLague/Neural-Network-Experiments).
- **Yorum:** Kademeli vaat ve dürüst tavan, finans içeriği için özellikle uygun. KAT-S merdiveni şöyle olabilir:
  1. Yazı-turadan iyi mi?
  2. P↑ kalibre mi (0.6 dediğinde ~%60 mı çıkıyor)?
  3. σ gerçekleşen oynaklığı izliyor mu?

**Stuff Made Here**
- **Kaynak:**
  - Sihir numarası gibi bir açılış: "It doesn't matter where I shoot on it, the ball goes in" → "This is that story".
  - İlk test başarısız ("basically always bricks my shot"). Kesin teşhis: topun yarıçapı hesaba katılmamış.
  - İddia sonda niteleniyor: "by always goes in, I mean goes in more often than it did otherwise".
  - 21:06, 9,2 milyon görüntülenme.
- **Yorum:** Finansta bu nitelemenin karşılığı: "Bitcoin'i tahmin ediyor" yerine "yazı-turadan biraz iyi ve ne zaman emin olmadığını biliyor". Kamera önünde bulunan bir bug ideal içerik olur (ör. veri sızıntısı ya da ileriye bakma hatası).

**Primer**
- **Kaynak:**
  - Şakasız, düz bir açılış ("This video is about natural selection").
  - İzleyiciyi tahmine davet ediyor ("what would you predict?"). Kendi yanılgısını hikâyenin motoru yapıyor ("This surprised me actually").
  - Kendi simülasyonları ve "trademark blob animations" (https://github.com/Primer-Learning/PrimerTools, https://lironshapira.substack.com/p/justin-helps-primer-on-youtube-is).
- **Yorum:** Ürün zaten bir tahmin olduğu için "durdur, P↑'yi göster, izleyiciye 'bu bahse girer miydin?' diye sor, sonra aç" yapısı doğal. Primer'ın sakinliği ay karakterine Code Bullet'ın maniklik hâlinden daha yakın.

**İzleyici tutma verisi:** Yedi üreticinin hiçbiri için bulunamadı.

### 2.3 Türkçe örnekler
| Üretici ve video | Seçilme nedeni |
|---|---|
| **Tolga Özuygur** (@hallederiz) — "YouTube Rapçisi Yapımı / E-Bliss: Yapay Zekalı Rap Robotu" (https://www.youtube.com/watch?v=-jsWYKo2PPc; 14:46; 31 Ocak 2021) | Krafer'la aynı yapı: komik bir "yapay zekâ yaptım" projesi (Türkçe trap sözleriyle GPT-2), Türkçe ve prodüksiyonu güçlü |
| **Kerem Mert İzmir** (kker4m) — "Yapay Zeka ile Video Düzenlemeyi Nasıl Otomatikleştirdim" (https://www.youtube.com/watch?v=x-H41Clv05A) | Türkçe, düşük cilalı, ekran kaydına dayalı geliştirici günlüğü; kimlik GitHub üzerinden doğrulandı (https://github.com/kker4m/ai_video_editor) |
| **Barış Özcan** — "Yapay zeka dünyasındaki en büyük sıçrama gerçekleşti! GPT-3 nedir?" (https://www.youtube.com/watch?v=r2dQgdktUJg; 16:34) + Bitcoin metni (https://barisozcan.com/bitcoin-insanlik-tarihinin-en-onemli-icadi-olabilir-mi/) | Sakin, benzetmeli Türkçe açıklama; Bitcoin'e ve yatırım tavsiyesi uyarısına bakışı |
| **Sarp Sagir** — "Herkes Zarardayken Yapay Zeka BIST'e Nasıl Fark Attı?" (https://www.youtube.com/watch?v=xhNY0f8Oe5Q) | **Karşı örnek:** Türkçe "yapay zekâ piyasayı yendi" söylemi |

**Tolga Özuygur**
- **Kaynak:**
  - Öncül, kendini tiye alarak kuruluyor: "Ben de her youtuber gibi bir rap parçası yapmak istedim ama benim bu konuda hiçbir yeteneğim yok." Vaat: "YouTube [rapçisinin] kendisini yapmaya karar verdim."
  - Robot bir karakter: "kendisi artık benim bir evladım"; adı "İblis" kelime oyunu.
  - Absürt bir söz dizesini ("Fiberim ıslak") gerçek bir teknik bilgiyle savunuyor: deniz altı fiber kabloları.
  - Teknik terimler (GPT-2, Arduino) korunuyor, eğitim sade Türkçeyle anlatılıyor ("cümlelerin yapısı ve bunlar arasındaki ilişki").
  - Vaat karşılanıyor: parça yayınlandı, kod açık (github.com/cemkod/e-bliss-rapgen).
  - Açıklamada ayrı bir kurgucu ve ekip isimleri var.
- **Yorum:**
  - Yaratılan şeyi bir **karakter** yapmak (robot = evlat), KAT-S'i ay karakterinin "huysuz tahmin çocuğu" gibi kurmaya uygun bir Türkçe örnek.
  - Absürdü gerçek teknik bilgiyle savunmak Türkçede işleyen bir mizah biçimi.
  - Açılış görüntüsü doğrulanmadı.

**Kerem Mert İzmir (kker4m)**
- **Kaynak:**
  - Standart selamlama ("Merhaba Arkadaşlar…"), sonra kendi sorunu (çok "arkadaşlar" diyor, jump cut'larla uğraşıyor), izleyici talebi ve vaat: "videolarımı editleyen bir Yapay Zeka yapacağım".
  - Neredeyse tüm terimler İngilizce ve Türkçe yazımla: "jump cut", "repository", "commit", "prompt", "token", "pars etmeliyiz", "generate edildi".
  - Tek bir kavram (virtual environment) ekranda çizilen bir daireyle açıklanıyor.
  - Sonuç dürüst bir anti-klimaks: 37 sn → 26 sn, tekrarlar silinmedi, "Bizimkinden de bir farkı yok bence", API maliyeti ~0,01 $.
- **Yorum:**
  - Dürüst ve kısmen başarısız bir sonuç, açıkça söylendiğinde Türkçe geliştirici izleyicide sorun yaratmıyor gibi görünüyor. İzleyici verisi yok; bu yalnızca bir işlev yorumu.
  - Düşük yapılandırmanın tavanı da görülüyor.

**Barış Özcan**
- **Kaynak:**
  - GPT-3 videosu cilalı bir girişle açılıyor, ardından ters köşe geliyor: "Bu minik girişin senaryosunu ben yazmadım…" (metni GPT-3 yazmış).
  - Bitcoin metni iddiayı baştan niteliyor ("…olabilir. Olmayabilir de…") ve hemen uyarıyor: "Anlatacaklarım bir yatırım tavsiyesi olmayacak". Fiyatı tarihle damgalıyor.
  - Benzetmeler: parametreler "175 milyar farklı ayar düğmesi", blockchain "bakkal defteri".
  - Bitcoin videosu açıklamasında "Canon C200 ile 4K çekilmiştir"; metin ve kaynaklar kendi sitesinde yayınlanmış.
- **Yorum:**
  - "Yöntemin kendisini açılışta ters köşe yapmak", model tahmini için uyarlanabilir: izleyiciye bir grafik gösterip sonra "bunu ben değil, model çizdi" demek.
  - Uyarının baştan ve içtenlikle verilmesi finans içeriğine uygun.

**Sarp Sagir (karşı örnek)**
- **Kaynak:**
  - Açıklamada "%27 fark" vaadi, tekrarlanan affiliate indirim linkleri.
  - Uyarı video ortasında geçiştiriliyor: "hiçbiri tabii ki yatırım tavsiyesi değildir arkadaşlar".
- **Yorum:** KAT-S'in **benzememesi gereken** söylem. Getiri rakamıyla başlık, affiliate link ve formül hâline gelmiş bir uyarı cümlesi.

### 2.4 Türkçe terminoloji, hitap ve düzenleyici bağlam
**Terminoloji önerisi.** Kaynaklardaki örüntü şu: araç ve süreç terimleri İngilizce kalıyor, ilk geçişte Türkçe açıklanıyor.

| Kavram | Öneri | Dayanak |
|---|---|---|
| candle | "mum" ("1 dakikalık mum"); "candlestick" bir kez | coinmuhendisi.com "mum verileri"; github.com/huseyinoymak/Merdiven |
| prediction | "tahmin"; "kehanet" yalnızca şaka için | Türkçe fiyat tahmini yazıları |
| P↑ | "yükselme olasılığı" + ekranda "P↑" | — |
| σ | "oynaklık" (anlatım), "volatilite" de anlaşılır; "sigma" bir kez | kriptohayat, xloji |
| backtest | "geriye dönük test (backtest)" | kriptohayat, aitr.blog |
| model / AI | KAT-S için "model", tür için "yapay zekâ" | — |
| neural network | "sinir ağı" + tek satırlık benzetme | Barış Özcan'ın "ayar düğmesi" benzetmesi |
| kaçınılacak | "sinyal", "al/sat" (tavsiye çağrışımı) | aşağıdaki düzenleyici bağlam |

**Hitap:** Üç üretici de "siz" ve "arkadaşlar" kullanıyor. "Sen" hitabı daha yayıncı ve genç kuşak tonunda okunur. Anlatıcı kararıyla birlikte seçilmeli.

**Düzenleyici bağlam** (ikincil kaynaklardan; SPK birincil metni bu araştırmada okunmadı):
- Türk hukukçulara göre "yatırım tavsiyesi değildir" cümlesi tek başına koruma sağlamıyor. Belirleyici olan içeriğin gerçekte ne yaptığı:
  - kişiye özel olup olmadığı,
  - süreklilik taşıyıp taşımadığı,
  - ücretli olup olmadığı,
  - somut al/sat yönlendirmesi içerip içermediği.
- Kaynaklar:
  - https://pegahukuk.com/kripto-yatirim-tavsiyesi-vermek-suc-mu-spk-duzenlemeleri/
  - https://www.btchaber.com/yatirim-tavsiyesi-veren-kripto-fenomenleri-suc-mu-isliyor/
  - https://defihukuk.com/kripto-pazarlama-hukuku/
  - https://www.sondakika.com/haber/haber-kripto-fenomenleri-icin-geri-sayim-basladi-20257775/ (Eylül 2026)
- Genel, kişiye özel olmayan eğitim ve analiz "tek başına suç değildir".
- **Üretim çıkarımı:**
  - Video bir deney ve eğitim olarak çerçevelenmeli.
  - Al/sat çağrısı, sinyal grubu, borsa affiliate linki olmamalı.
  - Uyarı erken ve içtenlikle söylenmeli, ama asıl koruma içeriğin kendisinin tavsiye niteliği taşımaması.
  - Sonuçlar tarihle damgalanmalı.
  - Hukuki değerlendirme bu araştırmanın kapsamı dışında.
- Türkçe izleyicinin "yapay zekâ ile zengin ol" içeriğine doymuş olduğu yorumu bir blog yazısına dayanıyor (https://aitr.blog/blog/ai-ile-borsa-trading-bot-gercek-mi/). Bu bir eğilim tespiti değil, bir yorumdur.

**Doğrulanamayanlar:**
- Tüm görüntü ve ses.
- kker4m videosunun tarihi ve süresi.
- Barış Özcan Bitcoin videosunun YouTube bağlantısı.
- Tolga'nın açılış sahnesinin görüntüsü.

### 2.5 Karşılaştırmanın gösterdiği olanaklar
Aynı "yapay zekâya bir şey öğrettim" konusu şu yollarla anlatılabiliyor:

| Deneyim | Motor | Anlatıcı | Mizah | Risk |
|---|---|---|---|---|
| **Komedi yolculuğu** (Krafer, Code Bullet) | Başarısızlık → dönüş | Alaycı, kendini tiye alan | Tepki, absürt benzetme, tür şakası | Kanıt ikinci plana düşer ("not far off") |
| **Önce sonuç** (b2studios, Stuff Made Here) | "Nasıl oldu?" merakı | Yetkin, alçakgönüllü | Kuru, yer yer | Açılış sonucu gerçekten elde olmalı |
| **Mühendislik günlüğü** (Pezzza) | Sorun → çözüm zinciri | Neredeyse görünmez | Çok az | Duygusal düzlük |
| **Absürt karşılaştırma** (Reeves) | Rakip ile çatışma | Kaotik karakter | Öncülün kendisi | Finansta taklit edilme riski |
| **Merak ve dürüst tavan** (Lague, Primer) | Hedef merdiveni, izleyici tahmini | Sakin öğretmen, yanılabilen | Yumuşak, sözel | Yavaşlık |

**KAT-S'e özgü tespit:**
- KAT-S'in ürünü **olasılık** (P↑) ve **belirsizlik** (σ).
- Bu, "önce sonuç" yapısını tek başına yetersiz kılıyor: bir güzel örnek hiçbir şey kanıtlamaz.
- "İzleyici tahmini" ve "dürüst tavan" yapılarını ise ürünün doğasına bağlıyor.

---

## 3. Avatar

### 3.1 Elde olanlar (dört farklı görsel; biri iki kez gönderildi)
Dosyalar `research/avatar/` altında; hepsi 1254×1254 px webp, **şeffaflık yok** (arka plan görüntüye gömülü).

| Dosya | Görünüş |
|---|---|
| `avatar_A_profil_siyah-cerceve.webp` | Dairesel kırpım, siyah zemin. Figür 3/4 profilde sağa bakıyor. Siyah kapüşonlu üst, kapüşon boyuna yığılmış, iki ip. Baş yerine krem-sarı parlayan **hilal**. Hilalin iç (içbükey) tarafı sağa açık, sol-alt kenarında lavanta bir kalınlık ("dilim" hissi). Yumuşak, boyalı anime ışığı; hilalde dış çizgi yok. |
| `avatar_B_profil_mavi-halka.webp` | A ile aynı poz; lacivert zemin, **mavi neon halka**, kapüşon kenarlarında mavi ışık. |
| `avatar_C_profil_mor-halka.webp` | A ile aynı poz; koyu mor zemin, **mor neon halka**, kapüşonda mor kenar ışığı. |
| `avatar_D_onden_mor-kapusonlu.webp` | **Farklı poz ve stil:** önden, omuzlar dahil yarım bel. **Mor kapüşonlu**, metal uçlu ipler. Hilal kalın **siyah dış çizgili**; daha düz, cel-shading bir stil. Boyun kısmı karanlık bir boşluk. Gradyanlı lacivert-mor zemin, kare kadraj. |

**Tutarlılık notu:** A/B/C ile D aynı karakter ama **iki farklı çizim stili**. A/B/C'de çizgi yok ve yumuşak ışık var; D'de kalın kontur ve düz renk var. Kapüşon rengi de farklı (siyah ↔ mor). Videoda tek bir stil seçilmeli, ya da stil farkı bilinçli bir anlam taşımalı (bkz. §3.3).

### 3.2 İfade olanakları (tek görselden türetilmedi; mevcut olanla ne yapılabileceği)
- **Yüz yok.** Bu yüzden ifade şu kanallardan gelebilir:
  1. **Işık:** hilalin parlaklığı, titreşimi, rengi (krem → soğuk mavi → sönük).
  2. **Evre:** hilal inceliyor ya da kalınlaşıyor, dolunaya ya da yeni aya dönüyor.
  3. **Baş eğimi ve dönüşü:** yalnızca 2D döndürme; profil ve önden görünüm zaten mevcut.
  4. **Beden dili:** yeni pozlar gerektirir; eller hiçbir görselde yok.
  5. **Çevre:** halka rengi, zemin ışığı.
- **Anlam katmanları (yorum; kültürel çağrışımlar):**
  - **"To the moon"** kripto argosu: fiyatın "aya gitmesi". Anlatıcının kendisi ay; abartılı iyimserliğe karşı ironik bir konum alabilir.
  - **Ay evresi ↔ güven:** Klipteki P↑ değerleri 0.43–0.54 arasında. Ay "dolunaya" hiç ulaşamıyor, yani model hiçbir zaman emin değil. Bu, ürünün gerçek verisinden çıkan, **karaktere özgü** bir görsel fikir.
  - **Gece ve 7/24 piyasa:** Kripto piyasası hiç kapanmaz; ay, herkes uyurken grafiği izleyen nöbetçi.
  - **Gelgit:** Ay suyu çeker. Fiyat dalgalarıyla bir metafor kurulabilir ama bilimsel olarak yanıltıcı bir çağrışım; dikkatli kullanılmalı.
  - **Türk izleyici için hilal:** Hilal, bayraktaki sembol nedeniyle ulusal bir çağrışım taşır. Bayraktaki hilal de içbükey tarafı sağa açık bir kompozisyonda. Bu hem tanınırlık fırsatı hem de istenmeyen okuma riski (siyasi/ulusal sembol). Karar kullanıcının; renk ve yıldız yokluğu bu okumayı zayıflatır.
  - **"Ay" kelimesi** hem gök cismi hem takvim ayı; kelime oyunu olanağı var.

### 3.3 Anlatıcı rolleri (alternatifler; henüz karar değil)
1. **Anlatıcı = kanal sahibinin kendisi.** Avatar bir maske; "ben" dili, deneyi yapan kişi. Krafer/Code Bullet'a yakın bir ilişki.
2. **Anlatıcı = modelin kişileştirilmiş hâli.** Ay, tahmini "gören" varlık; kanal sahibi başka bir ses. Diyalog ve çatışma kurulabilir.
3. **Anlatıcı = gözlemci ve eleştirmen.** Kendi modelini sorgulayan, hype'a mesafeli, sakin bir ses (Lague/Primer'a yakın). Ay "gecenin tanığı".
4. **Karma:** anlatıcı insan (avatar), ama grafikteki "ay evresi göstergesi" modelin güvenini temsil ediyor. Avatar ve veri görselleştirmesi aynı sembolü paylaşıyor.

**Stil farkının bilinçli kullanımı (öneri):** Yumuşak ışıklı profil (A/B/C) "gece, düşünme, anlatım" sahnelerinde; çizgili önden görünüm (D) "doğrudan hitap ve tepki" anlarında kullanılabilir. Bunun işe yarayıp yaramayacağı ancak bir test montajıyla anlaşılır.

### 3.4 Teknik görüntülerle ilişki
- **Avatarın sürekli ekranda olması gerekmiyor.** Metne göre Krafer'da da anlatıcı sesle var; görsel varlığı doğrulanmadı.
- Olası kullanımlar:
  - Grafiği işaret eden küçük bir köşe figürü.
  - Tahmin anında tam ekran tepki kartı.
  - Bölüm geçişlerinde siluet.
  - Hilalin kendisini **grafik elemanı** olarak kullanmak (ör. ay ışığının tahmin bölgesini aydınlatması). Bu son seçenek avatara en özgü olanı.
- **Renk uyumu:**
  - KAT-S klibindeki tahmin rengi camgöbeği/amber, gerçek gri, arka plan #030407.
  - Avatarın kremi tahmin amberiyle, lacivert/mor zemini klibin koyu zeminiyle doğal olarak uyumlu.
  - **Karar:** Hilal kremi = tahmin rengi mi olacak? Olursa "ayın ışığı = tahmin" metaforu görsel olarak kendiliğinden kuruluyor.

### 3.5 Gerekebilecek ek varlıklar (mevcut değil)
- **Temel:**
  - Şeffaf arka planlı (PNG/alpha) kesimler.
  - **Hilal ile beden ayrı katmanlarda** (ışık ve evre animasyonu için).
- **Ek pozlar:**
  - Yana dönük tam profil.
  - Başı eğik ("düşünüyor", "utanç").
  - Eller görünür (işaret etme, masada klavye).
  - Arkadan (ekrana bakarken).
- **Ay evreleri:** Yeni ay, ince hilal, yarım, şişkin, dolunay (güven göstergesi için 5–9 kare).
- **Tek stil kararı:** Konturlu mu, konturlu değil mi? Siyah kapüşonlu mu, mor mu?
- **Yüksek çözünürlük:** 1254 px tam ekran 1080p için sınırda; 4K için yetersiz.
- **Animasyon yöntemi:** Karar verilmedi. Seçenekler:
  - 2D kukla (After Effects / Live2D / Blender grease pencil).
  - Yalnızca ışık ve evre animasyonu, bedeni sabit tutmak (en az varlıkla en çok ifade).

---

## 4. Kullanıcının elindeki malzeme ve durumu

| Malzeme | Durum | Not |
|---|---|---|
| KAT-S klibi (21 sn, 1080p60, sessiz) | ✅ Var | 8 örnek. 01/08 (08:02) tahmin gerçekle neredeyse örtüşüyor; 08/08 (13:46) tahmin yükseliş, gerçek önce sert düşüş (aynı konuşmada kare kare incelendi) |
| Klipten 60 sn'lik deneme kurgusu | ✅ Var (`video/kat-s_intro_60s.mp4`) | Aşağıdaki §4.1'e bakın |
| Avatar | ✅ 4 görsel, 2 poz, 2 stil | §3.5'teki eksikler |
| **Geriye dönük test sonuçları** (yön isabeti, basit yöntemle kıyas, kalibrasyon) | ❌ Yok | Videonun esas karşılığı buna bağlı. **Henüz yapılmamış bir deneyin sonucu gerçek kanıt gibi kullanılmamalı.** |
| Model ayrıntıları (girdi, mimari, eğitim verisi, test aralığı) | ❌ Bilinmiyor | "Model neye bakıyor?" bölümü için gerekli |
| Klipteki 20 Haziran 2026 verisinin **test verisi** olup olmadığı | ❌ Bilinmiyor | "Modelin hiç görmediği veri" iddiası buna bağlı |
| P↑ ve σ'nın kesin tanımı | ⚠️ Yorumlandı, doğrulanmadı | P↑ h50: "50 bar sonra yukarıda olma olasılığı"; σ: "beklenen oynaklık" |
| KAT adı ile Krafer KAT™ ilişkisi | ❌ Açıklanmadı | §0.3 |
| Kullanıcının sesi, müzik, SFX | ❌ Yok | — |

### 4.1 Önceki 60 sn denemesinin bu araştırmaya göre değerlendirmesi
- **Sağlam bulduklarım:**
  - Iskayı ilk 20 sn'de göstermesi (Stuff Made Here ve Lague'deki dürüst niteleme işlevi).
  - Tek bir renk dilinin öğretilmesi.
  - Yol haritası kartıyla bir hedef merdiveni kurması (Lague).
- **Sorunlu olanlar:**
  1. **Maskeleme açılışı** (tahmin bölgesinin kapatılması), Krafer'ın merkezi metaforuyla ("cover up the right side") aynı. Genel bir fikir, ama doğrudan referansla yan yana görülecek. Farklı bir görsel yorum gerekebilir.
  2. **Anlatıcı kimliği yok.** Avatar kullanılmıyor; video sakin bir veri sunumu gibi.
  3. **"Model bu 50 mumu hiç görmeden çizdi"** ifadesi, test ayrımı doğrulanmadan yazıldı. Veri eğitim setindeyse yanıltıcı.
  4. **"Yüzlerce örnekte isabet oranı"** vaadi yol haritasında var, ama bu deney henüz yapılmadı.
  5. **KAT adı sorunu** (§0.3) çözülmeden başlık kartı "KAT-S 1.0" diyor.

---

## 5. Özgünlük: işlev ↔ Krafer'ın uygulaması ↔ KAT-S için farklı uygulama

| İşlev | Krafer'ın uygulaması (kaynak) | KAT-S için farklı olanaklar (öneri) |
|---|---|---|
| Klişe soruyu kanca yapmak | İroni: "no one has asked before" | Soruyu **izleyiciye** sormak (Primer): "Bu grafiğe bak — sen olsan ne derdin?" Ya da hype'ı karşıya almak: "Herkes aya gideceğini söylüyor. Ben aya sordum." |
| Seri bağlamı ve tez | Önceki simülasyon videosu | KAT-S için bir öncül yok. Onun yerine **kişisel motivasyon** ya da **somut bir an** (ör. klipteki 13:46 ıskası) kullanılabilir. |
| Başarısızlıktan komedi ve dönüm | Kayıplarını saklayan botlar | KAT-S'in gerçek başarısızlıkları: 13:46 ıskası, P↑'nin 0.5 civarına sıkışması. Varsa sızıntı ya da ileriye bakma hatası. **Uydurma değil, gerçek olan kullanılmalı.** |
| Önce sonuç, sonra açıklama | "So what's going on here? The KAT 1.3…" | Aynı işlev; ama sonuç tek bir örnek değil, **kalibrasyon** gibi dağılım bilgisi olabilir. |
| Kanıt anı | Dondurulmuş kareler: "not far off" | **Sayısal karşılık:** yazı-tura tabanı, naive tahmin, kalibrasyon. Krafer'ın bıraktığı boşluk. |
| Teknik yükü mizahla taşımak | Absürt benzetmeler (havuç, poker, Plinko) | Türkçe ve yerel benzetmeler, ya da **ay ile ilgili** benzetmeler. Örnek: "Ay'ın yalnızca bir kısmını görürüz; model de geleceğin yalnızca bir olasılığını görür." |
| Anlatıcı kişiliği | Alaycı, kendini tiye alan, hızlı | Ay karakterine uygun seçenekler: sakin-kuru, "nöbetçi", ya da kendi modelinden şüphe eden dürüst bir ses. Türkçe konuşma dilinin ritmi, İngilizce kafiye ve tür şakalarının çevirisiyle kurulamaz. |
| Kapanış ve ürün | Abonelikli site, başka kanal | Yatırım tavsiyesi uyarısı, açık belirsizlik, "KAT-S 2.0'da ne değişecek" |

**Kaçınılması gerekenler (brief'e göre):**
- Krafer'ın şakalarını Türkçeye çevirmek: Tino, Powell kafiyesi, "I hate Python", "videos don't grow on trees".
- "Hypothetically" montajının aynısı.
- "cover up the right side" metaforunun aynı biçimde kullanılması.
- Model adının KAT olarak kalması (§0.3).

---

## 6. Karar tablosu

### 6.1 Şimdi verilebilecek kararlar (bulgulara dayanarak)
1. **Kanıtın biçimi:** Tek bir örnek değil, ölçülebilir bir karşılaştırma: yazı-tura, "fiyat değişmez" tahmini, P↑ kalibrasyonu. *Gerekçe:* Krafer'ın bıraktığı boşluk; Lague/Stuff Made Here'deki dürüst niteleme; finansal içerikte güvenilirlik.
2. **Başarısızlığın rolü:** Gerçek ıskalar anlatının motoru olmalı; 13:46 örneği hazır. *Gerekçe:* Krafer'da en işlevsel an "cheating"; Code Bullet ve Stuff Made Here.
3. **Avatarın ayırt edici öğesi:** Hilal ışığı ve evresi. Kapüşon ikincil. *Gerekçe:* Code Bullet ile karışma riski; ay evresinin P↑ ile birleşme olanağı.
4. **Yatırım tavsiyesi olmadığı açıkça belirtilmeli.**

### 6.2 Kullanıcının vermesi gereken yaratıcı kararlar (alternatifler §3.3 ve §2.5'te)
- **Anlatıcının kim olduğu:** kanal sahibi, model ya da gözlemci.
- **Mizahın ağırlığı:**
  - Komedi motoru mu?
  - Kuru, yer yer mi?
  - Yalnızca başarısızlıktan doğan mı?
- **Açılışın biçimi:**
  - önce sonuç;
  - izleyiciye soru;
  - ıskadan başlamak;
  - hype'a karşı ironi.
- **Avatarın tek stili:** A/B/C (yumuşak) mı, D (konturlu) mu?

### 6.3 Hâlâ bilgi gereken konular
1. KAT-S ↔ Krafer KAT™ ilişkisi ve ad kararı (**engelleyici**).
2. Model ayrıntıları ve test ayrımı; klipteki verinin eğitimde kullanılıp kullanılmadığı.
3. P↑ ve σ tanımlarının doğrulanması.
4. Geriye dönük test: kaç örnek, hangi tarih aralığı, hangi ölçütler.
5. Krafer videosunun görsel doğrulaması (§1.7): kurgu ritmi, avatar kullanımı ve müzik hakkında şu an hiçbir gözlem yok.
6. Anlatıcı sesi: kullanıcının kendi sesi mi, TTS mi?
7. Türkçe terminoloji ve hitap tercihi (öneri §2.4'te).

---

## 7. İlk dakikanın üretimine geçmek için dayanak yeterli mi?

**Kısmen.**

- **Yeterli olanlar:**
  - Anlatı ve özgünlük çerçevesi.
  - Gerçek görüntü malzemesi: KAT-S klibi (isabet ve ıska örnekleri).
  - Avatarın temel görselleri.
  - Renk uyumu.
  - Karşılaştırmadan türetilmiş yapı seçenekleri.
- **Eksik olan ve ilk dakikayı doğrudan etkileyenler:**
  1. **Ad kararı** (KAT-S). Başlık kartı ve seslendirme buna bağlı.
  2. **Anlatıcı kararı** ve bu karara uygun **avatar varlıkları**: şeffaf kesim, ayrı hilal katmanı, en az 2–3 ek poz ya da evre.
  3. **Kanıt vaadi:** İlk dakikada "yüzlerce örnekle test edeceğiz" denecekse bu testin yapılabilir olduğundan emin olunmalı. Mümkünse sonuç önceden bilinmeli, ama ilk dakikada ifşa edilmemeli.
  4. Klipteki verinin test verisi olduğunun doğrulanması; "hiç görmeden" ifadesi buna bağlı.
- **Üretilebilir olan (eksikler giderilmeden bile):** Yalnızca **gerçek klip görüntüleri**, dürüst ve nitelenmiş bir anlatım ve **ışık ya da evre animasyonlu tek bir avatar pozu** ile bir ilk dakika taslağı. Kanıt iddiası içermemeli; soruyu ve yöntemi vaat etmeli.

---

## Kaynaklar
- Krafer, "I made an AI learn Stock Market Patterns": https://www.youtube.com/watch?v=0yNfaixWyf4
  - Başlık ve kanal: YouTube oEmbed.
  - Transkript: Exa ile, `kaynaklar/krafer_0yNfaixWyf4_transkript.txt`.
  - Tarih ve açıklama: https://socialcounts.org/youtube-video-analytics/0yNfaixWyf4
- Krafer, "I made a Market Simulation to see if Patterns are Real": https://www.youtube.com/watch?v=oWheof70O9g
- Krafer Crypto, "Using My KAT Models on Real Markets": https://www.youtube.com/watch?v=A9SuiU2vvuE
- KAT™ — Krafer Agent Trader: https://krafercrypto.com, https://krafercrypto.com/kat, https://krafercrypto.com/youtube, https://krafercrypto.com/change-log
- Patreon, "KAT (Krafer Agent Trader) - Market Simulation" (21 Nisan 2025): https://www.patreon.com/kraferc/posts/kat-krafer-agent-127154850
- Karşılaştırma videoları ve ek kaynaklar: §2.1–§2.2 içindeki bağlantılar
