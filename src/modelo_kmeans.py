import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

def main():
    print("--- SISTEMA INTELIGENTE DE TRANSPORTE - CLUSTERING AVANZADO ---")
    
    # 1. Cargar datos
    ruta_dataset = '../dataset/dataset_estaciones.csv'
    if not os.path.exists(ruta_dataset):
        ruta_dataset = 'dataset/dataset_estaciones.csv'
        
    try:
        df = pd.read_csv(ruta_dataset)
        print("Dataset cargado exitosamente con 5 variables operativas.\n")
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")
        return

    features = ['Pasajeros_Dia', 'Tiempo_Espera_Min', 'Conexiones', 'Buses_Hora', 'Incidentes_Mes']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['PCA1'] = X_pca[:, 0]
    df['PCA2'] = X_pca[:, 1]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=150)
    
    for i in range(df.shape[0]):
        plt.text(df['PCA1'][i] + 0.1, df['PCA2'][i] + 0.1, df['Estacion'][i], fontsize=9)

    plt.title('Agrupamiento de Estaciones de Transporte (K-Means)')
    plt.xlabel('Componente Principal 1 (Volumen y Flujo)')
    plt.ylabel('Componente Principal 2 (Tiempos e Incidentes)')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    os.makedirs('../docs', exist_ok=True)
    plt.savefig('../docs/clusters_visualizacion.png', bbox_inches='tight')
    print("Gráfica exportada exitosamente a 'docs/clusters_visualizacion.png'.\n")

    print("Resultados del Agrupamiento:")
    print("-" * 50)
    for i in range(3):
        estaciones = df[df['Cluster'] == i]['Estacion'].tolist()
        print(f"Perfil Operativo {i}: {', '.join(estaciones)}")
        
    df.drop(columns=['PCA1', 'PCA2']).to_csv('../dataset/resultados_clustering.csv', index=False)
    print("\nDataset con clústeres asignados exportado a 'dataset/resultados_clustering.csv'.")

if __name__ == '__main__':
    main()