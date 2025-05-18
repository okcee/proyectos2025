# Random Forest (Bosque Aleatorio)
'''
Random Forest es una combinación de árboles de decisión donde cada árbol selecciona una clase y luego se combinan las decisiones de cada árbol para seleccionar una clase final ganadora.  
Es uno de los algoritmos de aprendizaje de clasificación con mayor precisión.
Funciona eficientemente en bases de datos grandes y puede manejar cientos de variables de entrada.

Ensemble de Árboles de Decisión: Como bien dices, es una técnica de ensemble que combina múltiples árboles de decisión. No es solo un árbol, sino un "bosque" de ellos.
Votación (o Promedio): En problemas de clasificación, cada árbol del bosque "vota" por una clase, y la clase ganadora (la que recibe más votos) es la predicción final del modelo Random Forest. En problemas de regresión, se suele promediar las predicciones de cada árbol.
Alta Precisión: Es reconocido por ser uno de los algoritmos de clasificación más robustos y que, a menudo, logra una alta precisión. Esto se debe a que reduce el sobreajuste (overfitting) que puede ocurrir con árboles de decisión individuales profundos, promediando sus errores y sesgos.
Manejo de Datos Grandes y Muchas Variables: Es eficiente y escalable para trabajar con grandes conjuntos de datos y puede gestionar eficazmente bases de datos con cientos o miles de variables de entrada sin necesidad de una selección de características previa exhaustiva.
'''

