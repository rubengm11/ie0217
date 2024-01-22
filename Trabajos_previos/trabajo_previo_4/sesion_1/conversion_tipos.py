#conversion implicita

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value:", new_number)
print("Data type:", type(new_number))

#conversion explicita

num_string = '12'
num_integer = 23

print("Tipo antes de la conversion: ", type(num_string))

num_string = int(num_string)

print("Tipo despues de la conversion: ", type(num_string))

num_sum = num_integer + num_string

print(num_sum)

