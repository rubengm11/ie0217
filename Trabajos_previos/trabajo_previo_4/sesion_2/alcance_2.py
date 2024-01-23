def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Antes de llamar a inner_function():", num)
    inner_function()
    print("Despues de llamar a inner_function():", num)

outer_function()
print("Afuera de ambas funciones:", num)