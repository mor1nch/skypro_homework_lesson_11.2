import json


# загрузка и возврат json файла
def load_candidates():
    with open("candidates.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# возвращение кандидата по id
def get_candidate(candidate_id):
    data = load_candidates()
    for i in data:
        if i["id"] == candidate_id:
            return i


# возвращение кандидатов по name
def get_candidates_by_name(candidate_name):
    candidates = []
    data = load_candidates()
    for i in data:
        if i["name"] == candidate_name:
            candidates.append(i)
    return candidates


# возвращение кандидата по skill
def get_by_skill(skill_name):
    candidates = []
    data = load_candidates()
    for i in data:
        if skill_name.lower() in i["skills"].lower():
            candidates.append(i)
    return candidates
