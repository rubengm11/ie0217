import matplotlib.pyplot as plt

# Datos para el eje X e Y
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

# Crear el gráfico de línea
plt.plot(x, y, label='Datos de ejemplo')

# Añadir una anotación en el punto (5, 14)
plt.annotate('Valor Máximo', xy=(5, 14), xytext=(3, 16),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Configurar etiquetas y título del gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico con Anotación')

# Mostrar la leyenda en el gráfico
plt.legend()

# Mostrar el gráfico
plt.show()
