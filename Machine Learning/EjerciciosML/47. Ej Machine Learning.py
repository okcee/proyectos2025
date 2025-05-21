''' Predicción para acertar la lotería - Practicar con algoritmos y obtener la serie con mas posiblidades de acertar la lotería

🌟 Descripción general
Imagina que eres parte del equipo de análisis predictivo de una empresa de juegos de azar.
Tu tarea es desarrollar un sistema capaz de analizar combinaciones de lotería y estimar cuáles tienen más probabilidad de éxito, utilizando inteligencia artificial.
Para ello, crearás un modelo de clasificación con RandomForestClassifier que aprenda de datos históricos simulados, y luego lo aplicarás a nuevas combinaciones para seleccionar las mejores.

📌 Objetivos del proyecto
Desarrollar una aplicación completa compuesta por varias clases, que sea capaz de:
Simular combinaciones de lotería (con 6 números únicos entre 1 y 49).
Generar datos de entrenamiento con etiquetas de "éxito" (1) o "fracaso" (0), simulando que el 10% de las combinaciones históricas fueron ganadoras.
Entrenar un modelo de machine learning para predecir la probabilidad de éxito.
Aplicar el modelo a nuevas combinaciones aleatorias.
Mostrar la mejor combinación según el modelo.
Visualizar en una gráfica las 10 combinaciones con mayor probabilidad de éxito.

🧱 Clases que debes implementar
1.  Clase GeneradorSeries
Responsable de generar combinaciones aleatorias:
Método generar_series(cantidad): genera cantidad combinaciones de 6 números únicos aleatorios entre 1 y 49.
Cada combinación debe estar ordenada para mayor coherencia visual.
2. Clase DatosLoteria
Encargada de crear los datos de entrenamiento:
Método generar_datos_entrenamiento(cantidad=1000): genera un DataFrame con 1000 combinaciones y una columna adicional llamada "Exito" con valores 1 (éxito) o 0 (fracaso), simulando que el 10% de las combinaciones fueron ganadoras.
3. Clase ModeloLoteria
Encargada de construir y entrenar el modelo predictivo:
Entrena un modelo de RandomForestClassifier.
Métodos:
entrenar(X, y): entrena el modelo con los datos escalados.
predecir_probabilidades(X): devuelve las probabilidades de éxito para cada combinación evaluada.
4. Clase VisualizadorResultados
Responsable de mostrar los resultados en un gráfico:
Método graficar_top_combinaciones(df_series, probabilidades, top_n=10):
Muestra un gráfico de barras horizontal con las 10 combinaciones más prometedoras.
Usa matplotlib.pyplot.
5. Clase EjecutarSimulacion
Clase principal que ejecuta todo el flujo del proyecto:
Método ejecutar():
Genera los datos simulados.
Entrena el modelo.
Genera nuevas combinaciones a evaluar.
Predice la probabilidad de éxito.
Muestra por pantalla la mejor combinación encontrada.
Muestra un gráfico con las 10 más prometedoras.

📌 Requisitos técnicos
Utiliza pandas y numpy para manipular datos.
Usa RandomForestClassifier de sklearn.ensemble.
Escala las características numéricas con StandardScaler.
Crea gráficos con matplotlib.pyplot.

🎯 Ejemplo de uso
simulacion = EjecutarSimulacion()
simulacion.ejecutar()

Salida esperada
🎯 Mejor serie encontrada:
Números: [7, 35, 39, 41, 43, 47]
Probabilidad estimada de éxito: 0.4300
'''

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

class GeneradorSeries:
    """
    Responsable de generar combinaciones aleatorias de lotería.
    """
    def generar_series(self, cantidad: int, numeros_por_serie: int = 6, min_num: int = 1, max_num: int = 49) -> np.ndarray:
        """
        Genera 'cantidad' de combinaciones de lotería.

        Args:
            cantidad (int): Número de combinaciones a generar.
            numeros_por_serie (int): Cantidad de números en cada combinación (default 6).
            min_num (int): Número mínimo posible en la lotería (default 1).
            max_num (int): Número máximo posible en la lotería (default 49).

        Returns:
            np.ndarray: Un array de NumPy donde cada fila es una combinación ordenada.
        """
        series_generadas = []
        for _ in range(cantidad):
            # Asegura que los números sean únicos y dentro del rango
            if max_num - min_num + 1 < numeros_por_serie:
                raise ValueError("El rango de números es demasiado pequeño para la cantidad de números por serie.")
            serie = sorted(random.sample(range(min_num, max_num + 1), numeros_por_serie))
            series_generadas.append(serie)
        return np.array(series_generadas)

class DatosLoteria:
    """
    Encargada de crear los datos de entrenamiento para el modelo de lotería.
    """
    def __init__(self, generador: GeneradorSeries = None):
        """
        Inicializa la clase con un generador de series.

        Args:
            generador (GeneradorSeries, optional): Instancia de GeneradorSeries. 
                                                   Si None, se creará una instancia por defecto.
        """
        if generador is None:
            self.generador = GeneradorSeries()
        else:
            self.generador = generador

    def generar_datos_entrenamiento(self, cantidad: int = 1000, porcentaje_exito: float = 0.10) -> pd.DataFrame:
        """
        Genera un DataFrame con combinaciones y una columna "Exito".

        Args:
            cantidad (int): Número total de combinaciones a generar para el entrenamiento.
            porcentaje_exito (float): Proporción de combinaciones que serán marcadas como "Exito" (1).

        Returns:
            pd.DataFrame: DataFrame con las combinaciones y la columna "Exito".
                          Las columnas de las combinaciones se nombrarán 'N1', 'N2', ..., 'N6'.
        """
        # Generar las combinaciones de lotería
        series = self.generador.generar_series(cantidad)
        
        # Crear DataFrame
        column_names = [f'N{i+1}' for i in range(series.shape[1])]
        df_entrenamiento = pd.DataFrame(series, columns=column_names)
        
        # Generar etiquetas de éxito/fracaso
        # Se simula que un 'porcentaje_exito' de las combinaciones son ganadoras
        num_exitos = int(cantidad * porcentaje_exito)
        etiquetas = np.zeros(cantidad, dtype=int)
        indices_exito = np.random.choice(cantidad, num_exitos, replace=False)
        etiquetas[indices_exito] = 1
        
        df_entrenamiento['Exito'] = etiquetas
        
        return df_entrenamiento

class ModeloLoteria:
    """
    Encargada de construir, entrenar y usar el modelo predictivo de lotería.
    """
    def __init__(self, random_state: int = 42):
        """
        Inicializa el modelo y el escalador.

        Args:
            random_state (int): Semilla para reproducibilidad del RandomForestClassifier.
        """
        self.modelo = RandomForestClassifier(random_state=random_state, n_estimators=100) # n_estimators es un hiperparámetro común
        self.escalador = StandardScaler()
        self.columnas_entrenamiento = None # Para guardar los nombres de las columnas usadas en el entrenamiento

    def entrenar(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Entrena el modelo RandomForestClassifier con los datos proporcionados.
        Los datos X son escalados antes del entrenamiento.

        Args:
            X (pd.DataFrame): Características (las combinaciones de números).
            y (pd.Series): Variable objetivo (Etiqueta "Exito").
        """
        # Guardar los nombres de las columnas para asegurar consistencia en la predicción
        self.columnas_entrenamiento = X.columns.tolist()

        # Escalar las características
        X_escalado = self.escalador.fit_transform(X)
        
        # Entrenar el modelo
        self.modelo.fit(X_escalado, y)
        print("Modelo RandomForestClassifier entrenado.")

    def predecir_probabilidades(self, X_nuevas: pd.DataFrame) -> np.ndarray:
        """
        Predice las probabilidades de éxito para nuevas combinaciones.
        Las nuevas combinaciones son escaladas usando el mismo escalador ajustado durante el entrenamiento.

        Args:
            X_nuevas (pd.DataFrame): Nuevas combinaciones a evaluar. Debe tener las mismas columnas que X_entrenamiento.

        Returns:
            np.ndarray: Array con las probabilidades de éxito (clase 1) para cada combinación.
        """
        # Asegurar que las columnas estén en el mismo orden que en el entrenamiento
        if self.columnas_entrenamiento is None:
            raise RuntimeError("El modelo debe ser entrenado antes de hacer predicciones.")
        
        X_nuevas_ordenadas = X_nuevas[self.columnas_entrenamiento]

        # Escalar las nuevas características
        X_nuevas_escalado = self.escalador.transform(X_nuevas_ordenadas)
        
        # Predecir probabilidades (devuelve probabilidades para cada clase, nos interesa la clase 1 "Exito")
        probabilidades = self.modelo.predict_proba(X_nuevas_escalado)[:, 1]
        return probabilidades

class VisualizadorResultados:
    """
    Responsable de mostrar los resultados en un gráfico.
    """
    def graficar_top_combinaciones(self, df_series_evaluadas: pd.DataFrame, probabilidades: np.ndarray, top_n: int = 10) -> None:
        """
        Muestra un gráfico de barras horizontal con las 'top_n' combinaciones más prometedoras.

        Args:
            df_series_evaluadas (pd.DataFrame): DataFrame con las series evaluadas (columnas 'N1' a 'N6').
            probabilidades (np.ndarray): Array de probabilidades de éxito para cada serie en df_series_evaluadas.
            top_n (int): Número de combinaciones a mostrar en el gráfico.
        """
        if len(df_series_evaluadas) != len(probabilidades):
            raise ValueError("El DataFrame de series y el array de probabilidades deben tener la misma longitud.")

        # Crear un DataFrame temporal para facilitar la ordenación y selección
        df_resultados = df_series_evaluadas.copy()
        df_resultados['Probabilidad'] = probabilidades
        
        # Ordenar por probabilidad de forma descendente y tomar las top_n
        df_top = df_resultados.sort_values(by='Probabilidad', ascending=False).head(top_n)
        
        # Crear etiquetas para el gráfico (las combinaciones como strings)
        etiquetas_series = df_top.iloc[:, :-1].apply(lambda row: ', '.join(map(str, row)), axis=1) # Excluye la columna 'Probabilidad'
        
        plt.figure(figsize=(12, 8))
        bars = plt.barh(etiquetas_series, df_top['Probabilidad'], color='skyblue')
        plt.xlabel('Probabilidad Estimada de Éxito')
        plt.ylabel('Combinaciones de Lotería')
        plt.title(f'Top {top_n} Combinaciones de Lotería Más Prometedoras')
        plt.gca().invert_yaxis() # Mostrar la más probable arriba
        
        # Añadir el valor de la probabilidad en cada barra
        for bar in bars:
            plt.text(bar.get_width() + 0.005,  # Posición x (un poco a la derecha de la barra)
                     bar.get_y() + bar.get_height()/2, # Posición y (centro de la barra)
                     f'{bar.get_width():.4f}', # Texto a mostrar (probabilidad formateada)
                     va='center', ha='left')

        plt.tight_layout() # Ajustar para que no se corten las etiquetas
        plt.show()

class EjecutarSimulacion:
    """
    Clase principal que ejecuta todo el flujo del proyecto de predicción de lotería.
    """
    def __init__(self, cantidad_entrenamiento: int = 2000, cantidad_evaluar: int = 100):
        """
        Inicializa los parámetros de la simulación.

        Args:
            cantidad_entrenamiento (int): Número de series para generar datos de entrenamiento.
            cantidad_evaluar (int): Número de nuevas series aleatorias para evaluar.
        """
        self.cantidad_entrenamiento = cantidad_entrenamiento
        self.cantidad_evaluar = cantidad_evaluar
        self.generador_series = GeneradorSeries()
        self.datos_loteria = DatosLoteria(generador=self.generador_series)
        self.modelo_loteria = ModeloLoteria(random_state=42) # Usar random_state para reproducibilidad
        self.visualizador = VisualizadorResultados()

    def ejecutar(self) -> None:
        """
        Ejecuta el flujo completo:
        1. Genera datos de entrenamiento.
        2. Entrena el modelo.
        3. Genera nuevas combinaciones a evaluar.
        4. Predice la probabilidad de éxito para las nuevas combinaciones.
        5. Muestra la mejor combinación encontrada.
        6. Muestra un gráfico con las 10 combinaciones más prometedoras.
        """
        print("🚀 Iniciando Simulación de Predicción de Lotería 🚀")

        # 1. Generar datos de entrenamiento
        print(f"\n🔄 Generando {self.cantidad_entrenamiento} series para entrenamiento...")
        df_entrenamiento = self.datos_loteria.generar_datos_entrenamiento(cantidad=self.cantidad_entrenamiento)
        X_entrenamiento = df_entrenamiento.drop('Exito', axis=1)
        y_entrenamiento = df_entrenamiento['Exito']
        print(f"   Datos de entrenamiento generados. Forma de X: {X_entrenamiento.shape}, Forma de y: {y_entrenamiento.shape}")

        # 2. Entrenar el modelo
        print("\n🧠 Entrenando el modelo de predicción...")
        self.modelo_loteria.entrenar(X_entrenamiento, y_entrenamiento)

        # 3. Generar nuevas combinaciones a evaluar
        print(f"\n✨ Generando {self.cantidad_evaluar} nuevas combinaciones para evaluar...")
        series_nuevas_np = self.generador_series.generar_series(cantidad=self.cantidad_evaluar)
        # Convertir a DataFrame con los mismos nombres de columna que el entrenamiento
        df_series_nuevas = pd.DataFrame(series_nuevas_np, columns=X_entrenamiento.columns)
        print(f"   Nuevas combinaciones generadas. Forma: {df_series_nuevas.shape}")

        # 4. Predecir la probabilidad de éxito
        print("\n🔮 Prediciendo probabilidades de éxito para las nuevas combinaciones...")
        probabilidades_exito = self.modelo_loteria.predecir_probabilidades(df_series_nuevas)

        # 5. Mostrar la mejor combinación encontrada
        if len(probabilidades_exito) > 0:
            indice_mejor_serie = np.argmax(probabilidades_exito)
            mejor_serie_numeros = df_series_nuevas.iloc[indice_mejor_serie].values.tolist()
            mejor_probabilidad = probabilidades_exito[indice_mejor_serie]
            
            print("\n🎯 Mejor serie encontrada:")
            print(f"   Números: {mejor_serie_numeros}")
            print(f"   Probabilidad estimada de éxito: {mejor_probabilidad:.4f}")
        else:
            print("\n⚠️ No se generaron series para evaluar, no se puede mostrar la mejor combinación.")


        # 6. Mostrar un gráfico con las 10 combinaciones más prometedoras
        if len(df_series_nuevas) > 0 and len(probabilidades_exito) > 0:
            print("\n📊 Generando gráfico de las 10 combinaciones más prometedoras...")
            self.visualizador.graficar_top_combinaciones(df_series_nuevas, probabilidades_exito, top_n=10)
        else:
            print("\n⚠️ No hay suficientes datos para generar el gráfico.")
        
        print("\n✅ Simulación completada.")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Para que la simulación sea más "interesante" y el modelo tenga algo que aprender,
    # podríamos aumentar la cantidad de datos de entrenamiento.
    # Con 1000 muestras y 10% de éxito, solo hay 100 ejemplos positivos, lo que puede ser poco.
    # Aumentar a 5000 o 10000 podría dar resultados más diferenciados, aunque la naturaleza
    # aleatoria de la lotería hace que predecir sea inherentemente difícil.
    simulacion = EjecutarSimulacion(cantidad_entrenamiento=5000, cantidad_evaluar=200)
    simulacion.ejecutar()
