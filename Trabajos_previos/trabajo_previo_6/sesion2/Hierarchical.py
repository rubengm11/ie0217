import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering

# Generar datos de prueba con 3 clusters
X, y = make_blobs(n_samples=50, centers=3, random_state=42, cluster_std=1.0)

Z = linkage(X, method='complete')

# Visualizar el dendrograma
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Dendrograma Hierarchical Clustering')
plt.xlabel('indice del Punto de Datos')
plt.ylabel('Distancia')
plt.show()

# Aplicar clustering jerarquico con 3 clusters
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clustering.fit_predict(X)

plt.scatter(
    X[:, 0], X[:, 1],
    c=agg_labels,
    cmap='viridis',
    edgecolor='k',
    s=50
)
plt.title('Resultado del Clustering Jerarquico')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
plt.show()
