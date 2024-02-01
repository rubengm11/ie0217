import matplotlib.pyplot as plt

# Datos para la Serie A
x = [1, 2, 3, 4, 5]
y1 = [10, 12, 5, 8, 14]

# Datos para la Serie B
y2 = [5, 8, 9, 6, 10]

# Crear una figura con dos subtramas (1 fila, 2 columnas)
fig, axs = plt.subplots(1, 2)

# Subtrama 1: Gráfico de la Serie A
axs[0].plot(x, y1, label='Serie A')
axs[0].set_title('Subtrama 1')

# Subtrama 2: Gráfico de la Serie B
axs[1].plot(x, y2, label='Serie B', color='red')
axs[1].set_title('Subtrama 2')

# Configurar etiquetas de ejes X e Y y leyenda para ambas subtramas
for ax in axs:
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.legend()

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar la figura con ambas subtramas
plt.show()