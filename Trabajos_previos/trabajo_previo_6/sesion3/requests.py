import requests

# Realizar una solicitud GET a la URL proporcionada
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Imprimir el tipo de la respuesta
print("Tipo:", type(response))

# Imprimir la respuesta
print("Respuesta:", response)
print("Respuesta text:", response.text)
print("Respuesta:", response.__dict__)
