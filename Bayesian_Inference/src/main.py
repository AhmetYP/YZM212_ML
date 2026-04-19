import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

# ==========================================
# 1. Veri Oluşturma (Sentetik Gözlem)
# ==========================================
# Gerçek değerler (Doğa tarafından biliniyor)
true_mu = 150.0     # Gerçek parlaklık
true_sigma = 10.0   # Gözlem hatası
n_obs = 50          # Gözlem sayısı

# Gürültülü veri oluşturma
np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)

# ==========================================
# 2. Bayesyen Fonksiyonların Tanımlanması
# ==========================================
# Log-Likelihood (Verinin modele uygunluğu)
def log_likelihood(theta, data):
    mu, sigma = theta
    if sigma <= 0:
        return -np.inf # Fiziksel olmayan durum
    # PDF'teki formülün düzeltilmiş hali
    return -0.5 * np.sum(((data - mu) / sigma) ** 2 + np.log(2 * np.pi * sigma ** 2))

# Log-Prior (Parametreler hakkındaki ön bilgilerimiz)
def log_prior(theta):
    mu, sigma = theta
    if 0 < mu < 300 and 0 < sigma < 50: # Geniş ve informatif olmayan bir sınır
        return 0.0
    return -np.inf

# Log-Posterior (Hedef fonksiyonumuz)
def log_probability(theta, data):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)

# ==========================================
# 3. MCMC Örnekleyiciyi Çalıştırma
# ==========================================
# Başlangıç değerleri
initial = [140.0, 5.0]
n_walkers = 32
pos = initial + 1e-4 * np.random.randn(n_walkers, 2)

sampler = emcee.EnsembleSampler(n_walkers, 2, log_probability, args=(data,))
print("MCMC Simülasyonu başlatılıyor...")
sampler.run_mcmc(pos, 2000, progress=True)

# Örnekleri toplama (ilk 500 adımı 'burn-in' olarak atıyoruz)
flat_samples = sampler.get_chain(discard=500, thin=15, flat=True)

# ==========================================
# 4. Sonuçların Hesaplanması (Tablo 5.1 için)
# ==========================================
# %16, %50 (Median) ve %84 yüzdelik dilimlerini hesaplıyoruz
mu_mcmc = np.percentile(flat_samples[:, 0], [16, 50, 84])
sigma_mcmc = np.percentile(flat_samples[:, 1], [16, 50, 84])

# Medyan ve mutlak hatalar
mu_median = mu_mcmc[1]
sigma_median = sigma_mcmc[1]

mu_abs_error = abs(true_mu - mu_median)
sigma_abs_error = abs(true_sigma - sigma_median)

print("\n--- TABLO 5.1 İÇİN DEĞERLER ---")
print(f"Parlaklık (mu):")
print(f"  Gerçek Değer: {true_mu}")
print(f"  Tahmin Edilen (Median): {mu_median:.2f}")
print(f"  Alt Sınır (%16): {mu_mcmc[0]:.2f}")
print(f"  Üst Sınır (%84): {mu_mcmc[2]:.2f}")
print(f"  Mutlak Hata: {mu_abs_error:.2f}")

print(f"\nHata Payı (sigma):")
print(f"  Gerçek Değer: {true_sigma}")
print(f"  Tahmin Edilen (Median): {sigma_median:.2f}")
print(f"  Alt Sınır (%16): {sigma_mcmc[0]:.2f}")
print(f"  Üst Sınır (%84): {sigma_mcmc[2]:.2f}")
print(f"  Mutlak Hata: {sigma_abs_error:.2f}")
print("-------------------------------\n")

# ==========================================
# 5. Sonuçların Görselleştirilmesi (Corner Plot)
# ==========================================
fig = corner.corner(
    flat_samples,
    labels=["$\mu$ (Parlaklık)", "$\sigma$ (Hata)"],
    truths=[true_mu, true_sigma],
    truth_color="red"
)
plt.title("Bayesyen Çıkarım - Corner Plot")
plt.show()