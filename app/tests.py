from unittest import main, TestCase
from io import StringIO
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
# from models import Tournaments, Participants, Characters


class TestModels(TestCase):

   # def setUp(self):

    #--------------------------
    # Testing Tournaments Model
    #--------------------------

    def test_tournaments_add_one(self):
        # add tournament, assert it is first Tournament
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

    def test_characters_add_one(self):
        # add a character, assert it is where it belongs (if perhaps in alpha order)

        self.assertTrue(True)

    def test_characters_add_two(self):
        # add two/more charactesr, assert the number of participants
        self.assertTrue(True)

    def test_characters_validate_data(self):
        # add a character, assertEqual for Name, Universe, Weight, Available
        # moves, debut date
        self.assertTrue(True)

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
