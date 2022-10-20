import json


def load_candidates():
    """ Загружаем список кандидатов со всеми их данными из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_all():
    """ Формируем список всех кандидатов"""
    candidates = load_candidates()
    candidate_list = "<pre>"
    for candidate in candidates:
        candidate_list += get_candidate_data(candidate)
    candidate_list += "<pre>"
    return candidate_list


def get_by_pk(pk):
    """ Выбираем кандидата по его ID и формируем ответ"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            candidate_list = f"<img src='{candidate['picture']}'><br><pre>"
            candidate_list += f"{get_candidate_data(candidate)}<pre>"
            return candidate_list
    return "Кандидат не найден"


def get_by_skill(skill_name):
    """ Выбираем кандидатов, имеющих определенный навык и формируем ответ"""
    candidates = load_candidates()
    candidate_list = "<pre>"
    for candidate in candidates:
        skill_list = candidate['skills'].lower().split(', ')
        if skill_name in skill_list:
            candidate_list += get_candidate_data(candidate)
    if candidate_list == "<pre>":
        candidate_list += "Кандидаты не найдены<pre>"
    else:
        candidate_list += "<pre>"
    return candidate_list


def get_candidate_data(candidate):
    """ Формируем строку, содержащую данные кандидата"""
    candidate_list = f"<br>Имя кандидата - {candidate['name']}<br>"
    candidate_list += f"Позиция кандидата - {candidate['position']}<br>"
    candidate_list += f"Навыки через запятую - {candidate['skills']}<br>"
    return candidate_list
print