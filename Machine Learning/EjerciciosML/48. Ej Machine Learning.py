''' Clasificación Automática de Frutas - Practicar con algoritmos de clasificación

Contexto:
Eres parte de un equipo que desarrolla una app para supermercados inteligentes. Tu tarea es crear un clasificador automático de frutas basado en dos características: peso (en gramos) y tamaño (en cm). El modelo debe aprender a distinguir entre Manzanas, Plátanos y Naranjas usando datos generados de forma simulada.

Objetivo:
Construir una solución modular en Python que:
Genere datos aleatorios simulando las características físicas de frutas.
Entrene un clasificador K-Nearest Neighbors (KNN) con esos datos.
Permita predecir el tipo de fruta dados su peso y tamaño.
Muestre gráficamente los datos con colores distintos para cada fruta.

🔧 Especificaciones técnicas
1. Crear la clase GeneradorFrutas
Método: generar(self, num_muestras)
Debe generar num_muestras pares [peso, tamaño] y su respectiva etiqueta: "Manzana", "Plátano" o "Naranja".
Rango de valores por tipo:
Manzana: peso entre 120–200g, tamaño entre 7–9cm
Plátano: peso entre 100–150g, tamaño entre 12–20cm
Naranja: peso entre 150–250g, tamaño entre 8–12cm
2. Crear la clase ClasificadorFrutas
Constructor: __init__(self, k=3)
Método: entrenar(self, X, y) para entrenar un modelo KNeighborsClassifier
Método: predecir(self, peso, tamaño) que devuelva una fruta como string.
3: Crear la clase VisualizadorFrutas
Método: graficar(self, X, y, titulo="Frutas") que grafique un scatter plot (matplotlib), con color distinto por clase.
4: Clase principal AppClasificacionFrutas
Método: ejecutar(self)
Genera 100 muestras con GeneradorFrutas
Entrena el modelo con ClasificadorFrutas
Predice el tipo de fruta para una muestra nueva: peso 140g y tamaño 18cm
Imprime la predicción.
Muestra un gráfico de las frutas generadas.

✅ Ejemplo de uso
simulador = SimuladorFrutas()
simulador.ejecutar()

Salida esperada
🔍 Precisión del modelo: 90.00%
🍎 La fruta predicha para peso=140g y tamaño=18cm es: Plátano
'''

Resuelve en un script python el ejercicio 48. Ej Machine Learning.py Crea el código limpio y con comentarios que sea compatible con el entorno de udemy No es necesario explicaciones, solo el script para copiar