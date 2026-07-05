import requests

def get_user_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()