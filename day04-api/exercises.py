import requests
user = input("Github Username:")
params = {
    "sort": "updated",
    "per_page": 5
}
try:
    response = requests.get(f"https://api.github.com/users/{user}/repos",
        timeout=10, params=params)
    response.raise_for_status()
    resp_dict = response.json()
    for repo in resp_dict:
        print(f"Repository: {repo['name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Language: {repo['language']}")
        print()

    #print(f"Username: {resp_dict["login"]}\nFollowers: {resp_dict["followers"]}\nFollowing: {resp_dict["following"]}\nPublic repositories: {resp_dict["public_repos"]}")
    
except requests.RequestException as error:
    print("Request failed: ", error)

