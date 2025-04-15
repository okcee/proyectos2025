# Series

import numpy as np
import pandas as pd

etiquetas = ['a', 'b', 'c']
datos = [1,2,3]
pd.Series(data = datos, index = etiquetas)
print("Panda 1 :\n", pd.Series(datos,etiquetas))

array = np.arange(6, 9)
etiqueta2 = ['venta 1:', 'venta 2:', 'venta 3:']
pd.Series(array)
print("Panda 2 :\n", pd.Series(array, etiqueta2))

serie1 = pd.Series(array, etiqueta2)
print("Serie 1 :\n", serie1)

print("Imprimir un solo valor:", serie1['venta 1:'])# por la etiqueta
print("Imprimir un solo valor:", serie1[1]) # por posición
print("Imprimir  un solo valor:", serie1.iloc[1]) # por posición])

datos2 = ["MemoriaRAM", 118, "DiscoSSD", 170] # Las series permiten tenner datos de diferente tipo
etiquetas3 = ["Producto 1. ", "Valor 1. ", "Producto 2. ", "Valor 2. "]
serie2 = pd.Series(datos2, etiquetas3)
print("Serie 2 es:\n",pd.Series(serie2, etiquetas3))

# Suma de series

serie3 = pd.Series([1,2,3,4],["ventas1", "ventas2", "ventas3", "ventas4"]) # Si alguna tiene un dato más veríamos que hay un valor nulo (NaN), pero suma los posibles
serie4 = pd.Series([4,8,5],["ventas1", "ventas2", "ventas3"])
serie5 = serie3 + serie4
print("Serie 3 es:\n",serie3)
print("Serie 4 es:\n",serie4)
print("Serie 5 (La suma de Serie 3 y Serie 4) es:\n",serie5)
