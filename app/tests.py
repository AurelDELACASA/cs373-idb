from unittest import main, TestCase
from io import StringIO
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
# from models import Tournaments, Participants, Characters


class TestModels(TestCase):

   # def setUp(self):

    def test_tournaments(self):
        # add tournament, assert it is first Tournament
        # add two tournaments, assert there are two tournaments
        # add a tournament, assertEqual for name, date, location, entrants,
        # picture
        self.assertTrue(True)

    def test_participants(self):
        # add a participant, assert it is where it belongs (if perhaps in alpha order)
        # add two/more participants, assert the number of participants
        # add a participant, assertEqual for Gamertag, Profile Pic, Real Name,
        # Main,Location
        self.assertTrue(True)

    def test_characters(self):
        # add a character, assert it is where it belongs (if perhaps in alpha order)
        # add two/more charactesr, assert the number of participants
        # add a character, assertEqual for Name, Universe, Weight, Available
        # moves, debut date
        self.assertTrue(True)

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
