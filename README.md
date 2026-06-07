# Proyecto_IA_NoSupervisado-
# Sistema Inteligente de Transporte Masivo

## Descripción del Proyecto
Este proyecto implementa un sistema inteligente desarrollado en Python para el análisis y optimización de una red de transporte masivo. El proyecto se divide en dos fases principales:
1. **Búsqueda y Sistemas Basados en Reglas:** Implementación del algoritmo Breadth-First Search (BFS) para encontrar la ruta con el menor número de estaciones entre un origen y un destino utilizando una base de conocimiento en forma de grafo.
2. **Aprendizaje No Supervisado (Clustering):** Implementación del algoritmo K-Means para agrupar las estaciones de la red en diferentes perfiles operativos, basándose en variables como el volumen de pasajeros diario, tiempos de espera y cantidad de conexiones.

## Información Académica
* **Institución:** Corporación Universitaria Iberoamericana
* **Facultad:** Ingeniería
* **Programa:** Ingeniería de Ciencias de Datos
* **Asignatura:** Inteligencia Artificial
* **Docente:** Joaquin Sanchez
* **Integrantes:** Carlos David Alvarez Ojeda y Manuel Galindo Peña

## Estructura del Proyecto
Proyecto_IA_NoSupervisado/
├── dataset/
│   └── dataset_estaciones.csv
├── src/
│   └── modelo_kmeans.py
├── docs/
│   ├── descripcion_datos.pdf
│   ├── pruebas_componente.pdf
│   └── diagrama_estaciones.drawio
├── README.md
└── .gitignore                     

## Diagrama
graph TD
    %% Definición de Clústeres para GitHub/GitLab
    
    subgraph Cluster 0: Alta Demanda
        PN[Portal Norte]
        S[Suba]
        H[Heroes]
    end

    subgraph Cluster 2: Flujo Moderado
        C100[Calle 100]
        C72[Calle 72]
        M[Museo]
    end

    subgraph Cluster 1: Nodo Aislado
        A[Aeropuerto]
    end

    %% Conexiones de la red según tu diccionario
    PN --- C100
    PN --- S
    C100 --- H
    S --- H
    H --- C72
    C72 --- M

## Requisitos Previos
Antes de ejecutar el proyecto, es necesario tener instalado:
* Python 3.x
* Gestor de paquetes `pip`

Para instalar las dependencias necesarias, ejecuta en la terminal:
```bash
pip install -r requisitos.txt

