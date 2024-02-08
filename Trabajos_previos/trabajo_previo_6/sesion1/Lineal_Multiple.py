import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generacion de datos
X, y = make_regression(n_samples=100, n_features=3, noise=20, random_state=42)

# Creacion de un DataFrame
df = pd.DataFrame(X, columns=['Tamaño', 'Habitaciones', 'Distancia_Ciudad'])
df['Precio'] = y

# Division de los datos
X_train, X_test, y_train, y_test = train_test_split(
    df[['Tamaño', 'Habitaciones', 'Distancia_Ciudad']], 
    df['Precio'], test_size=0.2, random_state=42
)

# Instanciacion del modelo de regresion lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Impresion de los coeficientes y la intercepcion
print("Coeficientes:", modelo.coef_)
print("Intercepcion:", modelo.intercept_)

# Prediccion en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Visualizacion en graficos
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(X_test['Tamaño'], X_test['Habitaciones'], y_test, c='blue', marker='o', alpha=0.5)
ax1.set_xlabel('Tamaño')
ax1.set_ylabel('Habitaciones')
ax1.set_zlabel('Precio Verdadero')
ax1.set_title('Precio Verdadero vs. Tamaño y Habitaciones')

ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(X_test['Tamaño'], X_test['Habitaciones'], y_pred, c='red', marker='o', alpha=0.5)
ax2.set_xlabel('Tamaño')
ax2.set_ylabel('Habitaciones')
ax2.set_zlabel('Precio Predicho')
ax2.set_title('Precio Predicho vs. Tamaño y Habitaciones')

ax3 = fig.add_subplot(133)
ax3.scatter(y_test, y_pred, c='green', alpha=0.5)
ax3.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2)
ax3.set_xlabel('Precio Verdadero')
ax3.set_ylabel('Precio Predicho')
ax3.set_title('Comparacion de Precio Verdadero y Precio Predicho')

plt.tight_layout()
plt.show()

