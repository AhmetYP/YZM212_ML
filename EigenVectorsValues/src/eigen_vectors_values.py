import numpy as np

# Karşılaştırma yapabilmek için örnek bir karesel matris oluşturalım
A = np.array([[4, 1],
              [2, 3]])


# --- YÖNTEM 1: Numpy linalg.eig Kullanmadan Hesaplama (Referans: LucasBN Yaklaşımı) ---
def calculate_eigen_manual(matrix, iterations=100):
    # Rastgele bir başlangıç vektörü (özvektör adayı) oluştur
    v = np.random.rand(matrix.shape[1])

    for _ in range(iterations):
        # Matris ile vektörü çarp (yönü ve büyüklüğü değiştir)
        v_new = np.dot(matrix, v)
        # Vektörü normalize et (büyüklüğü 1 yap)
        v = v_new / np.linalg.norm(v_new)

    # Rayleigh bölümü ile özdeğeri hesapla: (v^T * A * v) / (v^T * v)
    # v normalize olduğu için payda kısmı (v^T * v) zaten 1'dir.
    eigenvalue = np.dot(v.T, np.dot(matrix, v))
    return eigenvalue, v


manuel_eigenvalue, manuel_eigenvector = calculate_eigen_manual(A)

# --- YÖNTEM 2: Numpy linalg.eig Kullanarak Hesaplama ---
numpy_eigenvalues, numpy_eigenvectors = np.linalg.eig(A)

# Numpy'ın bulduğu sonuçlar arasından en büyüğünü (dominant olanı) seçelim ki manuel ile kıyaslayabilelim
dominant_idx = np.argmax(numpy_eigenvalues)
numpy_dominant_eigenvalue = numpy_eigenvalues[dominant_idx]
numpy_dominant_eigenvector = numpy_eigenvectors[:, dominant_idx]

# --- SONUÇLARI YAZDIRMA VE KARŞILAŞTIRMA ---
print("--- 1. Manuel Hesaplama (eig kullanılmadan) ---")
print(f"Dominant Özdeğer: {manuel_eigenvalue:.4f}")
print(f"Özvektör: {manuel_eigenvector}\n")

print("--- 2. Numpy linalg.eig Hesaplaması ---")
print(f"Dominant Özdeğer: {numpy_dominant_eigenvalue:.4f}")
print(f"Özvektör: {numpy_dominant_eigenvector}")