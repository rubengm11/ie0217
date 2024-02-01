try:
    numerator = 10
    denominator = 0

    # Intenta realizar la división
    result = numerator / denominator

    # Si la división es exitosa, imprime el resultado
    print(result)

except ZeroDivisionError:
    # Si hay un error de división por cero, imprime un mensaje de error
    print("Error: El denominador no puede ser 0.")

finally:
    # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
    print("Este es el bloque de finalización")