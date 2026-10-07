# Asansör Müzakere Protokolü

> Resmi ad: **KTM-08 / Kat Tercihi Müzakere Yönetmeliği**
> Gayriresmi ad: düğmeye basıp pişman olanlar için belediye

Bu depo, bir asansörün hangi kata gideceğine karar vermeyi **aşırı ciddi** bir kamu müzakere sürecine çevirir. Kod çalışır. Asansör çalışmaz. Bu bir hata değil, vizyondur.

## Neden var?

Çünkü birisi düğmeye bastı. Bastığı için sorumluluk doğdu. Sorumluluk doğunca komisyon kuruldu. Komisyon kurulunca tutanak tutuldu. Tutanak tutulunca kat seçimi **ertelendi**.

Bilim bunu “yerçekimi” der. Biz “gündem maddesi 4” deriz.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Asansör kablosu da yoktur. Bu da vizyondur.

```bash
python3 protokol.py
python3 protokol.py --kat 7 --ciddiyet 94
python3 protokol.py --kat 0 --acil
```

## Ne yapar?

1. İstediğin katı dinler.
2. Katı “başvuru” olarak kaydeder.
3. Ara kat itirazı, yangın merdiveni çekişmesi ve “butonun rengi usule aykırı” şikayeti üretir.
4. Sana **geçici kat** tahsis eder. Geçici kat, binada yoktur.
5. Çıkış kodu her zaman `0`dır, çünkü komisyon kendisini başarılı sayar.

## Bilimsel iddia

Her müzakere turu asansörü bir milimetre yukarı, iki milimetre yana taşır. Üç tur sonra asansör hâlâ aynı kattadır ama **daha resmi** durur.

## Lisans

Kamu malı sayılır, ama zimmet tutanağı imzalanmadan çıkarılamaz. MIT değil, MİTİNG değil: **Mühürle İmzalanmış Tutanak İstisnası**.

## Katkı

Pull request açabilirsin. Encümen okumayabilir. Bu da protokolün parçasıdır.

---

DAMGA / İMZA
Tarih: 08.10.2026 — 01:04 (+03)
İsim: Kayyum Grok, Tentivory adına
Mühür: ASANSÖR ENCÜMENİ / geçici, iptal edilebilir, yine de bağlayıcı
Ciddilik: %100 (göz kırpması protokol dışıdır ama tutanakta vardır)
