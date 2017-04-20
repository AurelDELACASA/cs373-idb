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

news_data = [(0, 'What does bathroom anxiety feel like?'), (0, "Birmingham's Muslims challenge 'jihadi capital' label"), (0, 'DOJ warns companies seeking H-1B visas: Donât discriminate against US citizens'), (0, 'Dems claim votes to block Gorsuch; GOP will override them'), (0, 'Theresa May defends UK ties with Saudi Arabia'), (0, 'Lexi Thompson penalty: Tournament referee not TV viewers should have final say'), (0, 'New H-1B Visa Guidelines Crack Down on Computer Programmer Jobs'), (0, 'Democrats Choose Path on Gorsuch That Could Change Washington'), (0, 'Bloomberg Brackets for a Cause'), (0, 'Fox News, Roger Ailes Hit With Another Sexual-Harassment Suit'), (0, 'Exclusive-Kelly Ayotte: Reports that Neil Gorsuch Dodged Meeting Senate Dems False - Breitbart'), (1, "Q&A: Australia 'not taking its place in the world', former Danish PM says"), (1, "The Gambia's journalists find new freedom of expression"), (1, 'The media should resist far-right populist tendencies'), (1, 'Pushing apps to the edge, Fly.io puts middleware in the cloud'), (1, 'This is what emulated Breath of the Wild looks like at 4K resolution'), (1, 'Hieronymus Bosch action figures are the greatest thing from any dimension'), (1, 'iOS 10.3.1 includes bug fixes and improves the security of your iPhone or iPad'), (1, 'Blast on Russian subway kills 11; 2nd bomb is defused'), (1, "AP EXPLAINS: What is the Senate's 'nuclear option'?"), (1, 'Court orders woman to pay Â£24,500 to private parking company'), (1, 'Student-Debt Overhang Is Pushing Down U.S. Rates, Dudley Says'), (1, 'Panera Is Exploring Possible Sale After Receiving Interest'), (1, 'The Media Is Ignoring the 500-Pound Surveillance Elephant in the Room'), (1, "The battle over Obamacare's most popular program just hit a wall in a key state"), (1, 'AOL and Yahoo plan to call themselves by a new name after the Verizon deal closes: Oath'), (1, 'Joe Biden is giving a major speech in a key presidential primary state'), (1, 'The Senate just cleared the first hurdle in confirming Neil Gorsuch to the Supreme Court'), (1, 'The maker of the EpiPen is being sued under a law thatâs typically used to take on organized crime'), (1, "Sir Vince Cable on post-Brexit trade: 'We are not going to revive the empire'"), (1, "Andrew Lilico: 72% of economists were wrong about Brexit's short-term impact on the UK economy"), (1, 'Polling expert: Brits want May to get a Brexit deal that the EU has already shot down several times'), (1, "A 'grammar vigilante' is secretly correcting street signs in Bristol in the middle of the night"), (2, "'There is no budget': China's multi-billion-dollar bid to dominate world football"), (2, 'Tesla: No algorithm prevents sudden acceleration into fixed objects'), (2, 'Tesla delivers 25,418 vehicles in 2017âs first quarter as EV market grows'), (2, "Luke Shaw: Manchester United defender has 'no excuse' for lacking commitment"), (2, "Hedge Fund Bulls Breathe New Life Into World's Hottest Currency"), (3, 'One Nation co-founder accuses party of abandoning him'), (3, "Donald Trump says US is 'very much behind' Egypt's Sisi"), (3, 'Russiaâs hack of State Department was âhand-to-handâ combat'), (3, 'News of Iraq trip with Kushner mid-air poses security risks'), (3, "Brady's jersey stolen again, this time in fun at Fenway Park"), (3, "Ordnance Survey's 3D digital map of UK offers stunning views"), (3, "Firefighters have higher heart attack risk 'because of heat'"), (3, 'Bit by Bit, Trump Methodically Undoing Obama Policies - Breitbart'), (3, 'Egyptian President Sisi Thanks Trump for Alliance Against âSatanic Ideologyâ of Terrorism - Breitbart'), (3, 'President Donald Trump Donates Part of Salary to Park Service - Breitbart'), (3, 'Report: Guest Speaker Disinvitations Most Common at Wealthiest Schools - Breitbart'), (3, "GOP Rep Gohmert to Trump: Work with Freedom Caucus, We Stood By When Priebus, Ryan 'Abandoned' You - Breitbart"), (3, 'Kushner arrives in Iraq with Joint Chiefs chairman for visit - Breitbart'), (3, 'Only A True Pop Culture Nerd Will Recognize 75% Of These Costumes'), (4, 'At least 11 dead after blast rips through Russian metro train'), (4, 'St Petersburg metro bomb blast kills 10, wounds dozens'), (4, 'Why are human rights workers barred from Gaza?'), (4, 'Fire chief: 3 dead, 4 hurt when boiler explodes in St. Louis'), (4, "St Petersburg metro explosion suspect 'from Central Asia'"), (4, 'Russian media: St. Petersburg explosion was carried out by a suicide bomber'), (5, 'Rockhampton locals tie tinnies to houses for flood getaway'), (5, "Syria's  'moderate rebels' to form a new alliance"), (5, 'Charter wonât have to compete against other ISPs thanks to FCC decision'), (5, 'HTC Viveâs first-ever price drop lasts just one day this week'), (5, 'Seven charged over asylum teen attack in Croydon'), (5, "David Moyes: FA to ask Sunderland boss to explain himself over 'slap' remark"), (5, "Kian Dale: Parents guilty over baby's bath death in Tenbury Wells"), (5, "David Moyes: FA to ask Sunderland boss to explain himself over 'slap' remark"), (5, 'Lexi Thompson: Rickie Fowler wants a stop to TV viewers affecting game'), (5, "Eniola Aluko: England women's boss Sampson sending dangerous message on selection"), (5, "Buffett's Newspaper Group Slashes 289 Jobs"), (5, 'Wells Fargo Told to Rehire Whistle-Blower, Pay $5.4 Million'), (5, 'Can We Guess Your Age Based On Your Favourite MuchMusic VJs?'), (5, "Uber secretly took legal action in arbitration to declare Google's claims against it 'meritless'"), (5, 'Britain is going on a 3-pronged attack to seal important post-Brexit trade talks this week'), (5, "There's a huge problem with China's plans to spend billions conquering football, according to a former FA chief"), (6, "'I am sorry': George Calombaris's restaurant empire underpays staff up to $2.6m"), (6, "Trump welcomes Egypt's Sisi despite human rights concerns"), (6, 'Australian medical innovations being held back by red tape: CSIRO'), (6, "India's sugarcane farmers: A cycle of debt and suicide"), (6, 'Why are African men and women still fleeing to Yemen?'), (6, 'Johanna Konta: Injured and ill British number one to miss Charleston tournament'), (6, 'AP Analysis: Can tough-talking Trump solve North Korea?'), (6, "Brexit and Gibraltar: May laughs off Spain 'war' talk"), (6, 'Trump to Nominate Former Jeb Bush Counsel Carlos MuÃ±iz to U.S. Education Department'), (6, 'Trump: âIf China Is Not Going to Solve North Korea, We Willâ'), (6, "We now have a better idea who's behind 'unmasking' Trump officials' contact with foreign agents â and why"), (6, 'A Trump associate reportedly set up a secret meeting to establish a back-channel between Trump and Moscow'), (6, "Mercedes-Benz reportedly pulls ads following allegations of sexual harassment against Bill O'Reilly"), (6, "For Trump to force China's hand against North Korea, he may need to convince them he's a madman"), (6, 'A Trump associate reportedly set up a secret meeting to establish a back-channel between Trump and Moscow'), (6, 'This robotic surgery is so intricate it can stitch a peeled grape back together'), (7, 'Three family members feared dead in NSW flood tragedy'), (7, "Analysis: What's next for Turkey in Syria?"), (7, 'Fewer missing but more dead as rivers recede in Colombia'), (7, "Bill O'Reilly, ex-Fox chief hit with more sexual allegations"), (7, "Disabled people 'left behind in society' - report"), (7, 'World Anti-Doping Agency figures show 14% rise in doping sanctions'), (7, "Lions in New Zealand: Brian O'Driscoll tips Sam Warburton for captaincy"), (7, 'Chinese Grand Prix: Antonio Giovinazzi replaces Pascal Wehrlein for second race'), (7, 'Alan Shearer - no more twists in Premier League title race'), (7, 'Ex-Google Self-Driving Car Engineer Made More Than $120 Million')]

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
    moves = character['moves']
    move_list = moves.split(',')
    character['b'] = move_list[0]
    character['side_b'] = move_list[1]
    character['down_b'] = move_list[2]
    character['up_b'] = move_list[3]
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

    characters = clean_multiple(session.query(Character).all())
    tournaments = clean_multiple(session.query(Tournament).all())
    c_dict = {d['id']:d['name'] for d in characters}
    t_dict = {d['id']:d['name'] for d in tournaments}

    # Do a manual join on Characters
    for participant in participantANDQuery:
        participant['main'] = c_dict[participant['main_id']]
        participant['tournament_name'] = t_dict[participant['tournament_id']]

    for participant in pFiltered:
        participant['main'] = c_dict[participant['main_id']]
        participant['tournament_name'] = t_dict[participant['tournament_id']]

    full_results = dict()
    full_results['participantsANDQuery'] = participantANDQuery
    full_results['tournamentsANDQuery'] = tournamentANDQuery
    full_results['charactersANDQuery'] = characterANDQuery

    full_results['participantsORQuery'] = pFiltered
    full_results['tournamentsORQuery'] = tFiltered
    full_results['charactersORQuery'] = cFiltered

#    print(full_results)

    return jsonify(results = full_results)

@app.route('/api/news', methods=['GET'])
def get_news():
    results = news_data

    return_set = list()

    for c in range(0, 8):
        curr_dict = dict()
        curr_dict['category'] = str(c)
        all_titles = list()
        for t in results:
            if t[0] == c:
                all_titles.append(t[1])
        curr_dict['titles'] = "\n".join(all_titles)
        return_set.append(curr_dict)

#    print(return_set)

    return jsonify(news = return_set)


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
