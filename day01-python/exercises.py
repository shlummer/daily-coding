#List and Dictionary Exercises

""" user = {
    "name": "Alex",
    "age": 21,
    "skills": ["Python", "JavaScript"]
}
print(user["name"])
print(user.get("name"))
print(user.get("country", "unknown"))

user["age"] = 22
print(user["age"])
user["city"] = "Munich"
print(user["city"])
print(user)
print(user.keys())
print(user.values())
print(user.items())
print("country" in user)
print(user["missing"])
print(user.get("missing")) 

users = [
    {
        "name": "Anna",
        "skills": ["Python", "JavaScript"]
    },
    {
        "name": "Max",
        "skills": ["Python", "C++"]
    },
    {
        "name": "Leon",
        "skills": ["Javascript"]
    }
]
print(users[1]["skills"])
users[2]["skills"].append("SQL")
if "Python" in users[2]["skills"]:
    print(True)
else:
    print(False)
print(users)
print(len(users[0]["skills"]))
print(len(users[1]["skills"]))
print(len(users[2]["skills"]))

for key, value in users[0].items():
    print(key, value)
users[0].update({"age": 25, "city": "Berlin"})
print(users[0])

del users[0]["skills"]
print(users[0])
age = users[0].pop("age")
print(age)

for user in users:
    print(user["name"])

print(users[1]["skills"][0])
for user in users:
    if "Python" in user["skills"]:
        print(user["name"])"""

#Set Exercises
"""
skills = {"Python", "JavaScript", "SQL"}
print(skills)
skills.add("Docker")
print(skills)
skills.add("Python")
print(skills)
skills.discard("SQL")
print(skills)

if "Python" in skills:
    print("jit knows python")

team_a = {"Python", "JavaScript", "SQL", "Docker"}
team_b = {"Python", "Rust", "Docker", "AWS"}
print(team_a.intersection(team_b))
print(team_a | team_b)
print(team_a - team_b)
print(team_b - team_a)

team_a = {"Python", "JavaScript", "SQL", "Docker"}
team_b = {"Python", "Rust", "Docker", "AWS"}

print(team_a.intersection(team_b))
print(team_a | team_b)
print(team_a - team_b)
print(team_b - team_a)
if "Python" in team_a:
    print(True)
team_b.add("Git")
print(team_b)
team_b.discard("AWS")
print(team_b)
team_b.add("Python")
print(team_b)
"""

#Comprehension Exercises
"""numbers = [3, 7, 2, 8, 12, 5, 20, 11]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)
jit = [number for number in numbers if number > 10]
print(jit)
jitsquared = [number ** 2 for number in jit]
print(jitsquared)

numbers = [3, 7, 2, 8]
squares = {
    number: number ** 2 for number in numbers
}

languages = [
    "Python",
    "JavaScript",
    "Python",
    "Rust",
    "JavaScript",
    "Go"
]
unique = {language.lower() for language in languages}
print(unique)
"""

#Function Exercises
"""def greet(name):
    return f"Hello {name}"

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
def filter_by_skill(users, skill):
    return [user for user in users if skill in user["skills"]]
def get_top_student(students):
    return max(students, key=lambda student: student["grade"])
def normalize_username(username):
    return username.lower().replace(" ", "_")"""


