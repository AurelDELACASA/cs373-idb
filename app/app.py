from flask import Flask, render_template, make_response, jsonify, request
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
    session = Session()
    tournaments = clean_multiple(session.query(Tournament).all())
    return jsonify(tournaments = tournaments)

@app.route('/api/tournament/<int:tid>', methods=['GET'])
def return_tournament(tid):
    """
    API route for individual Tournament
    """
    session = Session()
    tournament = clean_single(session.query(Tournament).filter(Tournament.id == tid).one())
    participants = clean_multiple(session.query(Participant).filter(Participant.tournament_id == tid).all())
    tournament['num_participants'] = len(participants)
    return jsonify(tournament = tournament)

@app.route('/api/participants', methods=['GET'])
def return_participants():
    """
    API route for Participants
    """
    session = Session()
    participants = clean_multiple(session.query(Participant).all())
    characters = clean_multiple(session.query(Character).all())
    tournaments = clean_multiple(session.query(Tournament).all())
    c_dict = {d['id']:d['name'] for d in characters}
    t_dict = {d['id']:d['name'] for d in tournaments}

    # Do a manual join on Characters
    for participant in participants:
        participant['main'] = c_dict[participant['main_id']]
        participant['tournament_name'] = t_dict[participant['tournament_id']]
#        participant.pop('main_id', None)
    return jsonify(participants = participants)

@app.route('/api/participant/<int:pid>', methods=['GET'])
def return_participant(pid):
    """
    API route for individual Participant
    """
    session = Session()
    participant = clean_single(session.query(Participant).filter(Participant.id == pid).one())
    main = clean_single(session.query(Character).filter(participant['main_id'] == Character.id).one())
    participant['main'] = main['name']
    participant.pop('main_id', None)
    return jsonify(participant = participant)

@app.route('/api/characters', methods=['GET'])
def return_characters():
    """
    API route for Characters
    """
    session = Session()
    characters = clean_multiple(session.query(Character).all())
    for character in characters:
        character['weight'] = int(character['weight'])
        character['debut'] = int(character['debut'])
    return jsonify(characters = characters)

@app.route('/api/character/<int:cid>', methods=['GET'])
def return_character(cid):
    """
    API route for individual Character
    """
    session = Session()
    character = clean_single(session.query(Character).filter(Character.id == cid).one())
    return jsonify(character = character)

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

@app.route('/api/lake', methods=['GET'])
def search_db():
    """
    API route of all database data. Used for searching in the database
    """

    session = Session()
    participants = clean_multiple(session.query(Participant).all())
    characters = clean_multiple(session.query(Character).all())
    tournaments = clean_multiple(session.query(Tournament).all())
    for t in tournaments:
        participants.append(t)
    for c in characters:
        participants.append(c)

    finalResults = participants

    return jsonify(results = finalResults)




def clean_multiple(result_set):
    return_set = list()
    for entity in result_set:
        return_set.append(clean_single(entity))
    return return_set

def clean_single(result_set):
    entity_dict = result_set.__dict__.copy()
    entity_dict.pop("_sa_instance_state")
    return entity_dict






# search = str(request.args.get('query'))
#     count = int(request.args.get('limit'))

#     andSearch = search.lower().replace(" ","+") + ':*'
#     orSearch = search.lower().replace(" ","|") + ':*'
    
#     andResults = get_results(andSearch, count, "and")
#     orResults = get_results(orSearch, count, "or")

#     finalResults = andResults
#     l = [result["link"] for result in finalResults]
#     for r in orResults:
#         if r["link"] not in links:
#             finalResults.append(r)

#     return jsonify(results = finalResults)






def get_search_results(sQuery, count, sType):
    results = []

    session = Session()
    particpantQuery = clean_multiple(session.query(Participants).filter(func.to_tsvector(func.lower(Participants.title)).match(sQuery)).limit(count).all())
    tournamentQuery = clean_multiple(session.query(Tournaments).filter(func.to_tsvector(func.lower(Tournaments.title)).match(sQuery)).limit(count).all())
    characterQuery = clean_multiple(session.query(Characters).filter(func.to_tsvector(func.lower(Characters.title)).match(sQuery)).limit(count).all())

    for participant in participantQuery:
        result = {}
        result["title"] = cuisine.title
        result["image"] = cuisine.imageUrl
        result["link"] = "/cuisines/" + str(cuisine.id)
        result["type"] = "Cuisine"
        result["searchType"] = sType
        results.append(result)

    for tournament in tournamentQuery:
        result = {}
        result["title"] = recipe.title
        result["image"] = recipe.imageURL
        result["link"] = "/recipes/" + str(recipe.id)
        result["type"] = "Recipe"
        result["searchType"] = sType
        results.append(result)

    for character in characterQuery:
        result = {}
        result["title"] = ingredient.title
        result["image"] = ingredient.imageURL
        result["link"] = "/ingredients/" + str(ingredient.id)
        result["type"] = "Ingredient"
        result["searchType"] = sType
        results.append(result)

    results = sorted(results, key=lambda k : len(k["title"]))[:count]

    return results

if __name__ == "__main__":
    session = Session()

    characters = session.query(Character).all()
    participants = session.query(Participant).all()
    tournaments = session.query(Tournament).all()

    print("\n")
    print("Count Characters: " + str(len(characters)))
    print("Count Participants: " + str(len(participants)))
    print("Count Tournaments: " + str(len(tournaments)))
    print("\n")
    #app.run(debug=True, host='0.0.0.0')
    app.run()
