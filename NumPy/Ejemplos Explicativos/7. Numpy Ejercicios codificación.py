import numpy as np

'''Ejercicio 1
Generar N números aleatorios enteros entre un valor mínimo y máximo
Desarrolla una función llamada generar_numeros_enteros_aleatorios que tome como entrada el número de elementos N, un valor mínimo minimo y un valor máximo maximo, y utilice NumPy para generar una lista de N números enteros aleatorios en el rango [minimo, maximo].
def generar_numeros_enteros_aleatorios(N, minimo, maximo):
# Ejemplo de uso
N = 5
minimo = 1
maximo = 10
resultado = generar_numeros_enteros_aleatorios(N, minimo, maximo)
print(resultado)
Resultado:
[4, 10, 1, 8, 2]
'''
def generar_numeros_enteros_aleatorios(N, minimo, maximo):
    numeros_aleatorios = np.random.randint(minimo, maximo + 1, N)
    return numeros_aleatorios
print(generar_numeros_enteros_aleatorios(5, 1, 10))

'''Ejercicio 2
Generar una Secuencia de Números
Desarrolla una función llamada generar_secuencia_numerica que tome como entrada un valor mínimo minimo, un valor máximo maximo y un paso paso, y utilice NumPy para generar una secuencia de números en el rango [minimo, maximo) con el paso especificado.
def generar_secuencia_numerica(minimo, maximo, paso):
# Ejemplo de uso
minimo = 0
maximo = 10
paso = 2
resultado = generar_secuencia_numerica(minimo, maximo, paso)
print(resultado)
Resultado
[0 2 4 6 8]
Tipo de datos del resultado
type(resultado)
numpy.ndarray
'''
def generar_secuencia_numerica(minimo, maximo, paso):
    numeros = np.arange(minimo, maximo, paso)
    return numeros
print(generar_secuencia_numerica(0, 10, 2))
print(type(generar_secuencia_numerica(0, 10, 2)))

'''Ejercicio 3
Finanzas personales
Crear una función en Python que realice operaciones con arrays utilizando NumPy para analizar las finanzas personales de un estudiante. La función debe recibir dos arrays: uno con los ingresos mensuales de un estudiante durante un año y otro con sus gastos mensuales. La función debe devolver el balance mensual (ingresos - gastos), la suma total de los ingresos, la suma total de los gastos, y el saldo total (ingresos totales - gastos totales) durante todo el año.
Instrucciones:
Crear la función analizar_finanzas:
La función debe recibir dos arrays de 12 elementos: uno con los ingresos mensuales (ingresos) y otro con los gastos mensuales (gastos).
La función debe realizar las siguientes operaciones:
Balance mensual: Resta los ingresos menos los gastos para cada mes.
Total de ingresos: Suma todos los ingresos del año.
Total de gastos: Suma todos los gastos del año.
Saldo final: Calcula el saldo final del año (total ingresos - total gastos).
La salida debe ser un array con estos 4 resultados:
resultado = [balance_mensual, total_ingresos, total_gastos, saldo_final]
Requisitos:
Debes usar la librería NumPy para hacer las operaciones de forma eficiente.
Los datos de los ingresos y los gastos deben ser positivos (no considerar valores negativos).
Ejemplo de datos de entrada y salida esperada:
Ingresos mensuales: [1500, 1600, 1700, 1650, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
Gastos mensuales: [1000, 1100, 1200, 1150, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
Salida esperada: La salida de la función debe ser un array con los resultados de las operaciones, de la siguiente forma:
resultado = [[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],
    23650,
    17650,
    6000]
Analiza las finanzas personales de un estudiante durante un año. 
Calcula el balance mensual, el total de ingresos, el total de gastos 
y el saldo final.
Args:
ingresos (np.array): Array de ingresos mensuales (12 elementos).
gastos (np.array): Array de gastos mensuales (12 elementos).
Returns:
np.array: Array con el balance mensual, el total de ingresos, el total de gastos y el saldo final.

La función tiene como objetivo calcular el balance mensual, el total de ingresos, el total de gastos y el saldo final de una persona a lo largo de un año.
Pasos principales de la función:
Convertir listas en arrays de numpy: Usamos np.array() para convertir las listas de ingresos y gastos en arrays, lo que nos permite hacer operaciones matemáticas más fácilmente.
Calcular el balance mensual: Restamos los gastos de los ingresos mes a mes. Esto nos da un array con el balance para cada mes.
Calcular el total de ingresos y gastos: Usamos np.sum() para calcular la suma de todos los ingresos y todos los gastos del año.
Calcular el saldo final: Restamos el total de gastos al total de ingresos. Si el saldo es positivo, significa que se ahorró, y si es negativo, se gastó más de lo que se ganó.
Retornar los resultados: Devolvemos una lista con el balance mensual, el total de ingresos, el total de gastos y el saldo final.
Ejemplo:
Ingresos y gastos mensuales:
ingresos = [1500, 1600, 1700, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2500, 2600]
gastos = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2200, 2400]
Balance mensual: La diferencia entre ingresos y gastos cada mes.
Total de ingresos: La suma de todos los ingresos.
Total de gastos: La suma de todos los gastos.
Saldo final: La diferencia entre el total de ingresos y el total de gastos.

Sugerencias:
Usa numpy para manejar arrays y operaciones.
Realiza los cálculos paso a paso para que el código sea claro y fácil de seguir.
Asegúrate de que los resultados sean correctos al verificar con datos reales.
'''
import numpy as np

ingresos_ejemplo = [1500, 1600, 1700, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2500, 2600]
gastos_ejemplo = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2200, 2400]

def analizar_finanzas(ingresos, gastos):
    """
    Analiza las finanzas personales de un estudiante durante un año. 
    Calcula el balance mensual, el total de ingresos, el total de gastos 
    y el saldo final.
    
    Args:
    ingresos (np.array): Array de ingresos mensuales (12 elementos).
    gastos (np.array): Array de gastos mensuales (12 elementos).
    
    Returns:
    np.array: Array con el balance mensual, el total de ingresos, 
              el total de gastos y el saldo final.
    """
    ingresos_np = np.array(ingresos)
    gastos_np = np.array(gastos)
    balanceMensual = ingresos_np - gastos_np
    totalIngresos = np.sum(ingresos_np)
    totalGastos = np.sum(gastos_np)
    saldoFinal = totalIngresos - totalGastos
    resultado = np.array([balanceMensual, totalIngresos, totalGastos, saldoFinal], dtype=object)
    
    return resultado
    
    analisis = analizar_finanzas(ingresos_ejemplo, gastos_ejemplo)
    print("\nResultados del Análisis:")
    print(f"  Balance Mensual: {analisis[0]}") 
    print(f"  Total Ingresos:  {analisis[1]}")
    print(f"  Total Gastos:    {analisis[2]}")
    print(f"  Saldo Final:     {analisis[3]}")

# Solución Gemini, más completa


def analizar_finanzas(ingresos, gastos):
        
    # 1. Convertir listas en arrays de numpy (si no lo son ya)
    #    Esto permite usar operaciones vectorizadas eficientemente.
    ingresos_np = np.array(ingresos)
    gastos_np = np.array(gastos)
    
    # Validación de entradas
    if len(ingresos_np) != 12 or len(gastos_np) != 12:
        raise ValueError("Las listas/arrays de ingresos y gastos deben tener 12 elementos.")
    
    # Requisito: Los datos deben ser positivos (o cero)
    if np.any(ingresos_np < 0):
        raise ValueError("Los ingresos no pueden ser negativos.")
    if np.any(gastos_np < 0):
        raise ValueError("Los gastos no pueden ser negativos.")
        
    # 2. Calcular el balance mensual (operación vectorizada)
    #    Resta los gastos de los ingresos para cada elemento correspondiente.
    balanceMensual = ingresos_np - gastos_np
    
    # 3. Calcular el total de ingresos y gastos
    #    np.sum() suma todos los elementos del array.
    totalIngresos = np.sum(ingresos_np)
    totalGastos = np.sum(gastos_np)
    
    # 4. Calcular el saldo final
    #    La diferencia entre lo ganado y lo gastado en todo el año.
    saldoFinal = totalIngresos - totalGastos
    
    # 5. Retornar los resultados en un array NumPy
    #    Se usa dtype=object porque el primer elemento es un array y los otros son escalares.
    resultado = np.array([balanceMensual, totalIngresos, totalGastos, saldoFinal], dtype=object)
    
    return resultado

# --- Ejemplo de Uso con los datos proporcionados ---
ingresos_ejemplo = [1500, 1600, 1700, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2500, 2600]
gastos_ejemplo = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2200, 2400]

print("--- Analizando Finanzas con Datos de Ejemplo ---")
print(f"Ingresos: {ingresos_ejemplo}")
print(f"Gastos:   {gastos_ejemplo}")

try:
    # Llamamos a la función con los datos de ejemplo
    analisis = analizar_finanzas(ingresos_ejemplo, gastos_ejemplo)

    # Imprimimos los resultados de forma clara para verificar
    print("\nResultados del Análisis:")
    print(f"  Balance Mensual: {analisis[0]}") 
    print(f"  Total Ingresos:  {analisis[1]}")
    print(f"  Total Gastos:    {analisis[2]}")
    print(f"  Saldo Final:     {analisis[3]}")

    # Verificación rápida de los resultados esperados para este ejemplo:
    # Balance Mensual esperado: [500, 500, 500, 450, 400, 400, 400, 400, 400, 400, 300, 200]
    # Total Ingresos esperado: 23950
    # Total Gastos esperado: 19100
    # Saldo Final esperado: 4850

except ValueError as e:
    # Capturamos y mostramos cualquier error de validación
    print(f"\nError durante el análisis: {e}")

print("-" * 40)

# --- Ejemplo con datos aleatorios (como en el archivo original) ---
print("\n--- Analizando Finanzas con Datos Aleatorios ---")
ingresos_aleatorios = np.random.randint(1000, 2500, 12)
gastos_aleatorios = np.random.randint(800, 2200, 12)

print(f"Ingresos Aleatorios: {ingresos_aleatorios}")
print(f"Gastos Aleatorios:   {gastos_aleatorios}")

try:
    analisis_aleatorio = analizar_finanzas(ingresos_aleatorios, gastos_aleatorios)
    print("\nResultados del Análisis (Aleatorio):")
    print(f"  Balance Mensual: {analisis_aleatorio[0]}") 
    print(f"  Total Ingresos:  {analisis_aleatorio[1]}")
    print(f"  Total Gastos:    {analisis_aleatorio[2]}")
    print(f"  Saldo Final:     {analisis_aleatorio[3]}")
except ValueError as e:
    print(f"\nError durante el análisis aleatorio: {e}")