import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding ='utf-8') as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates


def get_candidate(candidate_id):
    pass

def get_candidates_by_name(candidate_name):
    pass

def get_candidates_by_skill(skill_name):
    pass
