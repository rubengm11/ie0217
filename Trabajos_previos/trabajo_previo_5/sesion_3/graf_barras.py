import matplotlib.pyplot as plt

# Definir las categorías y los valores asociados
categorias = ['A', 'B', 'C', 'D']
valores = [15, 8, 12, 10]

# Crear un gráfico de barras verticales con colores personalizados
plt.bar(categorias, valores, color='royalblue')

# Configurar etiquetas y título del gráfico
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Verticales')

# Mostrar el gráfico
plt.show()
