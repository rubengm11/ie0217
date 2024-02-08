import requests

try:
    response = requests.get('https://ejemplo.com/pagina-inexistente')

    response.raise_for_status()

    # Imprimir el contenido de la respuesta si la solicitud fue exitosa
    print(response.text)

except requests.exceptions.HTTPError as err:
    # Manejar errores HTTP, imprime el mensaje de error
    print(f"Error HTTP: {err}")
