from hmmlearn.hmm import CategoricalHMM
import numpy as np

# --- 1. 'EV' Modeli Tanımlaması ---
# n_components=2: e ve v durumları
model_ev = CategoricalHMM(n_components=2)
model_ev.n_features = 2  # High (0) ve Low (1) olmak üzere 2 gözlem çeşidi

# Teorik kısımdaki parametrelerin atanması
model_ev.startprob_ = np.array([1.0, 0.0])
model_ev.transmat_ = np.array([
    [0.6, 0.4],
    [0.2, 0.8]
])
model_ev.emissionprob_ = np.array([
    [0.7, 0.3],
    [0.1, 0.9]
])

# --- 2. 'OKUL' Modeli Tanımlaması ---
# OKUL kelimesi için rastgele ama mantıklı olasılıklar atayarak temsili bir model kuruyoruz.
model_okul = CategoricalHMM(n_components=2)
model_okul.n_features = 2

model_okul.startprob_ = np.array([0.5, 0.5])
model_okul.transmat_ = np.array([
    [0.5, 0.5],
    [0.3, 0.7]
])
model_okul.emissionprob_ = np.array([
    [0.4, 0.6],
    [0.8, 0.2]
])

# --- 3. Test Verisi ---
# Dışarıdan gelen yeni bir ses kaydı: High, Low, Low -> [0, 1, 1]
test_data = np.array([[0, 1, 1]]).T


# --- 4. Log-Likelihood Hesaplama ve Sınıflandırma ---
def classify_speech(observation_seq):
    # Her iki modelin bu gözlem dizisini üretme olasılığını (Log-Likelihood) hesaplıyoruz
    score_ev = model_ev.score(observation_seq)
    score_okul = model_okul.score(observation_seq)

    print(f"EV Modeli Log-Likelihood Puanı: {score_ev:.4f}")
    print(f"OKUL Modeli Log-Likelihood Puanı: {score_okul:.4f}")
    print("-" * 30)

    # Hangi model daha yüksek puan veriyorsa, ses o kelimeye aittir
    if score_ev > score_okul:
        print("Sonuç: Bu ses büyük ihtimalle 'EV' kelimesine aittir.")
    else:
        print("Sonuç: Bu ses büyük ihtimalle 'OKUL' kelimesine aittir.")


# Tahmin fonksiyonunu çalıştır
classify_speech(test_data)