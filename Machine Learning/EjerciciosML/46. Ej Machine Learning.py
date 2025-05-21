''' Agrupación de clientes según comportamientos de compra - Practicar con algoritmos de agrupación de machine learning

🎯 Objetivo General:
Simular un conjunto de datos de clientes con características comerciales, aplicar técnicas de machine learning no supervisado para segmentarlos mediante agrupamiento (clustering), y visualizar los resultados para analizar distintos perfiles de cliente. Todo el proyecto debe estar organizado usando clases.

📦 Requisitos:
Utiliza las librerías:
numpy
matplotlib
sklearn.cluster.KMeans
sklearn.preprocessing.StandardScaler
Estructura tu código en tres clases:
SimuladorClientes
ModeloSegmentacionClientes
TestSegmentacionClientes
🧩 Clase SimuladorClientes
Esta clase debe simular los datos de clientes con las siguientes características:
Atributos esperados (por cliente):
Monto gastado: valor entre 100 y 10,000.
Frecuencia de compras: entre 1 y 100.
Categorías preferidas: 3 valores aleatorios entre 1 y 5 (representando número de compras por categoría).
Implementa el método:
def generar_datos(self) -> np.ndarray
Este método debe devolver un array de 200 muestras, cada una con 3 columnas:
Monto gastado
Frecuencia de compras
Total de categorías preferidas (suma de los 3 valores generados)
🧠 Clase ModeloSegmentacionClientes
Esta clase debe encargarse de entrenar el modelo y realizar predicciones.
Atributos:
n_clusters: número de grupos a formar (por defecto: 3).
scaler: instancia de StandardScaler.
modelo: instancia de KMeans.
Métodos requeridos:
entrenar(datos: np.ndarray) -> None:
Escala los datos con StandardScaler.
Ajusta el modelo KMeans.
Guarda los datos escalados como atributo para futuras visualizaciones.
predecir(cliente_nuevo: list) -> int:
Recibe un nuevo cliente (3 características).
Escala sus datos.
Devuelve el número de cluster al que pertenece.
🧪 Clase TestSegmentacionClientes
Clase para integrar y probar todo el sistema. Implementa el método:
def ejecutar(self) -> None
Este método debe:
Crear una instancia de SimuladorClientes y generar los datos.
Instanciar ModeloSegmentacionClientes con 3 clusters.
Entrenar el modelo con los datos simulados.
Mostrar los primeros 5 registros de los datos simulados.
Predecir el cluster para un nuevo cliente con los siguientes datos:
cliente_nuevo = [2000, 10, 12]
(Significa: gastó 2000, compra 10 veces, tiene 12 compras sumadas en sus categorías preferidas).
  6. Mostrar por pantalla el cluster al que pertenece este nuevo cliente.
  7. Incluye una visualización de los datos segmentados usando matplotlib.
Representa los clientes en un gráfico de dispersión donde:
El eje X es el monto gastado.
El eje Y es la frecuencia de compras.
Los puntos se colorean según el cluster al que pertenecen (usa modelo.modelo.labels_ para obtenerlos).
Añade etiquetas, título, y barra de color.

💡 Consejos para el alumno
Usa np.column_stack para combinar varias columnas en un array.
Escalar los datos es fundamental en clustering: sin esto, las variables dominantes como “monto gastado” podrían sesgar los grupos.
Usa KMeans(n_clusters=3, random_state=42) para asegurar reproducibilidad.

🧪 Ejemplo de uso
test = TestSegmentacionClientes()
test.ejecutar()
Salida esperada
Primeros 5 registros de datos simulados:
[[3.80794718e+03 2.40000000e+01 1.00000000e+01]
 [9.51207163e+03 7.50000000e+01 1.30000000e+01]
 [7.34674002e+03 7.20000000e+01 9.00000000e+00]
 [6.02671899e+03 3.60000000e+01 1.00000000e+01]
 [1.64458454e+03 3.80000000e+01 9.00000000e+00]]
Modelo entrenado con 3 clusters.
El nuevo cliente pertenece al cluster: 1
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class SimuladorClientes:
    """
    Esta clase simula los datos de clientes con características comerciales.
    """
    def __init__(self, n_muestras: int = 200):
        """
        Inicializa el simulador.
        Args:
            n_muestras (int): Número de muestras de clientes a generar.
        """
        self.n_muestras = n_muestras

    def generar_datos(self) -> np.ndarray:
        """
        Genera datos simulados de clientes.

        Retorna:
            np.ndarray: Array de 200 muestras, cada una con 3 columnas:
                        - Monto gastado
                        - Frecuencia de compras
                        - Total de categorías preferidas (suma de 3 valores aleatorios entre 1 y 5)
        """
        # Monto gastado: valor entre 100 y 10,000
        monto_gastado = np.random.uniform(100, 10000, self.n_muestras)

        # Frecuencia de compras: entre 1 y 100
        frecuencia_compras = np.random.randint(1, 101, self.n_muestras)

        # Categorías preferidas: 3 valores aleatorios entre 1 y 5 (representando número de compras por categoría)
        # Suma de los 3 valores generados
        compras_categorias = np.random.randint(1, 6, size=(self.n_muestras, 3))
        total_categorias_preferidas = compras_categorias.sum(axis=1)

        # Combinar las columnas en un solo array
        datos_clientes = np.column_stack((monto_gastado, frecuencia_compras, total_categorias_preferidas))
        
        return datos_clientes

class ModeloSegmentacionClientes:
    """
    Esta clase se encarga de entrenar el modelo de segmentación y realizar predicciones.
    """
    def __init__(self, n_clusters: int = 3):
        """
        Inicializa el modelo de segmentación.

        Args:
            n_clusters (int): Número de grupos a formar (por defecto: 3).
        """
        self.n_clusters = n_clusters
        self.scaler = StandardScaler()
        # Usar KMeans(n_clusters=n_clusters, random_state=42) para asegurar reproducibilidad.
        # n_init='auto' o n_init=10 es el valor por defecto en versiones recientes de scikit-learn para evitar warnings.
        # Siguiendo estrictamente el consejo del alumno, solo se usa random_state.
        self.modelo = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10) 
        self.datos_escalados = None # Para guardar los datos escalados para visualizaciones

    def entrenar(self, datos: np.ndarray) -> None:
        """
        Entrena el modelo de segmentación.
        Escala los datos con StandardScaler y ajusta el modelo KMeans.
        Guarda los datos escalados como atributo.

        Args:
            datos (np.ndarray): Datos de los clientes para entrenar el modelo.
        """
        # Escalar los datos
        self.datos_escalados = self.scaler.fit_transform(datos)
        
        # Ajustar el modelo KMeans
        self.modelo.fit(self.datos_escalados)
        print(f"Modelo entrenado con {self.n_clusters} clusters.")

    def predecir(self, cliente_nuevo: list) -> int:
        """
        Predice el cluster para un nuevo cliente.

        Args:
            cliente_nuevo (list): Lista con las 3 características del nuevo cliente.
                                  [Monto gastado, Frecuencia de compras, Total de categorías preferidas]

        Retorna:
            int: Número de cluster al que pertenece el nuevo cliente.
        """
        # Convertir la lista a un array de NumPy y reestructurarlo
        cliente_nuevo_np = np.array(cliente_nuevo).reshape(1, -1)
        
        # Escalar los datos del nuevo cliente usando el scaler ajustado
        cliente_nuevo_escalado = self.scaler.transform(cliente_nuevo_np)
        
        # Predecir el cluster
        prediccion = self.modelo.predict(cliente_nuevo_escalado)
        
        return prediccion[0]

class TestSegmentacionClientes:
    """
    Clase para integrar y probar todo el sistema de segmentación de clientes.
    """
    def ejecutar(self) -> None:
        """
        Ejecuta el flujo completo de simulación, entrenamiento, predicción y visualización.
        """
        # 1. Crear una instancia de SimuladorClientes y generar los datos.
        print("Generando datos de clientes...")
        simulador = SimuladorClientes(n_muestras=200)
        datos_clientes = simulador.generar_datos()

        # 2. Instanciar ModeloSegmentacionClientes con 3 clusters.
        print("\nInicializando modelo de segmentación...")
        segmentador = ModeloSegmentacionClientes(n_clusters=3)

        # 3. Entrenar el modelo con los datos simulados.
        print("Entrenando modelo...")
        segmentador.entrenar(datos_clientes)

        # 4. Mostrar los primeros 5 registros de los datos simulados.
        print("\nPrimeros 5 registros de datos simulados:")
        print(datos_clientes[:5])

        # 5. Predecir el cluster para un nuevo cliente.
        cliente_nuevo = [2000, 10, 12] 
        # (Significa: gastó 2000, compra 10 veces, tiene 12 compras sumadas en sus categorías preferidas)
        print(f"\nPrediciendo cluster para el nuevo cliente: {cliente_nuevo}")
        cluster_predicho = segmentador.predecir(cliente_nuevo)
        
        # 6. Mostrar por pantalla el cluster al que pertenece este nuevo cliente.
        print(f"El nuevo cliente pertenece al cluster: {cluster_predicho}")

        # 7. Incluye una visualización de los datos segmentados usando matplotlib.
        if segmentador.datos_escalados is not None and segmentador.modelo.labels_ is not None:
            print("\nGenerando visualización de la segmentación...")
            plt.figure(figsize=(10, 7))
            
            # Usar los datos escalados para la visualización, como se guardaron en el modelo
            # Eje X: Monto gastado (escalado) - primera columna de datos_escalados
            # Eje Y: Frecuencia de compras (escalada) - segunda columna de datos_escalados
            scatter = plt.scatter(
                segmentador.datos_escalados[:, 0], 
                segmentador.datos_escalados[:, 1], 
                c=segmentador.modelo.labels_, 
                cmap='viridis',
                alpha=0.7,
                edgecolors='k'
            )
            
            # Marcar los centroides de los clusters
            centroides = segmentador.modelo.cluster_centers_
            plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, alpha=0.9, marker='X', label='Centroides')

            plt.xlabel("Monto Gastado (Escalado)")
            plt.ylabel("Frecuencia de Compras (Escalada)")
            plt.title("Segmentación de Clientes por Comportamiento de Compra")
            
            # Crear leyenda para los clusters
            legend_labels = [f'Cluster {i}' for i in range(segmentador.n_clusters)]
            # Crear una leyenda para los puntos de datos (clusters)
            # Esto es un poco más complejo con scatter si los colores son directos por 'c'
            # Una forma es crear handles manualmente o usar la barra de color.
            # La barra de color es más directa aquí.
            cbar = plt.colorbar(scatter, ticks=range(segmentador.n_clusters))
            cbar.set_label('Cluster')
            
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.show()
        else:
            print("No se pueden generar los gráficos porque el modelo no ha sido entrenado o los datos escalados no están disponibles.")

if __name__ == "__main__":
    # Ejemplo de uso
    test = TestSegmentacionClientes()
    test.ejecutar()
