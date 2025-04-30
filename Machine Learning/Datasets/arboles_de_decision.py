import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

vinos = pd.read_csv('vinos.csv')
vinos.head()

vinos['Wine Type'].unique()
vinos['Wine Type'].value_counts()

X = vinos.drop('Wine Type', axis=1)
y = vinos['Wine Type']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

from sklearn.tree import DecisionTreeClassifier
arbol = DecisionTreeClassifier()
arbol.fit(X_train, y_train)
predicciones = arbol.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,predicciones))
print(confusion_matrix(y_test,predicciones))

