def add_member(team: list[dict], name: str, skills: list[str]) -> None:
    team.append({
        "name": name,
        "skills": skills
    })


def add_skill(team: list[dict], name: str, skill: str) -> None:
    for member in team:
        if member["name"] == name:
            existing_skills = [s.lower() for s in member["skills"]]

            if skill.lower() not in existing_skills:
                member["skills"].append(skill)

            return


def find_by_skill(team: list[dict], skill: str) -> list[str]:
    return [
        member["name"]
        for member in team
        if skill.lower() in [s.lower() for s in member["skills"]]
    ]


def shared_skills(team: list[dict], name1: str, name2: str) -> set[str]:
    skills1 = set()
    skills2 = set()

    for member in team:
        if member["name"] == name1:
            skills1 = set(member["skills"])

        if member["name"] == name2:
            skills2 = set(member["skills"])

    return skills1.intersection(skills2)


def all_teams_skills(team: list[dict]) -> set[str]:
    all_skills = set()

    for member in team:
        all_skills.update(member["skills"])

    return all_skills


def missing_skills(team: list[dict], required_skills: set[str]) -> set[str]:
    team_skills = all_teams_skills(team)
    return required_skills - team_skills


def most_skilled_member(team: list[dict]) -> dict | None:
    if not team:
        return None

    return max(team, key=lambda member: len(member["skills"]))


def team_summary(team: list[dict]) -> str:
    lines = []

    for index, member in enumerate(team, start=1):
        skills = ", ".join(member["skills"])

        lines.append(
            f"{index}. {member['name']}\n"
            f"   Skills: {skills}"
        )

    return "\n\n".join(lines)