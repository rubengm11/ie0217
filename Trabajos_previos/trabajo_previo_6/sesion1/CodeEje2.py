import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

# Generacion de datos
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Division de los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciacion del modelo
modelo = LinearRegression()

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Calculo del coeficiente de determinacion R²
r2 = r2_score(y_test, y_pred)

# Resultados
plt.scatter(X_test, y_test, label='Datos de prueba', color='blue')
plt.plot(X_test, y_pred, label=f'Regresión Lineal (R²={r2:.2f})', color='red')
plt.title('Regresión Lineal y Coeficiente de Determinación R²')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

