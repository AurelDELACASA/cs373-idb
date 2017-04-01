from sqlalchemy import Table, Column
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/

Base = declarative_base()

class Tournament(Base):
    """
    Class definition for Tournament
    Contains a name, date, location, number of entrants, and path to an image
    """

    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    num_entrants = Column(Integer)
    image_path = Column(String(255), nullable=False)

#    def __init__(self, name, date, location, num_entrants, image_path):
#        self.name = name
#        self.date = date
#        self.location = location
#        self.num_entrants = num_entrants
#        self.image_path = image_path


class Character():
    """
    Class definition for Character
    Contains a character name, universe, weight, list of moves, and debut year
    """

    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    universe = Column(String(255), nullable=False)
    weight = Column(Integer)
    moves = Column(String(255), nullable=False)
    debut = Column(Integer)

#    def __init__(self, name, universe, weight, moves, debut, image_path):
#        self.name = name
#        self.universe = universe
#        self.weight = weight
#        self.moves = moves
#        self.debut = debut
#        self.image_path


class Participant():
    """
    Class definition for Participant
    Contains a gamer tag, path to a profile picture, real name, main character, and location
    """

    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    tag = Column(String(255), nullable=False)
    main_id = Column(Integer, ForeignKey('characters.id'))
    main = relationship(Character)
    location = Column(String(255), nullable=False)
    image_path = Column(String(255), nullable=False)

#    def __init__(self, name, tag, main, location, image_path):
#        self.name = name
#        self.tag = tag
#        self.main = main
#        self.location = location
#        self.image_path = image_path

class Entry():
    """
    Class definition for an Entry
    This class represents a participant's entry into a tournament
    This is represented as a many to many relationship
    which requires an association table with a foriegn key
    into tournament, and a foriegn key into participant
    """
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    participant_id = Column(Integer, ForeignKey('participants.id'))

    tournament = relationship(Tournament)
    participant = relationship(Participant)

    def __init__(self, tournament, participant):
        self.tournament = tournament
        self.participant = participant
