# Definición de un decorador llamado 'star'
def star(func):
    # Definición de la función interna 'inner' que toma cualquier número de argumentos posicionales (*args) y argumentos de palabras clave (**kwargs)
    def inner(*args, **kwargs):
        print("*" * 15)  # Imprime 15 asteriscos
        func(*args, **kwargs)  # Llama a la función original con los mismos argumentos
        print("*" * 15)  # Imprime 15 asteriscos después de que la función original se haya ejecutado
    # Devuelve la función interna 'inner'
    return inner

# Definición de otro decorador llamado 'percent'
def percent(func):
    # Definición de la función interna 'inner' similar a la anterior, que imprime 15 porcentajes antes y después de llamar a la función original
    def inner(*args, **kwargs):
        print("%" * 15)  # Imprime 15 porcentajes
        func(*args, **kwargs)  # Llama a la función original con los mismos argumentos
        print("%" * 15)  # Imprime 15 porcentajes después de que la función original se haya ejecutado
    # Devuelve la función interna 'inner'
    return inner

# Uso de múltiples decoradores, primero 'percent' y luego 'star'
@star
@percent
# Definición de la función 'printer', que simplemente imprime el mensaje que recibe
def printer(msg):
    print(msg)

# Llamada a la función decorada 'printer'
printer("Hello")
