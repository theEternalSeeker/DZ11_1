from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


app = Flask(__name__)
data = load_candidates_from_json('candidates.json')


@app.route('/')
def index():
    return render_template('index.html', candidates=data)

@app.route('/candidate/<int:id>')
def profile(id):
    candidate = get_candidate(id)
    return render_template('profile.html', candidate=candidate)


app.run(debug=True)
