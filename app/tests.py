from unittest import main, TestCase
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tournament, Participant, Character
from config import get_URI
import urllib.request
import json


class TestModels(TestCase):

    def setUp(self):
        self.engine = create_engine(get_URI())
        self.session = sessionmaker(bind=self.engine)
    #--------------------------
    # Testing Tournaments Model
    #--------------------------

    def test_tournaments_add_one(self):
        # add tournament, assert it is first Tournament
        session = self.session()

        tournament = Tournament(name='Smash Broski',
                                sanitized='smash-broski',
                                date='April 1, 2017',
                                location='MA',
                                image_path='path_to_image')

        session.add(tournament)
        session.commit()

        result = session.query(Tournament).order_by(
            Tournament.id.desc()).first()
        self.assertEqual(result.name, tournament.name)
        self.assertEqual(result.sanitized, tournament.sanitized)
        self.assertEqual(result.date, tournament.date)
        self.assertEqual(result.location, tournament.location)
        self.assertEqual(result.image_path, tournament.image_path)

        session.delete(tournament)
        session.commit()

    def test_tournaments_add_two_count(self):
        # add two tournaments, assert there are two tournaments
        session = self.session()
        num_tournaments = session.query(Tournament).count()

        tournament_one = Tournament(name='bust2',
                                    sanitized='bust2',
                                    date='April 11th, 2015',
                                    location='CA',
                                    image_path='https://images.smash.gg/images/tournament/1035/image-10e39229043ff962dd367a516b0bc090.png')

        tournament_two = Tournament(name='Smash Broski',
                                    sanitized='smash-broski',
                                    date='April 1, 2017',
                                    location='MA',
                                    image_path='path_to_image')

        session.add(tournament_one)
        session.add(tournament_two)
        session.commit()

        self.assertEqual(session.query(
            Tournament).count(), num_tournaments + 2)

        session.delete(tournament_one)
        session.delete(tournament_two)
        session.commit()

    def test_tournaments_add_two_validate_data(self):
        # add two tournaments, assertEqual for name, date, location, entrants,
        # picture
        session = self.session()
        num_tournaments = session.query(Tournament).count()

        tournament_one = Tournament(name='bust2',
                                    sanitized='bust2',
                                    date='April 11th, 2015',
                                    location='CA',
                                    image_path='https://images.smash.gg/images/tournament/1035/image-10e39229043ff962dd367a516b0bc090.png')

        tournament_two = Tournament(name='Smash Broski',
                                    sanitized='smash-broski',
                                    date='April 1, 2017',
                                    location='MA',
                                    image_path='path_to_image')

        tournaments = []
        tournaments.append(tournament_one)
        tournaments.append(tournament_two)

        session.add(tournament_two)
        session.add(tournament_one)
        session.commit()

        for i in range(0, 2):
            result = session.query(Tournament).order_by(
                Tournament.id.desc()).first()
            self.assertEqual(result.name, tournaments[i].name)
            self.assertEqual(result.sanitized, tournaments[i].sanitized)
            self.assertEqual(result.date, tournaments[i].date)
            self.assertEqual(result.location, tournaments[i].location)
            self.assertEqual(result.image_path, tournaments[i].image_path)
            session.delete(result)
            session.commit()

    #---------------------------
    # Testing Participants Model
    #---------------------------

    def test_participants_add_one(self):
        # add a participant
        session = self.session()

        character = Character(name='Snorlax',
                              universe='Pokemon',
                              weight='180',
                              moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                              debut='2004',
                              tier='E',
                              image_path='Snorlax.png')

        tournament = Tournament(name='bust2',
                                sanitized='bust2',
                                date='April 11th, 2015',
                                location='CA',
                                image_path='https://images.smash.gg/images/tournament/1035/image-10e39229043ff962dd367a516b0bc090.png')

        participant = Participant(sponsor='C9',
                                  tag='mang0',
                                  main=character,
                                  location='California',
                                  tournament=tournament)

        session.add(character)
        session.add(tournament)
        session.add(participant)
        session.commit()

        result = session.query(Participant).order_by(
            Participant.id.desc()).first()
        self.assertEqual(result.sponsor, participant.sponsor)
        self.assertEqual(result.tag, participant.tag)
        self.assertEqual(result.location, participant.location)
        self.assertEqual(result.tournament, participant.tournament)

        session.delete(result)
        session.delete(tournament)
        session.delete(character)
        session.commit()

    def test_participants_add_two_count(self):
        # add two/more participants, assert the number of participants
        session = self.session()

        num_participants = session.query(Participant).count()
        character_one = Character(name='Snorlax',
                                  universe='Pokemon',
                                  weight='180',
                                  moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                                  debut='2004',
                                  tier='E',
                                  image_path='Snorlax.png')

        character_two = Character(name='Sonic',
                                  universe='Sonic',
                                  weight='95',
                                  moves='Hammer Spin Dash, Burning Spin Dash, Spring Jump, Springing Headbutt',
                                  debut='2013',
                                  tier='A',
                                  image_path='Sonic.png')

        tournament_one = Tournament(name='bust2',
                                    sanitized='bust2',
                                    date='April 11th, 2015',
                                    location='CA',
                                    image_path='https://images.smash.gg/images/tournament/1035/image-10e39229043ff962dd367a516b0bc090.png')

        tournament_two = Tournament(name='Smash Broski',
                                    sanitized='smash-broski',
                                    date='April 1, 2017',
                                    location='MA',
                                    image_path='path_to_image')

        participant_one = Participant(sponsor='C9',
                                      tag='mang0',
                                      main=character_one,
                                      location='California',
                                      tournament=tournament_one)

        participant_two = Participant(sponsor='Selfless',
                                      tag='Broseidon',
                                      main=character_two,
                                      location='Russia',
                                      tournament=tournament_two)

        session.add(character_one)
        session.add(character_two)
        session.add(tournament_one)
        session.add(tournament_two)
        session.add(participant_one)
        session.add(participant_two)
        session.commit()

        self.assertEqual(session.query(Participant).count(),
                         num_participants + 2)

        session.delete(character_one)
        session.delete(character_two)
        session.delete(tournament_one)
        session.delete(tournament_two)
        session.delete(participant_one)
        session.delete(participant_two)
        session.commit()

    def test_participants_add_two_validate_data(self):
        # add a participant, assertEqual for Gamertag, Profile Pic, Real Name,
        # Main, Location
        session = self.session()

        num_participants = session.query(Participant).count()
        character_one = Character(name='Snorlax',
                                  universe='Pokemon',
                                  weight='180',
                                  moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                                  debut='2004',
                                  tier='E',
                                  image_path='Snorlax.png')

        character_two = Character(name='Sonic',
                                  universe='Sonic',
                                  weight='95',
                                  moves='Hammer Spin Dash, Burning Spin Dash, Spring Jump, Springing Headbutt',
                                  debut='2013',
                                  tier='A',
                                  image_path='Sonic.png')

        tournament_one = Tournament(name='bust2',
                                    sanitized='bust2',
                                    date='April 11th, 2015',
                                    location='CA',
                                    image_path='https://images.smash.gg/images/tournament/1035/image-10e39229043ff962dd367a516b0bc090.png')

        tournament_two = Tournament(name='Smash Broski',
                                    sanitized='smash-broski',
                                    date='April 1, 2017',
                                    location='MA',
                                    image_path='path_to_image')

        participant_one = Participant(sponsor='C9',
                                      tag='mang0',
                                      main=character_one,
                                      location='California',
                                      tournament=tournament_one)

        participant_two = Participant(sponsor='Selfless',
                                      tag='Broseidon',
                                      main=character_two,
                                      location='Russia',
                                      tournament=tournament_two)

        participants = []

        participants.append(participant_one)
        participants.append(participant_two)

        session.add(character_one)
        session.add(character_two)
        session.add(tournament_one)
        session.add(tournament_two)
        session.add(participant_two)
        session.add(participant_one)
        session.commit()

        for i in range(0, 2):
            result = session.query(Participant).order_by(
                Participant.id.desc()).first()
            self.assertEqual(result.tag, participants[i].tag)
            self.assertEqual(result.sponsor, participants[i].sponsor)
            self.assertEqual(result.tag, participants[i].tag)
            self.assertEqual(result.main, participants[i].main)
            self.assertEqual(result.location, participants[i].location)
            self.assertEqual(result.tournament, participants[i].tournament)
            session.delete(result)
            session.commit()

        session.delete(character_one)
        session.delete(character_two)
        session.delete(tournament_one)
        session.delete(tournament_two)
        # participants deleted in the loop
        session.commit()

    #-------------------------
    # Testing Characters Model
    #-------------------------

    def test_character_add_one(self):
        # add one character and validate data
        session = self.session()

        character = Character(name='Snorlax',
                              universe='Pokemon',
                              weight='180',
                              moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                              debut='2004',
                              tier='E',
                              image_path='Snorlax.png')
        session.add(character)
        session.commit()

        # get the last row in the Character table
        result = session.query(Character).order_by(Character.id.desc()).first()
        self.assertEqual(result.name, character.name)
        self.assertEqual(result.universe, character.universe)
        self.assertEqual(result.moves, character.moves)
        self.assertEqual(result.debut, character.debut)
        self.assertEqual(result.tier, character.tier)
        self.assertEqual(result.image_path, character.image_path)

        session.delete(result)
        session.commit()

    def test_character_add_two_count(self):
        # add two characters, validate count
        session = self.session()
        num_characters = session.query(Character).count()

        character_one = Character(name='Snorlax',
                                  universe='Pokemon',
                                  weight='180',
                                  moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                                  debut='2004',
                                  tier='E',
                                  image_path='Snorlax.png')

        character_two = Character(name='Sonic',
                                  universe='Sonic',
                                  weight='95',
                                  moves='Hammer Spin Dash, Burning Spin Dash, Spring Jump, Springing Headbutt',
                                  debut='2013',
                                  tier='A',
                                  image_path='Sonic.png')

        session.add(character_one)
        session.add(character_two)
        session.commit()

        self.assertEqual(session.query(Character).count(), num_characters + 2)
        session.delete(character_one)
        session.delete(character_two)
        session.commit()

    def test_character_add_two_validate_data(self):
        # add two characters, validate data
        session = self.session()

        character_one = Character(name='Snorlax',
                                  universe='Pokemon',
                                  weight='180',
                                  moves='Rollout, Belly Drum, Heavy Slam, Yawn',
                                  debut='2004',
                                  tier='E',
                                  image_path='Snorlax.png')

        character_two = Character(name='Sonic',
                                  universe='Sonic',
                                  weight='95',
                                  moves='Hammer Spin Dash, Burning Spin Dash, Spring Jump, Springing Headbutt',
                                  debut='2013',
                                  tier='A',
                                  image_path='Sonic.png')

        characters = []
        characters.append(character_one)
        characters.append(character_two)

        session.add(character_two)
        session.add(character_one)
        session.commit()

        for i in range(0, 2):
            # get the last row in the Character table
            result = session.query(Character).order_by(
                Character.id.desc()).first()
            self.assertEqual(result.name, characters[i].name)
            self.assertEqual(result.universe, characters[i].universe)
            self.assertEqual(result.moves, characters[i].moves)
            self.assertEqual(result.debut, characters[i].debut)
            self.assertEqual(result.tier, characters[i].tier)
            self.assertEqual(result.image_path, characters[i].image_path)
            session.delete(result)
            session.commit()

    #------------------
    # Testing API calls
    #------------------

    def test_query_all_tournaments_count(self):
        # query for all tournaments, validate count
        session = self.session()
        num_tournaments = session.query(Tournament).count()

        url = 'http://smashdb.me/api/tournaments'
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        num_results = len(list(list(result_json.items())[0])[1])

        self.assertEqual(num_tournaments, num_results)

    def test_query_one_tournament(self):
        # query for one tournaments
        tournament_id = '3'  # Hardcoded BUST2's tournament_id
        tournament_json = json.loads("""
            {
                "tournament": {
                    "date": " April 11th, 2015", 
                    "id": 3, 
                    "image_path": "https://images.smash.gg/images/tournament/1037/image-5b136245e78f2d0b22fdef47609f5c34.png", 
                    "location": " MA", 
                    "name": "BUST2", 
                    "num_participants": 222, 
                    "sanitized": "bust2"
                }
            }""")

        url = 'http://smashdb.me/api/tournament/' + tournament_id
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        self.assertEqual(tournament_json, result_json)

    def test_query_all_participants_count(self):
        # query for all participants, validate count
        session = self.session()
        num_participants = session.query(Participant).count()

        url = 'http://smashdb.me/api/participants'
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        num_results = len(list(list(result_json.items())[0])[1])

        self.assertEqual(num_participants, num_results)

    def test_query_one_participant(self):
        # query for one participants
        participant_id = '3'  # Hardcoded Leffen's participant_id
        participant_json = json.loads("""
            {
                "participant": {
                    "id": 3, 
                    "location": "Sweden", 
                    "main": "Falco", 
                    "sponsor": "TSM", 
                    "tag": "Leffen", 
                    "tournament_id": 2
                }
            }""")

        url = 'http://smashdb.me/api/participant/' + participant_id
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        self.assertEqual(participant_json, result_json)

    def test_query_all_characters(self):
        # query for all characters, validate count
        session = self.session()
        num_characters = session.query(Character).count()

        url = 'http://smashdb.me/api/characters'
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        num_results = len(list(list(result_json.items())[0])[1])

        self.assertEqual(num_characters, num_results)

    def test_query_one_character(self):
        # query for one character
        character_id = '2'  # Hardcoded Mario's character_id
        character_json = json.loads("""
            {
                "character": {
                        "debut": "1981",
                        "name": "Mario", 
                        "universe": "Mario", 
                        "id": 2, 
                        "weight": "100", 
                        "tier": "E", 
                        "moves": "Super Jump Punch,Fireball,Mario Tornado,Cape",
                        "image_path": "mario.png"
                }
            }""")

        url = 'http://smashdb.me/api/character/' + character_id
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        result_json = json.loads(response.read().decode(encoding))
        self.assertEqual(character_json, result_json)


if __name__ == "__main__":
    main()
