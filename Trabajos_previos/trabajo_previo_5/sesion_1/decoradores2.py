# Definición de la función make_pretty que toma una función func como argumento
def make_pretty(func):
    # Definición de la función interna inner que imprime un mensaje y luego llama a func
    def inner():
        print("I got decorated")
        func()
    # Devuelve la función interna inner
    return inner

# Decoración de la función ordinary usando el decorador make_pretty
@make_pretty
# Definición de la función ordinary
def ordinary():
    print("I am ordinary")

# Llamada a la función ordinary, que ahora ha sido decorada por make_pretty
ordinary()