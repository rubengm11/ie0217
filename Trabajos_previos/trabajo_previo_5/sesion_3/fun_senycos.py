import matplotlib.pyplot as plt
import numpy as np

# Crear un arreglo de puntos en el intervalo [0, 2 * π] para el eje X
x = np.linspace(0, 2 * np.pi, 100)

# Calcular los valores de las funciones seno y coseno para cada punto en x
y1 = np.sin(x)
y2 = np.cos(x)

# Graficar las funciones seno y coseno
plt.plot(x, y1, label='Seno')
plt.plot(x, y2, label='Coseno')

# Configurar etiquetas y título del gráfico
plt.xlabel('Ángulo (rad)')
plt.ylabel('Valor')
plt.title('Funciones Seno y Coseno')

# Mostrar la leyenda en el gráfico
plt.legend()

# Mostrar el gráfico
plt.show()
