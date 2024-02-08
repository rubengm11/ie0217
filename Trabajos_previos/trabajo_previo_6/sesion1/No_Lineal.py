import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

np.random.seed(42) 
X = 2 * np.random.rand(100, 1)
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)  

# Visualizacion de los datos de regresion no lineal
plt.scatter(X, y)
plt.title('Datos de Regresion No Lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

grado_polinomio = 2  
# Creacion del modelo polinomico
modelo_polinomico = make_pipeline(PolynomialFeatures(grado_polinomio), LinearRegression())
modelo_polinomico.fit(X, y) 

# Predicciones del modelo polinomico
X_test = np.linspace(0, 2, 100).reshape(100, 1) 
y_pred = modelo_polinomico.predict(X_test)  

# Visualizacion de la regresion polinomica
plt.scatter(X, y)
plt.plot(X_test, y_pred, color='red', label=f'Regresion Polinomica ({grado_polinomio} grado)')
plt.title('Regresion Polinomica')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

