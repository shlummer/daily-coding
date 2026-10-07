import requests

params = {
    "sort": "updated",
    "per_page": 5
}

def get_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return f"Request failed : {error}"

def get_repos(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}/repos", timeout=10, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return f"Request failed : {error}"
        