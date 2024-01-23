greet = lambda name : print('Hola mundo, nombre:', name)

greet('Ruben')

my_list = [1, 5, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0), my_list))

print(new_list)