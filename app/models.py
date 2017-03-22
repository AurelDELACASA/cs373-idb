# import statements for sqlalchemy

class Tournament(self):
    tournament_name = ""
    date = ""
    location = ""
    num_entrants = 0
    imageURL = ""

    def __init__(tournament_name, date, location, num_entrants, imageURL):
        self.tournament_name = tournament_name
        self.date = date
        self.location = location
        self.num_entrants = num_entrants


class Participant(self):
    gamer_tag = ""
    profile_picture = ""
    real_name = ""
    main = None
    location = ""

    def __init__(gamer_tag, profile, main, location):
        self.gamer_tag = gamer_tag
        self.profile_picture = profile_picture
        self.real_name = real_name
        self.main = main
        self.location = location


class Character(self):
    character_name = ""
    universe = ""
    weight = ""
    moves = None
    debut = ""

    def __init__(character_name, universe, weight, moves, debut):
        self.character_name = character_name
        self.universe = universe
        self.weight = weight
        self.moves = moves
        self.debut = debut
