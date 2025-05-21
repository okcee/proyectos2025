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

