# Laboratuvar 3: Özdeğerler ve Özvektörler (Eigenvalues & Eigenvectors)

Bu çalışma, YZM212 Makine Öğrenmesi dersi kapsamında, matris manipülasyonlarının temel taşlarından olan özdeğer ve özvektör kavramlarının teorik ve pratik analizini içermektedir.

## 1. Makine Öğrenmesi ve Matris İlişkisi

Matematiksel olarak bir matris dönüşümü şu denklemle ifade edilir:
$$A \cdot v = \lambda \cdot v$$
Burada **$\lambda$** bir skaler değerdir (özdeğer). 

**Makine Öğrenmesindeki Rolü:**
Özdeğerler ve özvektörler, verinin boyutunu indirgerken bilgisini korumamızı sağlayan **Temel Bileşen Analizi (PCA)** gibi yöntemlerin temelini oluşturur. Ayrıca öneri sistemlerinde kullanılan **Tekil Değer Ayrıştırması (SVD)** ve grafik teorisi tabanlı kümeleme algoritmalarında kritik rol oynarlar.

*Referans: Machine Learning Mastery - Introduction to Eigenvalues and Eigenvectors.*

## 2. Numpy `linalg.eig` Fonksiyon Analizi

Numpy kütüphanesinin `linalg` modülü altında bulunan `eig` fonksiyonu, karesel matrislerin özdeğer ve özvektörlerini hesaplamak için kullanılır.

* **Dokümantasyon:** Fonksiyon, biri özdeğerleri (w) diğeri ise normalize edilmiş özvektörleri (v) içeren iki yapı döndürür. Özvektörler matrisin sütunlarında saklanır.
* **Kaynak Kod ve İşleyiş:** Numpy'ın GitHub kaynak kodları incelendiğinde, hesaplamaların doğrudan Python ile değil, arka planda yüksek performanslı **LAPACK** (Linear Algebra Package) kütüphanesinin `_geev` rutinleri kullanılarak yapıldığı görülmüştür. Bu sayede karmaşık matris işlemleri çok düşük hata payı ve yüksek hızla gerçekleştirilir.

## 3. Manuel Uygulama ve Karşılaştırma

Bu aşamada, Numpy'ın hazır fonksiyonunu kullanmadan, iteratif bir yaklaşımla (Power Iteration) dominant özdeğer hesaplaması yapılmıştır.

**Referans Çalışma:** [LucasBN - Eigenvalues and Eigenvectors](https://github.com/LucasBN/Eigenvalues-and-Eigenvectors)

### Elde Edilen Bulgular
Aynı matris üzerinde yapılan testlerde:
- **Manuel Yöntem:** İterasyonlar sonucunda en büyük (dominant) özdeğere ve ilgili özvektöre başarıyla yakınsanmıştır.
- **Numpy `eig` Yöntemi:** Matrisin tüm özdeğerlerini anlık ve daha yüksek hassasiyetle hesaplamıştır.

İki yöntem karşılaştırıldığında, manuel algoritmanın eğitim amaçlı mantığı kavramada yararlı olduğu, ancak profesyonel projelerde Numpy'ın LAPACK tabanlı çözümünün hız ve kararlılık açısından tercih edilmesi gerektiği sonucuna varılmıştır.

---
**Hazırlayan:** Ahmet 
**Ders:** YZM212 Makine Öğrenmesi