numbers = {2, 4, 5, 6, 6, 2, 8}
print(numbers)

# adicion del entero 32 al set
numbers.add(32)
print(numbers)

lenguajes = {'swift', 'Java', 'Python'}
print('Set inicial:', lenguajes)
# eliminar el lenguaje java
removedValue = lenguajes.discard('Java')

print('Set despues de eliminar:', lenguajes)

frutas = {'Manzana', 'Pera', 'Mango'}
for f in frutas:
    print(f)