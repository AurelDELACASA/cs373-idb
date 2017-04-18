from flask import Flask, render_template, make_response, jsonify, request
import subprocess
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
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

@app.route('/api/tournament/<int:tid>/participants', methods=['GET'])
def get_participant_list(tid):
    """
    API route for getting participants for a specific tournament
    """
    session = Session()
    participants = clean_multiple(session.query(Participant).filter(Participant.tournament_id == tid).all())
    return jsonify(participants = participants)

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

@app.route('/api/participant/<int:pid>/similar', methods=['GET'])
def get_similar_participants(pid):
    """
    API route for getting all participants with the same name
    """
    session = Session()
    participant = clean_single(session.query(Participant).filter(Participant.id == pid).one())
    participants = clean_multiple(session.query(Participant).filter(Participant.tag == participant['tag']).all())

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

@app.route('/api/character/<int:cid>/participants', methods=['GET'])
def return_participants_for_character(cid):
    """
    API route to get participants that use a character
    """
    session = Session()
    participants = clean_multiple(session.query(Participant).filter(Participant.main_id == cid).all())
    characters = clean_multiple(session.query(Character).all())
    tournaments = clean_multiple(session.query(Tournament).all())
    c_dict = {d['id']:d['name'] for d in characters}
    t_dict = {d['id']:d['name'] for d in tournaments}

    # Do a manual join on Characters
    for participant in participants:
        participant['main'] = c_dict[participant['main_id']]
        participant['tournament_name'] = t_dict[participant['tournament_id']]
    return jsonify(participants = participants)

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

@app.route('/api/search', methods=['GET'])
def search():
    query = str(request.args.get('query'))
    AND_query = query.lower().replace(" ", "+") + ":*"
    OR_query = query.lower().replace(" ", "|") + ":*"

    session = Session()

    participantANDQuery = clean_multiple(session.query(Participant).filter(func.to_tsvector(func.lower(Participant.tag)).match(AND_query)).all())
    tournamentANDQuery = clean_multiple(session.query(Tournament).filter(func.to_tsvector(func.lower(Tournament.name)).match(AND_query)).all())
    characterANDQuery = clean_multiple(session.query(Character).filter(func.to_tsvector(func.lower(Character.name)).match(AND_query)).all())

    participantORQuery = clean_multiple(session.query(Participant).filter(func.to_tsvector(func.lower(Participant.tag)).match(OR_query)).all())
    tournamentORQuery = clean_multiple(session.query(Tournament).filter(func.to_tsvector(func.lower(Tournament.name)).match(OR_query)).all())
    characterORQuery = clean_multiple(session.query(Character).filter(func.to_tsvector(func.lower(Character.name)).match(OR_query)).all())

    pIDs = [x['id'] for x in participantANDQuery]
    tIDs = [x['id'] for x in tournamentANDQuery]
    cIDs = [x['id'] for x in characterANDQuery]

#    print(pIDs)
#    print(tIDs)
#    print(cIDs)

    pFiltered = list()
    tFiltered = list()
    cFiltered = list()

    for participant in participantORQuery:
        if participant['id'] not in pIDs:
            pFiltered.append(participant)

    for tournament in tournamentORQuery:
        if tournament['id'] not in tIDs:
            tFiltered.append(tournament)

    for character in characterORQuery:
        if character['id'] not in cIDs:
            cFiltered.append(character)

    full_results = dict()
    full_results['participantsANDQuery'] = participantANDQuery
    full_results['tournamentsANDQuery'] = tournamentANDQuery
    full_results['charactersANDQuery'] = characterANDQuery

    full_results['participantsORQuery'] = pFiltered
    full_results['tournamentsORQuery'] = tFiltered
    full_results['charactersORQuery'] = cFiltered

    print(full_results)

    return jsonify(results = full_results)


def clean_multiple(result_set):
    return_set = list()
    for entity in result_set:
        return_set.append(clean_single(entity))
    return return_set

def clean_single(result_set):
    entity_dict = result_set.__dict__.copy()
    entity_dict.pop("_sa_instance_state")
    return entity_dict

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
