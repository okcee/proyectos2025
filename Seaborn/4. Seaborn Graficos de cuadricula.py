from matplotlib import pyplot as plt
import seaborn as sns

vuelos = sns.load_dataset('flights') # Cargamos un dataset que viene con la librería para hacer pruebas
print("Los primeros 10 elementos del dataset son: ")
print(vuelos.head(10))
''' Dataset
   year month  passengers
0  1949   Jan         112
1  1949   Feb         118
2  1949   Mar         132
3  1949   Apr         129
4  1949   May         121
5  1949   Jun         135
6  1949   Jul         148
7  1949   Aug         148
8  1949   Sep         136
9  1949   Oct         119
'''

# Seaborn: Gráficos de cuadrícula (grids): PairGrid y FacetGrid
