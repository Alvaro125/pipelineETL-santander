import requests

from extract import sdw2023_api_url, users
from transform import transform


def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False
def load():
    for user in users:
        success = update_user(user)
        print(f"User {user['name']} updated? {success}!")