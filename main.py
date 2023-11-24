from flask import Flask
import utils

app = Flask(__name__)
candidates = utils.load_candidates_from_json()

@app.route("/")
def page_index():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n"
    str_candidates += '</pre>'
    return str_candidates