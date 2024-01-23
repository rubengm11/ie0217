squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares) # Imprime true

print(2 not in squares) # imprime true

# 49 no es una key, por lo tanto imprime false
print(49 in squares)

# recorrer un diccionario con for
for i in squares:
    print(squares[i])