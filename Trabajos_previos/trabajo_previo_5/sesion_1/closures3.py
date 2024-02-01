# Definición de la función make_multiplier_of que toma un argumento n
def make_multiplier_of(n):
    # Definición de la función interna multiplier que multiplica su argumento por n
    def multiplier(x):
        return x * n
    # Devuelve la función interna multiplier
    return multiplier

# Crear una función times3 que multiplica su argumento por 3 usando make_multiplier_of
times3 = make_multiplier_of(3)

# Crear una función times5 que multiplica su argumento por 5 usando make_multiplier_of
times5 = make_multiplier_of(5)

# Imprimir el resultado de times3 con el argumento 9 (3 * 9)
print(times3(9))

# Imprimir el resultado de times5 con el argumento 3 (5 * 3)
print(times5(3))

# Imprimir el resultado de times5 aplicado dos veces sobre el argumento 2 (5 * (5 * 2))
print(times5(times5(2)))
