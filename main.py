import utils
from flask import Flask, render_template

app = Flask(__name__)


# главная страница
@app.route("/")
def page_main():
    candidates = utils.load_candidates()
    return render_template('list.html', candidates=candidates)


# страница с кандидатом по id
@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = utils.get_candidate(uid)
    if not candidate:
        return 'Кандидат на найден'
    return render_template('single.html', candidate=candidate)


# страница с кандидатом по name
@app.route("/search/<candidate_name>")
def search_candidates_page(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


# страница с кандидатом по skill
@app.route("/skill/<skill_name>")
def search_candidates_by_skill_page(skill_name):
    candidates = utils.get_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run()
