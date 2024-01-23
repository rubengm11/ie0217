import random 
# rand int entre 10 y 20
print(random.randrange(10, 20))

# string random de la lista
list1 = ['a', 'b', 'c', 'd']
print(random.choice(list1))

# revolver la lista
random.shuffle(list1)
print(list1)

print(random.random)

# ingreso a lista
myList = ['C++', 'comer', 'Python', 'Hola', 4]
print(myList[1:3])
print(myList[:])