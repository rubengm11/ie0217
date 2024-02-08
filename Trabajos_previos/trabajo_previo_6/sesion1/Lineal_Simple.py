import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)  
X = 2 * np.random.rand(100, 1)  
y = 4 + 3 * X + np.random.randn(100, 1)  

# Instanciacion del modelo de regresion lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Impresion de coeficiente e intercepcion
print("Coeficiente:", modelo.coef_[0][0])  
print("Intercepcion:", modelo.intercept_[0])  

# Grafico de dispersion y recta de regresion
plt.scatter(X, y) 
plt.plot(X, modelo.predict(X), color='red', linewidth=3)
plt.title('Regresion Lineal')  
plt.xlabel('X')  
plt.ylabel('y')  
plt.show()

