import math


# def <nombre de la funcion> (argumentos)
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Suma =', sum)


def find_square(num):
    result = num * num
    return result

def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print('El resultado es:', result)


# funcion main que llama a la funcion add_numbers y find_square
def main():
    add_numbers(5,4)
    print(find_square(6))
    print('Square root of 4 is:', math.sqrt(4))
    print('2 elevado a 3 es:', pow(2,3))
    find_sum(2, 5, 6, 7, 8, 76)

# llamada del main
main()