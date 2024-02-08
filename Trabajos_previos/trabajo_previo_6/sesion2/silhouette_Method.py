from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Generar datos aleatorios
X = np.random.rand(100, 2) * 10  

silhouette_scores = []  

# Iterar sobre diferentes valores de k
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k, random_state=42)  
    kmeans.fit(X) 
    
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score) 

plt.plot(range(2, 20), silhouette_scores, marker='o')
plt.title('Método de la Silueta')  
plt.xlabel('Número de Clusters (k)')  
plt.ylabel('Coeficiente de Silueta')  
plt.show()

