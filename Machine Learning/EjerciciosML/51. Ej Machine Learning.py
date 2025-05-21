''' Segmentación de Clientes y Predicción de Compra - Practicar con diferentes algoritmos de forma conjunta

Contexto
Eres analista de datos en una empresa de comercio electrónico que quiere mejorar su estrategia de marketing mediante la segmentación de clientes y la predicción de su intención de compra.

Tu objetivo es crear un sistema que:
Genere datos sintéticos representativos de clientes reales, con variables como cuánto gastan, cuántas compras hacen, y con qué frecuencia compran.
Segmente a los clientes en grupos similares usando un algoritmo de clustering.
Entrene un modelo predictivo para estimar si un cliente comprará en el próximo mes basándose en sus características y el segmento al que pertenece.
Visualice los segmentos y la probabilidad de compra para facilitar la interpretación de los resultados.

Datos proporcionados y estructura
Clase CustomerDataGenerator
Esta clase debe generar un DataFrame con 300 clientes sintéticos, cada uno con estas columnas:
total_spent: Dinero total gastado por el cliente, en euros (valor aleatorio entre 50 y 1500).
total_purchases: Número total de compras realizadas (entero entre 1 y 50).
purchase_frequency: Frecuencia de compra mensual (valor entre 0.5 y 10).
will_buy_next_month: Etiqueta binaria (1 o 0) que indica si el cliente comprará el próximo mes. La regla para asignar 1 es: si total_spent > 500 y purchase_frequency > 4, el cliente comprará (1), si no, no comprará (0).

Modelado
Clase CustomerSegmentationModel
Esta clase debe:
Recibir el DataFrame generado.
Segmentar clientes en 3 grupos usando KMeans con las variables total_spent, total_purchases y purchase_frequency.
Añadir la columna customer_segment al DataFrame con el número de segmento asignado a cada cliente.
Entrenar un modelo de regresión logística para predecir will_buy_next_month, usando como variables las originales más la segmentación (transformada en variables dummy).
Proveer métodos para obtener la precisión del modelo y la matriz de confusión.

Visualizaciones
Función graficar_segmentos(data):
Genera un scatter plot de total_spent vs purchase_frequency.
Usa colores diferentes para cada segmento.
Añade leyenda, etiquetas y título descriptivo.
Función graficar_probabilidad_compra(modelo):
Muestra cómo varía la probabilidad de compra del cliente en función del gasto total (total_spent), manteniendo constantes total_purchases=25 y purchase_frequency=5.
Dibuja la curva de probabilidad predicha por el modelo de regresión logística.

Indicaciones numéricas y técnicas
Número de muestras: 300.
Número de clusters para KMeans: 3.
Random seed: 42 para reproducibilidad.
División de datos para entrenamiento/prueba: 80% / 20%.
Iteraciones máximas para la regresión logística: 500.
Uso solo de numpy, pandas, sklearn y matplotlib

Ejemplo de uso
# 1. Generar datos
generador = CustomerDataGenerator()
datos_clientes = generador.generate(300)
# 2. Crear modelo
modelo = CustomerSegmentationModel(datos_clientes)
modelo.segment_customers()
modelo.train_model()
# 3. Resultados
print("Precisión del modelo:", modelo.get_accuracy())
print("Matriz de confusión:\n", modelo.get_confusion_matrix())
# 4. Visualizaciones
graficar_segmentos(modelo.data)
graficar_probabilidad_compra(modelo.model)

Salida esperada
Precisión del modelo: 0.8833333333333333
Matriz de confusión:
 [[30  2]
 [ 5 23]]
'''

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Constante para la semilla aleatoria para reproducibilidad
RANDOM_SEED = 42

class CustomerDataGenerator:
    """
    Genera datos sintéticos de clientes.
    """
    def __init__(self, random_seed=RANDOM_SEED):
        """
        Inicializa el generador de datos.
        Args:
            random_seed (int): Semilla para la generación de números aleatorios.
        """
        self.random_seed = random_seed
        # Establecer la semilla para numpy directamente aquí asegura que se use para todas las operaciones.
        np.random.seed(self.random_seed)

    def generate(self, num_samples=300):
        """
        Genera un DataFrame con datos sintéticos de clientes.

        Args:
            num_samples (int): Número de muestras de clientes a generar.

        Returns:
            pd.DataFrame: DataFrame con los datos de los clientes.
                          Columnas: 'total_spent', 'total_purchases', 
                                    'purchase_frequency', 'will_buy_next_month'.
        """
        # Generar características iniciales
        data = {
            'total_spent': np.random.uniform(50, 1500, num_samples),
            'total_purchases': np.random.randint(1, 51, num_samples),
            'purchase_frequency': np.random.uniform(0.5, 10, num_samples)
        }
        df = pd.DataFrame(data)

        # Definir la etiqueta 'will_buy_next_month' según la regla especificada
        # Si total_spent > 500 y purchase_frequency > 4, el cliente comprará (1), si no (0).
        df['will_buy_next_month'] = np.where(
            (df['total_spent'] > 500) & (df['purchase_frequency'] > 4), 1, 0
        )
        return df

class CustomerSegmentationModel:
    """
    Realiza la segmentación de clientes y entrena un modelo de predicción de compra.
    """
    def __init__(self, data: pd.DataFrame, random_seed=RANDOM_SEED):
        """
        Inicializa el modelo de segmentación y predicción.

        Args:
            data (pd.DataFrame): DataFrame con los datos de los clientes.
            random_seed (int): Semilla para operaciones aleatorias (KMeans, train_test_split, LogisticRegression).
        """
        self.data = data.copy()  # Trabajar con una copia para no modificar el original
        self.random_seed = random_seed
        self.kmeans_model = None
        self.model = None  # Modelo de Regresión Logística
        self.X_test = None
        self.y_test = None
        self.lr_feature_names = None # Nombres de las características usadas para la Regresión Logística

    def segment_customers(self, n_clusters=3):
        """
        Segmenta los clientes en `n_clusters` grupos usando KMeans.
        Las características para el clustering son 'total_spent', 'total_purchases', y 'purchase_frequency'.
        Añade una columna 'customer_segment' al DataFrame.

        Args:
            n_clusters (int): Número de clusters para KMeans.
        """
        features_for_clustering = ['total_spent', 'total_purchases', 'purchase_frequency']
        X_cluster = self.data[features_for_clustering]

        # Inicializar y entrenar el modelo KMeans
        # n_init=10 es una buena práctica para estabilidad y es el default en versiones antiguas de sklearn.
        # random_state para reproducibilidad.
        self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=self.random_seed, n_init=10)
        self.data['customer_segment'] = self.kmeans_model.fit_predict(X_cluster)

    def train_model(self, test_size=0.2, max_iter_logreg=500):
        """
        Entrena un modelo de regresión logística para predecir 'will_buy_next_month'.
        Utiliza las características originales más la segmentación del cliente (transformada en variables dummy).

        Args:
            test_size (float): Proporción del dataset para el conjunto de prueba.
            max_iter_logreg (int): Número máximo de iteraciones para el solver de Regresión Logística.
        """
        if 'customer_segment' not in self.data.columns:
            raise ValueError("La segmentación de clientes debe realizarse antes de entrenar el modelo.")

        # Crear variables dummy para 'customer_segment'
        # dtype=int para que las dummies sean 0 o 1 enteros.
        segment_dummies = pd.get_dummies(self.data['customer_segment'], prefix='segment', dtype=int)
        
        # Preparar características (X) y variable objetivo (y)
        original_features = ['total_spent', 'total_purchases', 'purchase_frequency']
        X = pd.concat([self.data[original_features], segment_dummies], axis=1)
        y = self.data['will_buy_next_month']
        
        # Guardar los nombres de las características para referencia futura
        self.lr_feature_names = X.columns.tolist()

        # Dividir los datos en conjuntos de entrenamiento y prueba
        # stratify=y es útil para mantener la proporción de clases en la división.
        X_train, self.X_test, y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_seed, stratify=y
        )

        # Inicializar y entrenar el modelo de Regresión Logística
        # solver='liblinear' es adecuado para datasets pequeños y problemas binarios.
        self.model = LogisticRegression(
            random_state=self.random_seed, 
            max_iter=max_iter_logreg,
            solver='liblinear' 
        )
        self.model.fit(X_train, y_train)

    def get_accuracy(self):
        """
        Calcula y devuelve la precisión del modelo en el conjunto de prueba.

        Returns:
            float: Precisión del modelo.
        """
        if self.model is None or self.X_test is None or self.y_test is None:
            raise ValueError("El modelo no ha sido entrenado o los datos de prueba no están disponibles.")
        y_pred = self.model.predict(self.X_test)
        return accuracy_score(self.y_test, y_pred)

    def get_confusion_matrix(self):
        """
        Calcula y devuelve la matriz de confusión del modelo en el conjunto de prueba.

        Returns:
            np.ndarray: Matriz de confusión.
        """
        if self.model is None or self.X_test is None or self.y_test is None:
            raise ValueError("El modelo no ha sido entrenado o los datos de prueba no están disponibles.")
        y_pred = self.model.predict(self.X_test)
        return confusion_matrix(self.y_test, y_pred)

def graficar_segmentos(data: pd.DataFrame):
    """
    Genera un gráfico de dispersión de 'total_spent' vs 'purchase_frequency',
    coloreando los puntos según 'customer_segment'.

    Args:
        data (pd.DataFrame): DataFrame que incluye 'total_spent', 'purchase_frequency',
                             y 'customer_segment'.
    """
    if 'customer_segment' not in data.columns:
        print("Advertencia: La columna 'customer_segment' no se encontró en los datos para graficar.")
        return

    plt.figure(figsize=(10, 6))
    
    unique_segments = sorted(data['customer_segment'].unique())
    # Usar plt.get_cmap para compatibilidad con versiones de Matplotlib
    # Si plt.get_cmap no está disponible (muy viejo Matplotlib), plt.cm.get_cmap es el fallback.
    try:
        cmap = plt.get_cmap('viridis', len(unique_segments))
    except AttributeError: 
        cmap = plt.cm.get_cmap('viridis', len(unique_segments))


    for i, segment_id in enumerate(unique_segments):
        segment_data = data[data['customer_segment'] == segment_id]
        plt.scatter(segment_data['total_spent'], 
                    segment_data['purchase_frequency'], 
                    label=f'Segmento {segment_id}',
                    color=cmap(i), # Asignar color del colormap
                    alpha=0.7, s=50) # s es el tamaño del punto

    plt.title('Segmentación de Clientes: Gasto Total vs. Frecuencia de Compra')
    plt.xlabel('Gasto Total (€)')
    plt.ylabel('Frecuencia de Compra (mensual)')
    plt.legend(title='Segmentos')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def graficar_probabilidad_compra(log_reg_model: LogisticRegression):
    """
    Muestra cómo varía la probabilidad de compra del cliente en función del 'total_spent',
    manteniendo 'total_purchases'=25 y 'purchase_frequency'=5 constantes.
    La curva de probabilidad se predice usando el modelo de regresión logística proporcionado.
    Asume que el modelo fue entrenado con características que incluyen dummies de segmento
    (ej. 'segment_0', 'segment_1', 'segment_2') y grafica la probabilidad para el 'segment_0'.

    Args:
        log_reg_model (LogisticRegression): El modelo de regresión logística entrenado.
    """
    # Intentar obtener los nombres de las características del modelo (sklearn >= 0.23/0.24)
    if hasattr(log_reg_model, 'feature_names_in_'):
        lr_feature_names = log_reg_model.feature_names_in_
    else:
        # Fallback si 'feature_names_in_' no está disponible (versiones antiguas de sklearn)
        # Esta es una suposición basada en la estructura del problema.
        print("Advertencia: El modelo de Regresión Logística no tiene 'feature_names_in_'.")
        print("Se asumirán nombres de características estándar para la gráfica de probabilidad:")
        print("['total_spent', 'total_purchases', 'purchase_frequency', 'segment_0', 'segment_1', 'segment_2']")
        lr_feature_names = ['total_spent', 'total_purchases', 'purchase_frequency', 
                            'segment_0', 'segment_1', 'segment_2']
                            
    # Rango para 'total_spent' (basado en la generación de datos)
    total_spent_range = np.linspace(50, 1500, 300)
    
    # Crear un diccionario para los datos del DataFrame de predicción
    plot_df_data = {}

    # Establecer las características constantes y la variable que cambia
    plot_df_data['total_spent'] = total_spent_range
    plot_df_data['total_purchases'] = 25  # Constante según el requisito
    plot_df_data['purchase_frequency'] = 5 # Constante según el requisito

    # Establecer las variables dummy de segmento
    # Se asume que se grafica para el 'segment_0'
    # y que las columnas dummy se llaman 'segment_X' (ej. segment_0, segment_1, segment_2)
    # Esta parte es crucial y depende de cómo se nombraron las dummies durante el entrenamiento.
    assumed_plot_segment_dummy = 'segment_0' # Asumimos graficar para el segmento 0
    found_target_segment_dummy = False

    for feature_name in lr_feature_names:
        if feature_name.startswith('segment_'):
            if feature_name == assumed_plot_segment_dummy:
                plot_df_data[feature_name] = np.ones_like(total_spent_range, dtype=int)
                found_target_segment_dummy = True
            else:
                # Otras dummies de segmento se ponen a 0
                plot_df_data[feature_name] = np.zeros_like(total_spent_range, dtype=int)
    
    if not found_target_segment_dummy and any(name.startswith('segment_') for name in lr_feature_names):
        print(f"Advertencia: La columna dummy '{assumed_plot_segment_dummy}' no se encontró entre las características del modelo.")
        print("La gráfica de probabilidad podría no representar el segmento deseado.")
        # Si el dummy asumido no existe, pero otros sí, la gráfica no será para ese segmento.
        # Podríamos intentar tomar el primer dummy 'segment_X' encontrado, pero es menos específico.

    # Crear el DataFrame para la predicción
    try:
        # Asegurar que el DataFrame tenga todas las columnas esperadas por el modelo y en el orden correcto
        plot_df = pd.DataFrame(plot_df_data, columns=lr_feature_names)
    except ValueError as e:
        # Esto podría ocurrir si una columna en lr_feature_names no está en plot_df_data (ej. un error en la lógica anterior)
        print(f"Error al crear DataFrame para la gráfica de probabilidad: {e}")
        print(f"Columnas esperadas por el modelo: {lr_feature_names}")
        print(f"Columnas generadas en plot_df_data: {list(plot_df_data.keys())}")
        return
    except KeyError as e:
        # Esto podría ocurrir si una columna en lr_feature_names no está en plot_df_data
        print(f"Error de KeyError al crear DataFrame para la gráfica de probabilidad: {e}. Falta una columna.")
        print(f"Columnas esperadas por el modelo: {lr_feature_names}")
        print(f"Columnas generadas en plot_df_data: {list(plot_df_data.keys())}")
        # Intentar crear el DataFrame con las columnas disponibles y rellenar las que falten si es posible
        # o simplemente retornar si la situación es irrecuperable.
        # Forzamos la creación con las columnas que tenemos y las que faltan serán NaN, lo que fallará en predict_proba
        # Es mejor asegurar que plot_df_data contenga todas las lr_feature_names.
        # La lógica actual de construcción de plot_df_data debería cubrir todas las lr_feature_names.
        # Si no es así, hay un problema en la suposición de nombres o en la lógica.
        return


    # Predecir probabilidades (probabilidad de la clase 1)
    probabilities = log_reg_model.predict_proba(plot_df)[:, 1]

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(total_spent_range, probabilities, label=f'Probabilidad de Compra (Asumiendo {assumed_plot_segment_dummy})')
    plt.title('Probabilidad de Compra Estimada vs. Gasto Total del Cliente')
    plt.xlabel('Gasto Total (€)')
    plt.ylabel('Probabilidad Estimada de Compra el Próximo Mes')
    plt.ylim(0, 1) # La probabilidad está entre 0 y 1
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# --- Ejemplo de Uso ---
if __name__ == '__main__':
    # Establecer la semilla global de numpy para asegurar la reproducibilidad.
    # CustomerDataGenerator y CustomerSegmentationModel también usan RANDOM_SEED internamente.
    np.random.seed(RANDOM_SEED)

    # 1. Generar datos
    print("1. Generando datos de clientes...")
    generador = CustomerDataGenerator(random_seed=RANDOM_SEED)
    datos_clientes = generador.generate(300)
    print(f"Datos generados: {datos_clientes.shape[0]} muestras.")
    # print(datos_clientes.head()) # Descomentar para ver una muestra

    # 2. Crear y entrenar el modelo
    print("\n2. Creando y entrenando el modelo de segmentación y predicción...")
    modelo_segmentacion = CustomerSegmentationModel(datos_clientes, random_seed=RANDOM_SEED)
    
    print("   Segmentando clientes...")
    modelo_segmentacion.segment_customers(n_clusters=3)
    # print(modelo_segmentacion.data['customer_segment'].value_counts()) # Ver distribución

    print("   Entrenando modelo de predicción de compra...")
    modelo_segmentacion.train_model(test_size=0.2, max_iter_logreg=500)
    print("   Modelo entrenado.")

    # 3. Resultados del modelo
    print("\n3. Resultados del modelo de predicción:")
    precision = modelo_segmentacion.get_accuracy()
    matriz_confusion = modelo_segmentacion.get_confusion_matrix()
    
    print(f"Precisión del modelo: {precision}")
    print("Matriz de confusión:\n", matriz_confusion)

    # 4. Visualizaciones
    print("\n4. Generando visualizaciones...")
    
    # Gráfico de Segmentos
    print("   Mostrando gráfico de segmentación de clientes...")
    graficar_segmentos(modelo_segmentacion.data)
    
    # Gráfico de Probabilidad de Compra
    # La función espera solo el modelo de regresión logística según el enunciado.
    print("   Mostrando gráfico de probabilidad de compra...")
    if modelo_segmentacion.model:
        graficar_probabilidad_compra(modelo_segmentacion.model)
    else:
        print("   No se pudo generar la gráfica de probabilidad: el modelo no está entrenado.")

    print("\n--- Fin del script ---")
