import numpy as np

# Fungsi untuk menghitung cosine similarity antara dua vektor
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

# Representasi vektor dari dokumen A, B, C, D, E, dan F
A = np.array([1, 1, 1, 1, 0, 0])
B = np.array([1, 0, 1, 0, 1, 1])
C = np.array([1, 1, 0, 0, 1, 0])
D = np.array([1, 1, 1, 0, 0, 1])
E = np.array([0, 1, 0, 1, 1, 1])
F = np.array([0, 0, 1, 1, 1, 1])

# Menghitung cosine similarity antara dokumen A dengan dokumen B, C, D, E, dan F
similarity_AB = cosine_similarity(A, B)
similarity_AC = cosine_similarity(A, C)
similarity_AD = cosine_similarity(A, D)
similarity_AE = cosine_similarity(A, E)
similarity_AF = cosine_similarity(A, F)

# Mencetak hasil cosine similarity
print("Cosine similarity antara dokumen A dan B:", similarity_AB)
print("Cosine similarity antara dokumen A dan C:", similarity_AC)
print("Cosine similarity antara dokumen A dan D:", similarity_AD)
print("Cosine similarity antara dokumen A dan E:", similarity_AE)
print("Cosine similarity antara dokumen A dan F:", similarity_AF)
