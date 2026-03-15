# YZM212 Makine Öğrenmesi - 2. Laboratuvar Ödevi: MLE ile Akıllı Şehir Planlaması

## Problem Tanımı
Bu projede, bir belediyenin ulaşım departmanı senaryosu üzerinden, şehrin en yoğun ana caddesindeki trafik akışının (bir dakikada geçen araç sayısı) Poisson Dağılımı kullanılarak modellenmesi amaçlanmıştır. Gelecekteki trafiği tahmin edebilmek adına en uygun parametre (λ), Maximum Likelihood Estimation (MLE) yöntemiyle hesaplanmıştır.

## Veri
Modelin eğitilmesi ve test edilmesi için, bir dakikada geçen araç sayısını gösteren 14 gözlemden oluşan küçük bir trafik veri seti kullanılmıştır: `[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]`.

## Yöntem
* **Teorik (Analitik) Çözüm:** Poisson dağılımı için Likelihood ve Log-Likelihood fonksiyonları matematiksel olarak türetilmiş, türev alınarak optimal parametrenin verilerin aritmetik ortalamasına eşit olduğu kanıtlanmıştır.
* **Sayısal (Numerical) Çözüm:** Python üzerinde `scipy.optimize` kütüphanesi kullanılarak Negatif Log-Likelihood (NLL) fonksiyonu minimize edilmiş ve sayısal MLE tahmini gerçekleştirilmiştir.
* **Görselleştirme:** Bulunan λ değeri ile oluşturulan teorik Poisson Olasılık Kütle Fonksiyonu (PMF), gerçek verinin histogramı ile üst üste çizdirilerek modelin uyumu analiz edilmiştir.

## Sonuçlar
Hem analitik türetme (aritmetik ortalama) hem de Python ile yapılan sayısal optimizasyon sonucunda, trafik modeli için en uygun parametre değeri **λ ≈ 12.14** olarak bulunmuştur. 

## Yorum ve Tartışma
Elde edilen görselleştirmeler, küçük bir veri seti olmasına rağmen Poisson modelinin gerçek veri dağılımına (özellikle 11-13 araç bandındaki tepe noktasına) iyi bir uyum sağladığını göstermektedir. 
Bununla birlikte, MLE yöntemi (Poisson için doğrudan ortalamaya bağlı olduğundan) aykırı değerlere (outliers) karşı son derece hassastır. Yanlışlıkla girilecek yüksek bir gözlem değeri (örn. 200), λ parametresini şiddetle saptırarak trafik yoğunluğunun gerçekte olduğundan çok daha fazla algılanmasına ve hatalı altyapı kararları alınmasına (örn. gereksiz yol genişletme) yol açabilir. Bu durum, makine öğrenmesi süreçlerinde anomali tespitinin önemini vurgulamaktadır.
