#Mini Project: Hackathon Team Analyzer
import utils
team = [
    {
        "name": "Anna",
        "skills": ["Python", "JavaScript", "SQL"]
    },
    {
        "name": "Max",
        "skills": ["Python", "Docker", "C++"]
    },
    {
        "name": "Leon",
        "skills": ["JavaScript", "React"]
    }
]
required_skills = {
    "Python",
    "JavaScript",
    "SQL",
    "Git",
    "Docker",
    "React"
}
if __name__ == "__main__":
    print(utils.team_summary(team))
    utils.add_member(team, "Jit", ["Python", "JavaScript"])
    print(utils.team_summary(team))
    print(utils.find_by_skill(team, "Python"))
    print(utils.shared_skills(team, "Anna", "Max"))
    print(utils.all_teams_skills(team))
    print(utils.missing_skills(team, required_skills))
    print(utils.most_skilled_member(team))
    print(utils.team_summary(team))


