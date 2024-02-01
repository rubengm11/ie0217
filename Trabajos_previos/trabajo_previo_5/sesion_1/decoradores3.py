# Definición de la función smart_divide que toma una función func como argumento
def smart_divide(func):
    # Definición de la función interna inner que toma dos argumentos a y b
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        # Verificación si b es cero para evitar la división por cero
        if b == 0:
            print("Whoops! cannot divide")
            return
        # Llamada a la función original func(a, b) si b no es cero
        return func(a, b)
    # Devuelve la función interna inner
    return inner

# Decoración de la función divide usando el decorador smart_divide
@smart_divide
# Definición de la función divide que imprime el resultado de la división
def divide(a, b):
    print(a / b)

# Llamada a la función divide, que ahora ha sido decorada por smart_divide
divide(2, 5)  # Imprime "I am going to divide 2 and 5" y luego imprime el resultado 0.4
divide(2, 0)  # Imprime "I am going to divide 2 and 0" y luego imprime "Whoops! cannot divide"
