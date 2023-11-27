import json

__data = []
def load_candidates_from_json(path):
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
        return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                "name" : candidate['name'],
                "picture" : candidate['picture'],
                "position" : candidate['position'],
                "gender" : candidate['gender'],
                "age" : candidate['age'],
                "skills" : candidate['skills'],
            }
    return {"unknown":"неизвестный кандидат"}

def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()] #списковое включение (семантичкский сахар)

def get_candidates_by_skill(skill_name):
    pass
