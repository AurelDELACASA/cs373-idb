from flask import Flask, render_template, make_response, jsonify
from models import Tournament, Participant, Character
import os

app = Flask(__name__)

# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def splash(path):
    return make_response(open(os.path.join(os.path.dirname(__file__), "templates/index.html")).read())

@app.route('/api/tournaments', methods=['GET'])
def return_tournaments():
    t1 = Tournament("name1", "01/02/03", "California", 195, "/some/tpath1")
    t2 = Tournament("name2", "04/05/06", "Texas", 30, "/some/tpath2")
    t3 = Tournament("name3", "07/08/09", "New York", 195, "/some/tpath3")
    result_set = [t1, t2, t3]
    tournaments = [tournament.__dict__ for tournament in result_set]
    return jsonify(tournaments = tournaments)

@app.route('/api/tournament/<name>', methods=['GET'])
def return_tournament(name):
    t1 = Tournament("name1", "01/02/03", "California", 195, "/some/tpath1")
    return jsonify(tournament = t1.__dict__)

@app.route('/api/participants', methods=['GET'])
def return_participants():
    p1 = Participant("Mang0", "/some/ppath1", "Joseph", "Mario", "Canada")
    p2 = Participant("Friberg", "/some/ppath2", "Dave", "Samus", "Ohio")
    p3 = Participant("summit1g", "/some/ppath3", "Steve", "Link", "Florida")
    result_set = [p1, p2, p3]
    participants = [participant.__dict__ for participant in result_set]
    return jsonify(participants = participants)

@app.route('/api/participant/<name>', methods=['GET'])
def return_participant(name):
    p1 = Participant("Mang0", "/some/ppath1", "Joseph", "Mario", "Canada")
    return jsonify(participant = p1.__dict__)

@app.route('/api/characters', methods=['GET'])
def return_characters():
    c1 = Character("Mario", "Super Mario Borthers", 100, ["Dunk", "Back Throw", "Cape"], 1999)
    c2 = Character("Link", "The Legend of Zelda", 104, ["Hook Shot", "Boomerang", "Bombs"], 1986)
    c3 = Character("Samus", "Metroid", 110, ["Energy Ball", "Missiles", "Screw Attack"], 1986)
    result_set = [c1, c2, c3]
    characters = [character.__dict__ for character in result_set]
    return jsonify(characters = characters)

@app.route('/api/character/<name>', methods=['GET'])
def return_character(name):
    c1 = Character("Mario", "super Mario Borthers", 100, ["Dunk", "Back Throw", "Cape"], 1999)
    return jsonify(character = c1.__dict__)


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=80)
    app.run(debug=True)
