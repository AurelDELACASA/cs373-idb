# import statements for sqlalchemy

class Tournament():
    """
    Class definition for Tournament
    Contains a name, date, location, number of entrants, and path to an image
    """
    name = ""
    date = ""
    location = ""
    num_entrants = 0
    image_path = ""

    def __init__(self, name, date, location, num_entrants, image_path):
        self.name = name
        self.date = date
        self.location = location
        self.num_entrants = num_entrants
        self.image_path = image_path


class Participant():
    """
    Class definition for Participant
    Contains a gamer tag, path to a profile picture, real name, main character, and location
    """
    name = ""
    tag = ""
    main = None
    location = ""
    image_path = ""

    def __init__(self, name, tag, main, location, image_path):
        self.name = name
        self.tag = tag
        self.main = main
        self.location = location
        self.image_path = image_path


class Character():
    """
    Class definition for Character
    Contains a character name, universe, weight, list of moves, and debut year
    """
    name = ""
    universe = ""
    weight = ""
    moves = None
    debut = ""

    def __init__(self, name, universe, weight, moves, debut, image_path):
        self.name = name
        self.universe = universe
        self.weight = weight
        self.moves = moves
        self.debut = debut
        self.image_path

class Entry():
    """
    Class definition for an Entry
    This class represents a participant's entry into a tournament
    This is represented as a many to many relationship
    which requires an association table with a foriegn key
    into tournament, and a foriegn key into participant
    """
    tournament = None
    participant = None

    def __init__(self, tournament, participant):
        self.tournament = tournament
        self.participant = participant
