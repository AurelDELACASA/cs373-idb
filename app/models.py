# import statements for sqlalchemy

class Tournament():
    """
    Class definition for Tournament
    Contains a name, date, location, number of entrants, and path to an image
    """
    tournament_name = ""
    date = ""
    location = ""
    num_entrants = 0
    imageURL = ""

    def __init__(self, tournament_name, date, location, num_entrants, imageURL):
        self.tournament_name = tournament_name
        self.date = date
        self.location = location
        self.num_entrants = num_entrants
        self.imageURL = imageURL


class Participant():
    """
    Class definition for Participant
    Contains a gamer tag, path to a profile picture, real name, main character, and location
    """
    gamer_tag = ""
    profile_picture = ""
    real_name = ""
    main = None
    location = ""

    def __init__(self, gamer_tag, profile_picture, real_name, main, location):
        self.gamer_tag = gamer_tag
        self.profile_picture = profile_picture
        self.real_name = real_name
        self.main = main
        self.location = location


class Character():
    """
    Class definition for Character
    Contains a character name, universe, weight, list of moves, and debut year
    """
    character_name = ""
    universe = ""
    weight = ""
    moves = None
    debut = ""

    def __init__(self, character_name, universe, weight, moves, debut):
        self.character_name = character_name
        self.universe = universe
        self.weight = weight
        self.moves = moves
        self.debut = debut
