from flask import Flask, render_template, make_response, jsonify
import subprocess
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Tournament, Participant, Character
from config import get_URI
import os

IMAGE_ROOT_PATH = "/static/images/"

TOURNAMENT_PATH_PREFIX = "tournaments/"
PARTICIPANT_PATH_PREFIX = "participants/"
CHARACTER_PATH_PREFIX = "characters/"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_URI()
print("Using URI: " + get_URI())
engine = create_engine(get_URI())
Session = sessionmaker(bind = engine)

# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def splash(path):
    """
    Route for generic path
    """
    return make_response(open(os.path.join(os.path.dirname(__file__), "templates/index.html")).read())

@app.route('/api/tournaments', methods=['GET'])
def return_tournaments():
    """
    API route for Tournaments
    """
    t1 = Tournament("name1", "01/02/03", "California", 195, "/static/images/bracketIcon.png")
    t2 = Tournament("name2", "04/05/06", "Texas", 30, "/some/tpath2")
    t3 = Tournament("name3", "07/08/09", "New York", 195, "/some/tpath3")
    result_set = [t1, t2, t3]
    tournaments = [tournament.__dict__ for tournament in result_set]
    return jsonify(tournaments = tournaments)

@app.route('/api/tournament/<name>', methods=['GET'])
def return_tournament(name):
    """
    API route for individual Tournament
    """
    t1 = Tournament("name1", "01/02/03", "California", 195, "/static/images/bracketIcon.png")
    return jsonify(tournament = t1.__dict__)

@app.route('/api/participants', methods=['GET'])
def return_participants():
    """
    API route for Participants
    """
    p1 = Participant("Mang0", "/static/images/mango.png", "Joseph", "Mario", "Canada")
    p2 = Participant("Friberg", "/some/ppath2", "Dave", "Samus", "Ohio")
    p3 = Participant("summit1g", "/some/ppath3", "Steve", "Link", "Florida")
    result_set = [p1, p2, p3]
    participants = [participant.__dict__ for participant in result_set]
    return jsonify(participants = participants)

@app.route('/api/participant/<name>', methods=['GET'])
def return_participant(name):
    """
    API route for individual Participant
    """
    p1 = Participant("Mang0", "/static/images/mango.png", "Joseph", "Mario", "Canada")
    return jsonify(participant = p1.__dict__)

@app.route('/api/characters', methods=['GET'])
def return_characters():
    """
    API route for Characters
    """
    c1 = Character("Mario", "Super Mario Brothers", 100, ["Dunk", "Back Throw", "Cape"], 1999)
    c2 = Character("Link", "The Legend of Zelda", 104, ["Hook Shot", "Boomerang", "Bombs"], 1986)
    c3 = Character("Samus", "Metroid", 110, ["Energy Ball", "Missiles", "Screw Attack"], 1986)
    result_set = [c1, c2, c3]
    characters = [character.__dict__ for character in result_set]
    return jsonify(characters = characters)

@app.route('/api/character/<name>', methods=['GET'])
def return_character(name):
    """
    API route for individual Character
    """
    c1 = Character("Mario", "Super Mario Brothers", 100, ["Dunk", "Back Throw", "Cape"], 1999)
    return jsonify(character = c1.__dict__)

@app.route('/api/runTests', methods=['GET'])
def run_tests():
    """
    API route for running unit tests
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "tests.py"
    try:
        process = subprocess.check_output(["python", os.path.join(script_dir, rel_path)],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        process = e.output

    return process.decode("utf-8")

if __name__ == "__main__":
    print("Creating session...")
    session = Session()
    print("Making query...")
    result = session.query(Character).all()[0].__dict__
    print(result)
    #app.run(debug=True, host='0.0.0.0')
    app.run()
