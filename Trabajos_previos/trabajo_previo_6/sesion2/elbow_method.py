from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Generar datos aleatorios
X = np.random.rand(100, 2) * 10

# Lista para almacenar las inercias para diferentes valores de k
inertias = []

# Probar diferentes valores de k
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    kmeans.fit(X)
    
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Metodo del Codo')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Inercia')
plt.show()

