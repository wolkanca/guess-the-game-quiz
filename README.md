# 🎮 Hangi Oyun Bu? – Wolkanca Oyunları #06

**3 simge, 1 video oyunu!** Görsel ipuçlarını açıp hangi oyun olduğunu tahmin et. Az ipucuyla bilmek daha çok puan kazandırır.

Bu oyun, Wolkanca Oyunları serisinin altıncı numaralı mini oyunudur. Serideki #05 daha sonra hazırlanabilir. `ai-or-real-quiz`, `zoom-object-quiz`, `turkiye-sehir-quiz` ve `real-or-fake-news-quiz` projelerinin bağımsız, mobil uyumlu HTML/CSS/JS yaklaşımını sürdürür.

## Özellikler

- **37 video oyunu** içeren soru havuzu. Her turda **10 rastgele soru**: 4 kolay, 4 orta, 2 zor.
- **4 seçenekli oyun tahmini.** İlk simge açık; sıradaki iki simgeyi veya yazılı ipucunu açabilirsin.
- **İpucu maliyeti:** Tek simgeyle 200, iki simgeyle 140, üç simgeyle 90, metin ipucuyla 60 temel puan. Doğru cevaplarda art arda seri bonusu (+20, +40, +60) kazanılabilir.
- İsteğe bağlı **25 saniyelik süreli mod**. Zaman dolunca soru yanlış sayılır.
- Her cevap sonrasında oyun adı, türü ve kısa tanıtım.
- `localStorage` ile kişisel rekor; tekrar oynama ve sonuç paylaşma.
- Klavye kısayolları: `1`, `2`, `3`, `4` cevap seçer; `i` yeni simge açar.
- Tamamen tarayıcıda çalışır. Haricî JavaScript kütüphanesi, API anahtarı veya sunucu gerekmez.
- Oyun ekran görüntüleri, logoları, markalara ait karakter görselleri **kullanılmaz**. Simgeler genel emoji temsilleridir; oyun adları yalnızca tanımlama amaçlıdır.

## Hemen çalıştır

`index.html` dosyasını tarayıcıda açman yeterli. İstersen yerel bir sunucuda çalıştır:

```bash
python3 -m http.server 8000
```

Tarayıcıdan `http://localhost:8000` adresine git.

## GitHub’a yükle

Önerilen public repo adı: **`wolkanca/guess-the-game-quiz`**.

1. Bu depoda oyun dosyalarının `main` dalında olduğunu kontrol et.
2. **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save** seç.
3. GitHub Pages yayınlandığında beklenen adres: **`https://wolkanca.github.io/guess-the-game-quiz/`**. GitHub Pages bu depoda henüz etkinleştirilmiş olmayabilir; yayınlanana dek adresin çalıştığı iddia edilmez.
4. WordPress blog yazısına `wordpress-embed.html` kodunu **Özel HTML** bloğundan ekle.

> SEO: GitHub Pages’deki HTML dosyasında `noindex,follow` vardır. Organik trafik için hedef sayfanın Wolkanca.com’daki blog yazısı olması amaçlanır. GitHub Pages sürümünü ayrıca indeksletmek istiyorsan metayı değiştir.

## Yeni oyun ekleme

`games.json` düzenlenebilir veri kaynağıdır. Her soru:

```json
{
  "id": "ornek-oyun",
  "name": "Örnek Oyun",
  "difficulty": "orta",
  "icons": ["🎮", "⭐", "🕹️"],
  "genre": "Macera",
  "hint": "Oyunu anlatan kısa ipucu.",
  "fact": "Cevap sonrası gösterilen bilgi.",
  "distractors": ["Alternatif A", "Alternatif B", "Alternatif C"]
}
```

- `difficulty`: `kolay`, `orta`, `zor` olabilir.
- Her soruda tam **3 simge** ve **3 benzersiz yanlış seçenek** olmalı.
- Oyunun adı yanlış seçeneklerden birisi olamaz.
- Veriyi düzenledikten sonra `python3 build.py` komutunu çalıştır; bu betik `index.template.html` ile `games.json` dosyalarını birleştirerek yayına hazır `index.html` üretir.

## Test

Oyunu `index.html` üzerinden açıp soru, ipucu, zamanlayıcı, skor ve sonuç ekranını deneyebilirsin.

İlk sürüm, 1280 px masaüstü ve 390/320 px mobil genişliklerde 10 soruluk tur, ipucu, sonuç ve tekrar oynama akışlarıyla test edilmiştir.

## Kaynak ve telif notu

Bu bağımsız oyun resmi oyun şirketleriyle bağlantılı değildir. Oyun adları ve türleri açıklama/tanımlama amacıyla kullanılır. Görsel ipuçları ilgili oyunların resmî görselleri değildir. Yanlış olabilecek tarihî ayrıntılar için kaynak doğrulaması yaparak yeni soruları genişlet.

Bazı tarih bilgileri için örnek doğrulama bağlantıları:

- [Minecraft – oyunun çıkış tarihi hakkında](https://www.minecraft.net/en-us/about-minecraft) (ilk sürüm 2009, tam sürüm 2011).
- [Stardew Valley – resmî basın sayfası](https://www.stardewvalley.net/press/) (2016).
- [Portal – Steam](https://store.steampowered.com/app/400/Portal/) (2007).
- [Celeste – Steam](https://store.steampowered.com/app/504230/Celeste/) (2018).