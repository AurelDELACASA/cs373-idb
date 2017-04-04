import pickle
import wget

tournaments = pickle.load(open("tournaments.pickle", "rb"))
base_dir = "tournament_images/"
for tournament in tournaments:
    if tournament[4]:
        wget.download(tournament[4], out=base_dir + tournament[1] + ".png")
