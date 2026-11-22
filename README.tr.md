# Anti-Slop Design Skills v3.0 — Türkçe Rehber

![Tasarım galerisi](gallery/cover.png)

**82 skill, 42 görsel stil, 20 sektörel site yapısı, 14 renk paleti, 5 sosyal medya tasarımı ve 1 Tasarım Direktörü.**

Geleneksel grafik tasarımdan farklı sektörlerin gerçek web sitesi ihtiyaçlarına uzanan, **görselliği olan** bir Agent Skills kütüphanesi. Klişe yapay zekâ arayüzlerinden kurtulmanın yolu yalnızca rengi değiştirmek değil; her projeye **uygun mimari + estetik + kullanıcı yolculuğu** seçmek.

- [Tüm skill'leri filtreli galeride gör](gallery/index.html) (HTML'yi yerel tarayıcıda aç)
- [42 görsel stilin tek sayfalık görseli](gallery/contact-sheet.jpg)
- [Sektörlere göre hazır kombinasyon örnekleri](examples/industry-recipes.md)

Her skill klasöründe: `SKILL.md`, `preview.png`, `demo.html` var. Görseller gerçek tarayıcıda render edilmiş özgün statik demoların ekran görüntüleridir; çalışan rezervasyon sistemi, üretime hazır site veya yayımlanmış ürün oldukları iddia edilmez.

## Skill türleri

| Katman | Adet | İşlev |
|---|---:|---|
| Görsel stil | 42 | Tasarım karakteri ve tarihsel esin |
| Sektörel site yerleşimi | 20 | Restoran, otel, emlak, hukuk, etkinlik ve daha fazlası |
| Renk paleti | 14 | Uyumlu ortak token sistemi |
| Sosyal medya | 5 | Kampanya / duyuru düzeni |
| Tasarım Direktörü | 1 | Doğru seçim, uyumluluk ve eleştiri kontrolü |

## Kurulum

```bash
python tools/install.py --list
python tools/install.py --skill design-director --skill legal-practice --skill swiss-editorial --target /projem/.agents/skills
```

**Gemini CLI:** `.gemini/skills/` · **Claude Code:** `.claude/skills/` · **uyumlu ajanlar:** `.agents/skills/`. Ajanın güncel kurulum kurallarını kontrol edin.

Örnek komut:

```text
Önce design-director skill'ini uygula. Bir hukuk bürosu web sitesi için
legal-practice + swiss-editorial + oxblood-parchment kullan.
Gerçek kullanıcı akışını, mobil önceliği, klavye erişilebilirliğini ve
boş/yükleniyor/hata durumlarını tasarla. Klişe yapay zekâ arayüzünü ve
uydurma müşteri yorumlarını kullanma. Kodunu üret, kararı açıkla.
```

## GitHub'a yükleme

ZIP'i çıkart, klasörün **içindeki** tüm dosyaları yeni bir repoya yükle. README görselleri GitHub içinde gösterir. `gallery/index.html` çevrimdışı gezilebilir. İstersen statik galeriyi GitHub Pages üzerinden yayımlayabilirsin (repo kökünde `index.html` yönlendirmesi bulunur).

**Kaynak yaklaşımı:** SITE123'ün sektörel örnek çeşitliliğinden kategoriler için fikir alınmıştır, hazır SITE123 şablonları veya müşteri görselleri kopyalanmamıştır. Çalışma özgün statik HTML/SVG demolarına ve tarihsel tasarım prensiplerine dayanır. MIT lisanslıdır.
