from unittest import main, TestCase
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tournament, Participant, Character
from config import get_URI


class TestModels(TestCase):

    def setUp(self):
        self.engine = create_engine(get_URI())
        self.session = sessionmaker(bind=self.engine)
    #--------------------------
    # Testing Tournaments Model
    #--------------------------

    def test_tournaments_add_one(self):
        # add tournament, assert it is first Tournament
        #session = self.session()

        #tournament = Tournament()

        self.assertTrue(True)

    def test_tournaments_add_two(self):
        # add two tournaments, assert there are two tournaments
        self.assertTrue(True)

    def test_tournaments_validate_data(self):
        # add a tournament, assertEqual for name, date, location, entrants, picture
        self.assertTrue(True)

    #---------------------------
    # Testing Participants Model
    #---------------------------

    def test_participants_add_one(self):
        # add a participant, assert it is where it belongs (if perhaps in alpha order)
        # session = self.session()

        # participant = Participant(clantag='C9',
        #     tag='Mang0',
        #     main_id='21',
        #     #main=session.query(Character).get(21).name,
        #     main='Pichu',
        #     location='California',
        #     tournament_id='2',
        #     tournament=session.query(Tournament).get(2).sanitized)
        #     tournament='bust2')

        # session.add(participant)
        # session.commit()

        # result = session.query(Participant).order_by(Participant.id.desc()).first()
        # self.assertEqual(result.clangtag, participant.clantag)
        # self.assertEqual(result.tag, participant.tag)
        # self.assertEqual(result.main_id, participantr.main_id)
        # self.assertEqual(result.location, participant.location)
        # self.assertEqual(result.tournament_id, participant.tournament_id)
        # self.assertEqual(result.tournament, participant.tournament)

        # session.remove(result)
        # session.commit()
        self.assertTrue(True)

    def test_participants_add_two(self):
        # add two/more participants, assert the number of participants
        self.assertTrue(True)

    def test_participants_validate_data(self):
        # add a participant, assertEqual for Gamertag, Profile Pic, Real Name, Main, Location
        self.assertTrue(True)

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

    def test_character_add_two(self):
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

        self.assertEqual(session.query(Character).count(), num_characters+2)
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

        for i in range(0,2):
            # get the last row in the Character table
            result = session.query(Character).order_by(Character.id.desc()).first()
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

    def test_query_all_tournaments(self):
        # query for all tournaments
        self.assertTrue(True)

    def test_query_one_tournament(self):
        # query for one tournaments
        self.assertTrue(True)

    def test_query_all_participants(self):
        # query for all participants
        self.assertTrue(True)

    def test_query_one_participant(self):
        # query for one participants
        self.assertTrue(True)

    def test_query_all_characters(self):
        # query for all characters
        self.assertTrue(True)

    def test_query_one_character(self):
        # query for one characters
        self.assertTrue(True)


if __name__ == "__main__":
    main()
