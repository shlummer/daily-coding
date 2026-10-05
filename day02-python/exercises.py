# exception handling
def safe_average(number: list[int])-> float | None:
    try:
        return sum(number) / len(number)
    except ZeroDivisionError:
        return None
def safe_int(value: str)-> int | None:
    try:
        return int(value)
    except ValueError:
        return None
    
# reading and writing
"""with open("learning_log.txt", "w") as file:
    file.write("Day 2\nExceptions\nFiles")
with open("learning_log.txt", "r") as file:
    print(file.read())
with open("learning_log.txt", "a") as file:
    file.write("\njson")
with open("learning_log.txt", "r") as file:
    print(file.read())"""
# json
import json
team = [
    {"name": "Anna", "skills": ["Python"]},
    {"name": "Max", "skills": ["C++"]}
]
with open("team.json", "w") as file:
    json.dump(team, file, indent=4)
with open("team.json", "r") as file:
    loaded_team = json.load(file)
"""print(loaded_team)
print(loaded_team[1]["skills"])"""
#csv
import csv
participants = []
with open("participents.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        """print(row["name"])
        print(row["score"])"""
        participants.append(row)
    top_participant = max(participants,key=lambda participant: int(participant["score"]))
    """print("Highest score: ", top_participant["name"])
    print("Score: ",top_participant["score"])"""
#env
"""import os
from dotenv import load_dotenv

load_dotenv()

usero = os.getenv("USER")
lang = os.getenv("FAV_LANG")

print(usero)
print(lang)"""
