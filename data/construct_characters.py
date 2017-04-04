import pickle
import random

if __name__ == "__main__":
    movetypes = list(dict(pickle.load(open("movetypes.pickle", "rb"))).items())[0][1]

    movenames = dict(pickle.load(open("movenames.pickle", "rb")))
    universes = dict(pickle.load(open("universes.pickle", "rb")))
    tiers = dict(pickle.load(open("tiers.pickle", "rb")))

    characters = list()

    for key in movenames.keys():
        name = key[:len(key) - 1].replace("%26", "&").replace(".", "").replace("_", " ")
        universe = universes[key]
        tier = tiers[key]
        moves = ", ".join(set([x for x in movenames[key] if x != ' ']))
        image_path = key.lower()[:len(key) - 1].replace(".", "") + ".png"

        weight = random.randint(100, 200)
        debut = random.randint(1990, 2000)

        characters.append(tuple([str(name), str(universe), str(weight), str(moves), str(debut), str(tier), str(image_path)]))

    print(characters)
    pickle.dump(characters, open("characters.pickle", "wb"))
    print("Done.")
