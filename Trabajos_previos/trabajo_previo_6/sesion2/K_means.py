from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = np.random.rand(100, 2) * 10

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c='blue', marker='o')
plt.title('Puntos de Datos Aleatorios')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1],
                c=('r' if labels[i] == 0 else 'b' if labels[i] == 1 else 'g'),
                marker='o')

plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=200, label='Centroids')
plt.title('Resultado del Clustering con K-Means')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
plt.legend()

plt.tight_layout()
plt.show()
