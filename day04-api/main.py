import github_api

user = input("GitHub Username: ")
user_data = github_api.get_user(user)
user_repos = github_api.get_repos(user)
stars = 0
print(f"Username: {user_data['login']}")
print(f"Followers: {user_data['followers']}")
print(f"Following: {user_data['following']}")
print(f"Public Repositories: {user_data['public_repos']}\n")

for repo in user_repos:
    print(f"Repository: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Language: {repo['language']}")
    stars += repo['stargazers_count']
    print()

most_starred = max(user_repos, key=lambda repo: repo['stargazers_count'])

print("Total stars: ", stars)
print("Most starred repository:", most_starred['name'])
print("Stars:", most_starred['stargazers_count'])