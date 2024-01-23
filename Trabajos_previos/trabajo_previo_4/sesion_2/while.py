i = 1
n = 5

number = int(input('Ingrese un numero: '))
total = 0

while i <= n:
    print(i)
    i = i+1

while number!=0:
    total += number
    number = int(input('Ingrese un numero: '))

print('Total = ', total)