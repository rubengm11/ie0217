import matplotlib.pyplot as plt

# Datos para el gráfico de barras
categorias = ['A', 'B', 'C', 'D']
valores = [15, 8, 12, 10]

# Datos para el gráfico de líneas
tendencia = [5, 10, 8, 13]

# Crear una figura con dos subgráficos (1 fila, 2 columnas)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Subgráfico 1: Gráfico de barras
axs[0].bar(categorias, valores, color='royalblue')
axs[0].set_title('Gráfico de Barras')

# Subgráfico 2: Gráfico de líneas
axs[1].plot(categorias, tendencia, color='green', marker='o')
axs[1].set_title('Gráfico de Línea')

# Configurar etiquetas de ejes X e Y para ambos subgráficos
for ax in axs:
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar la figura con los dos subgráficos
plt.show()
