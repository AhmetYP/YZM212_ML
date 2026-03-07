# HMM ile İzole Kelime Tanıma Sistemi Tasarımı

Bu proje, 2025-2026 Bahar Dönemi YZM212 Makine Öğrenmesi dersi kapsamında, Gizli Markov Modelleri (Hidden Markov Model - HMM) kullanılarak geliştirilmiş izole bir kelime tanıma simülasyonudur.

## Problem Tanımı
Konuşma tanıma sistemlerinde kelimeler, "fonem" adı verilen temel ses birimlerinden oluşmaktadır. Bu projede amaç, dışarıdan gelen ve bilinmeyen bir ses verisinin (gözlem dizisinin), önceden tanımlanmış "EV" ve "OKUL" HMM modellerinden hangisine daha yüksek olasılıkla (Log-Likelihood) ait olduğunu bularak kelime sınıflandırması yapmaktır.

## Veri
Projede iki temel bileşen üzerinden modelleme yapılmıştır:
* **Gizli Durumlar (Hidden States):** Kelimeleri oluşturan fonemleri temsil eder (Örn: "EV" kelimesi için S={e, v}).
* **Gözlemler (Observations):** Sesin frekans karakteristiğini temsil eden spektrum verileridir (O={High, Low}). Uygulama aşamasında test verisi olarak [High, Low, Low] (indeks karşılığı [0, 1, 1]) ardışık gözlem dizisi kullanılmıştır.

## Yöntem
Çalışma teorik ve uygulamalı olmak üzere iki aşamada gerçekleştirilmiştir:
* **Teorik Modelleme:** İlk aşamada Viterbi Algoritması kullanılarak, verilen geçiş ve emisyon olasılıkları üzerinden [High, Low] gözlem dizisini üreten en olası fonem dizisi matematiksel olarak (adım adım) hesaplanmıştır.
* **Uygulama (Python):** Python dilinde hmmlearn kütüphanesi kullanılarak "EV" ve "OKUL" kelimeleri için iki ayrı model (CategoricalHMM) tanımlanmıştır. Modellerin olasılık matrisleri belirlendikten sonra, test verisi ([0, 1, 1]) sisteme verilmiş ve her iki modelin Log-Likelihood (score) değerleri hesaplanarak karşılaştırılmıştır.

## Sonuçlar
Sisteme verilen [High, Low, Low] test verisi üzerinde yapılan sınıflandırma sonucunda elde edilen Log-Likelihood puanları şöyledir:
* **EV Modeli Puanı:** -1.3295
* **OKUL Modeli Puanı:** -2.5624

Hesaplamalar sonucunda EV modelinin skoru daha yüksek çıktığı için, sisteme verilen sesin "EV" kelimesine ait olduğu tahmin edilmiştir. Teorik kısımda yapılan Viterbi algoritması el hesaplamaları `report/cozum_anahtari.pdf` dosyasında sunulmuştur.

## Yorum ve Tartışma
* **Gürültünün Etkisi:** Ses verisindeki gürültü (noise), HMM modelinin emisyon (yayılma) olasılıklarının dağılımını düzleştirerek (bozarak) sistemin belirli bir fonemi ayırt etme gücünü zayıflatır. Bu durum modelin yanlış duruma geçiş yapma ihtimalini artırır.
* **Derin Öğrenme vs. HMM:** Gerçek bir sistemde binlerce kelime olduğunda, kelime ve fonem kombinasyonları nedeniyle HMM'in durum uzayı devasa boyutlara ulaşır ve Viterbi algoritmasının hesaplama maliyeti katlanarak artar. Ayrıca HMM'in dayandığı Markov varsayımı insan dilindeki uzun vadeli bağlamları yakalamada yetersiz kaldığından, bu tür büyük ölçekli problemlerde akustik ve dil modellerini uçtan uca öğrenebilen Derin Öğrenme yapıları (RNN, LSTM, Transformer vb.) tercih edilmektedir.

## Proje Dizin Yapısı
Proje klasör yapısı aşağıdaki gibidir:

    HMM-Speech-Recognition/
    ├── data/
    ├── src/
    │   └── recognizer.py       # HMM sınıflandırma ve Log-Likelihood hesaplama kodları
    ├── report/
    │   └── cozum_anahtari.pdf  # Viterbi el hesaplamaları ve teorik analiz yanıtları
    ├── requirements.txt        # Proje bağımlılıkları (hmmlearn, numpy vb.)
    └── README.md               # Proje dokümantasyonu