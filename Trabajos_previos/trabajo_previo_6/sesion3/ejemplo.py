import requests

# Obtener datos de usuarios desde la API
users_response = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = users_response.json()

# Obtener datos de publicaciones desde la API
posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts_data = posts_response.json()

user_posts = {}

for user in users_data:
    user_posts[user['id']] = []

# Organizar las publicaciones por usuario
for post in posts_data:
    user_id = post.get('userId')
    if user_id in user_posts:
        user_posts[user_id].append({
            'title': post['title'],
            'body': post['body']
        })

# Mostrar las publicaciones por usuario
for user_id, posts in user_posts.items():
    user = next((user for user in users_data if user['id'] == user_id), None)
    if user:
        print(f"\nPublicaciones de {user['name']} ({user['email']}):\n")
        for post in posts:
            print(f"Title: {post['title']}\nBody: {post['body']}\n")
    else:
        print(f"No se encontraron datos para el usuario con ID {user_id}")
