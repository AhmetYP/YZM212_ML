
---

# YZM212 Makine Öğrenmesi - 4. Laboratuvar Ödevi: Bayesyen Çıkarım ile Parlaklık Analizi

[cite_start]Bu proje, uzak bir galaksinin gürültülü gözlem verilerini kullanarak, gök cisminin gerçek parlaklığını ve veri setindeki belirsizliği (standart sapma) Bayesyen yöntemlerle tahmin etmeyi amaçlamaktadır[cite: 2, 4].

## 1. Problem Tanımı
[cite_start]Astronomi projelerinde gözlem verileri genellikle gürültülüdür ve laboratuvar ortamında deney yapılamadığı için belirsizliklerin yönetilmesi kritiktir[cite: 3, 5]. [cite_start]Bu çalışmada, Bayes Teoremi kullanılarak veriler ışığında bir modelin parametreleri ($\mu$ ve $\sigma$) hakkındaki bilgiler güncellenmiş ve en olası değerler kestirilmiştir[cite: 8].

## 2. Veri
[cite_start]Çalışmada, "doğa" tarafından bilinen ancak bizim tarafımızdan tahmin edilmeye çalışılan şu kontrol değişkenleri kullanılarak sentetik bir veri seti oluşturulmuştur[cite: 22, 29]:
* [cite_start]**Gerçek Parlaklık ($\mu$):** 150.0 [cite: 23]
* [cite_start]**Gözlem Hatası ($\sigma$):** 10.0 [cite: 24]
* [cite_start]**Gözlem Sayısı (n):** 50 [cite: 25]

[cite_start]Veriler, bu parametrelerle oluşturulan Gaussian dağılımına rastgele gürültü eklenerek elde edilmiştir[cite: 28].

## 3. Yöntem
[cite_start]Parametre kestirimi için **Bayesyen Çıkarım** ve **Markov Chain Monte Carlo (MCMC)** simülasyonu kullanılmıştır[cite: 15].
* [cite_start]**Kütüphaneler:** `numpy`, `emcee`, `corner`, `matplotlib`[cite: 17, 18, 19, 20].
* [cite_start]**Olasılık Fonksiyonları:** Log-Likelihood, Log-Prior (0 < $\mu$ < 300 ve 0 < $\sigma$ < 50 aralığında informatif olmayan) ve Log-Posterior fonksiyonları tanımlanmıştır[cite: 47, 51, 58].
* **MCMC Yapılandırması:** 32 yürüyüşçü (walkers) ve 2000 adım kullanılmıştır. [cite_start]İlk 500 adım "burn-in" olarak atılmıştır[cite: 66, 69, 70].

## 4. Sonuçlar
MCMC simülasyonu sonucunda elde edilen parametre değerleri aşağıda özetlenmiştir:

| Değişken | Gerçek Değer | Tahmin Edilen (Median) | Alt Sınır (%16) | Üst Sınır (%84) | Mutlak Hata |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$\mu$ (Parlaklık)** | 150.0 | 147.79 | 146.43 | 149.07 | 2.21 |
| **$\sigma$ (Hata Payı)** | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

## 5. Yorum ve Tartışma
* **Doğruluk:** Model, %6-7 civarındaki gürültü oranına rağmen gerçek parlaklık değerine yüksek bir doğrulukla yaklaşmıştır.
* **Hassasiyet:** İstatistiksel olarak ortalamanın ($\mu$) tahmini, varyansın ($\sigma$) tahmininden daha dar bir güven aralığına sahiptir. Bu durum $n=50$ gözlem sayısı ile uyumludur; gözlem sayısı arttıkça bu belirsizlikler daha da azalacaktır.
* **Korelasyon:** Corner Plot üzerindeki elips şeklindeki dağılımın eksenlere paralel olması, parlaklık tahmini ile gözlem hatası tahmini arasında bir bağımlılık (korelasyon) olmadığını göstermektedir.

---

