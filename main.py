from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/')
""" Выводим всех кандидатов"""
def all_candidates():
    return get_all()


@app.route('/candidates/<int:pk>')
""" Выводим кандидата по его ID"""
def get_current_candidate(pk):
    return get_by_pk(pk)


@app.route('/skills/<skill_name>')
""" Выводим кандидатов с конкретным навыком"""
def get_candidates_by_skill(skill_name):
    return get_by_skill(skill_name)


if __name__ == "__main__":
    app.run()
