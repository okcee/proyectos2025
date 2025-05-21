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

