# Diccionario con capitales
capital_city = {'Nepal': 'Kathmandu', 'Italia' : 'Roma', 'Inglaterra' : 'London'}
print(capital_city)

# Se imprime la capital asociada a Nepal
print(capital_city['Nepal'])

capital_city["Japon"] = "Tokyo"

print("Diccionario actualizado:", capital_city)


# ejemplo de estudiantes
student_id = {111 : "Eric", 112 : "Kyle", 113 : "Butters"}

print("Diccionario inicial:", student_id)

# se elimina el item con el codigo 111
del student_id[111]

print("Diccionario actualizado:", student_id)