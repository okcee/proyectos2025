import pandas as pd
import numpy as np

'''Ejercicio 1
Crea una lista "asignaturas" con los textos "matematicas", "fisica", "historia"
Crea una lista "notas" con los valores 9,9,8
Crea una serie con la lista "notas" como valores, y la lista "asignaturas" como indices
Crea la variable "nota_fisica" con la nota de la asignatura "fisica"
Mediante el metodo "print" muestra la frase "La nota de fisica es un ..." (Sustituir ... por la nota de física)
'''
asignaturas = ['matematicas', 'fisica', 'historia']
notas = [9,9,8]
serie = pd.Series(data=notas,index=asignaturas)
notas_fisica = serie['fisica']
print("La nota de física es un", format(notas_fisica))


'''Ejercicio 2
El objetivo será crear un dataframe con las ventas de nuestras 3 oficinas para los meses de enero, febrero y marzo.
Pasos a seguir:
Crea una variable "ventas_enero" que contenga una lista de 3 números enteros aleatorios entre 100 y 500.
Crea una variable "ventas_febrero" que contenga una lista de 3 números enteros aleatorios entre 100 y 500.
Crea una variable "ventas_marzo" que contenga una lista de 3 números enteros aleatorios entre 100 y 500.
Crea una variable "filas" que contenga esta lista de palabras: 'ventas_enero','ventas_febrero','ventas_marzo'
Crea una variable "columnas" que contenga esta lista de palabras: 'oficina1','oficina2','oficina3'
Crea una variable "ventas" que contenga una lista con los valores de ventas de enero, febrero y marzo
Crea una variable "dataframe" que contenga las ventas, filas y columnas
Mediante "print" muestra el valor de "Las ventas de enero para la oficina 1 son de ...."
'''
ventas_enero = np.random.randint(100, 500, 3)
ventas_febrero = np.random.randint(100, 500, 3)
ventas_marzo = np.random.randint(100, 500, 3)

filas = ['ventas_enero','ventas_febrero','ventas_marzo']
columnas = ['oficina1','oficina2','oficina3']
ventas = [ventas_enero,ventas_febrero,ventas_marzo]

dataframe = pd.DataFrame(ventas, filas, columnas)
print("Las ventas de enero para la oficina 1 son de:")
print(dataframe['oficina1']['ventas_enero'], '\n')
