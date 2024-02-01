class InvalidAgeException(Exception):
    pass 


number = 18

try:
    input_num = int(input("Ingrese un numero"))
    if input_num<number:
        raise InvalidAgeException
    else:
        print("Mayor de edad")

except InvalidAgeException:
    print("Edad menor a 18")
