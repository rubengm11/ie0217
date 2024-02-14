import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def clustering(data):
    # Caracteristicas de interes
    features_for_clustering = ['selling_price', 'km_driven', 'year']
    data_for_clustering = data[features_for_clustering]

    # Estandarizar las caracteristicas
    scaler = StandardScaler()
    data_for_clustering_scaled = scaler.fit_transform(data_for_clustering)

    # Evaluacion con el metodo del codo
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_for_clustering_scaled)
        inertia.append(kmeans.inertia_)

    # Grafico el metodo del codo
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Método del Codo para Determinar el Número Óptimo de Clusters')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Inercia')
    plt.show()

    # Evaluacion con el metodo de silhouette
    silhouette_scores = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_for_clustering_scaled)
        labels = kmeans.labels_
        silhouette_scores.append(silhouette_score(data_for_clustering_scaled, labels))

    # Grafico el metodo de silhouette
    plt.plot(range(2, 11), silhouette_scores, marker='o')
    plt.title('Método de Silhouette para Determinar el Número Óptimo de Clusters')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Silhouette Score')
    plt.show()


    # K-Means con el número optimo de clusters (3) encontrado con los metodos anteriores
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(data_for_clustering_scaled)

    data['cluster'] = labels

    # Analisis de clusters con PCA
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(data_for_clustering_scaled)

    plt.scatter(data_pca[:, 0], data_pca[:, 1], c=labels, cmap='viridis', edgecolor='k', s=50)
    plt.title('Visualización de Clusters con PCA')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.show()

    # Evaluacion del rendimiento
    print("\nResultado del Clustering:")
    print(data[['selling_price', 'km_driven', 'year', 'cluster']].head())
