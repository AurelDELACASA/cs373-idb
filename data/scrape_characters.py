from bs4 import BeautifulSoup
import requests
import re
import pickle
import sys
import string

if __name__ == "__main__":
    base_url = "https://www.ssbwiki.com"

    names = ["Mario_","Luigi_","Yoshi_","Donkey_Kong_","Link_",
    "Samus_","Kirby_","Fox_","Pikachu_","Captain_Falcon_","Ness_",
    "Peach_","Bowser_","Dr._Mario_","Zelda_","Sheik_","Ganondorf_",
    "Young_Link_","Falco_","Mewtwo_","Pichu_","Ice_Climbers_",
    "Marth_","Roy_","Mr._Game_%26_Watch_"]

    movetypes = dict()
    movenames = dict()
    universes = dict()
    tiers = dict()
    weights = dict()
    debuts = dict()
    for character in names:
        move_names = [0] * 60

        # Grabbing Move types
        r = requests.get(base_url + "/" + character + "(SSBM)")
        soup = BeautifulSoup(r.text, "html.parser")

        character = character[:len(character) - 1].replace("_", " ").strip().replace("%26", "&")

        table = soup.find('table', {"class" : "wikitable"})

        # Grabbing Move names
        index = 0
        for tr in table('tr'):
            td_list = tr.find_all('td')
            if len(td_list) > 0:
                t2 = td_list[0]
                text = t2.find(text=True)
                if text == None or text == "":
                    text = " "
                if text[0].isalpha() or text == " ":
                    move_names[index] = text
                    index += 1
        move_names = [x for x in move_names if x != 0]
        move_names = [x for x in move_names if x != ' ']
        move_names = list(set(move_names))
        movenames[character] = move_names

        # Grabbing Tiers
        table = soup.find('table', {"class" : "infobox bordered"})
        for tr in table('tr'):
            td_list = tr.find_all('td')
            for t3 in td_list:
                text = t3.find(text=True)
                if ("(" in text):
                    tier = text[:1]
                    tiers[character] = tier

        # Grabbing Universes
        table = soup.find('table', {"class" : "infobox bordered"})
        for tr in table('tr'):
            td = tr.find('td', {"width" : "55%"})
            if td != None:
                text = td.find(text=True)
                universes[character] = text

    # Grabbing Weights
    r = requests.get(base_url + "/Weight")
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('caption')
    text = tables[3]
    table = text.find_parent()
    for tr in table('tr'):
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            t4 = td_list[1]
            t5 = td_list[2]
            character = t4.find(text=True)
            weight = t5.find(text=True)
            weights[character] = weight

    # Grabbing Debuts
    for name in names:
        index = 0

        # Grabbing Move types
        r = requests.get(base_url + "/" + name)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', {"class" : "infobox bordered"})
        for tr in table('tr'):
            td_list = tr.find_all('td')
            if len(td_list) > 1:
                t6 = td_list[0]
                head = t6.find(text=True)
                t7 = td_list[1]

                text = t7.findAll(text=True)
                if len(text) == 2 and head == "Debut":
                    debut = text[1]
                    debut = debut[1:]
                    debuts[name] = debut

    debuts_hardcoded = {'Pikachu':"1996", 'Mewtwo':"1996", 'Pichu':"1996", 'Ganondorf':"1986", 'Marth':"1990", 'Roy':"2001"}
    characters = list()
    for k in names:
        name = k[:len(k) - 1].replace("_", " ").strip().replace("%26", "&")
        universe = str(universes[name])
        weight = str(weights[name].strip())
        moves = str(",".join(movenames[name]))
        debut = debuts_hardcoded[name] if name in debuts_hardcoded else str(debuts[k].strip()[1:-1])
        tier = str(tiers[name])
        image_path = str(name.lower().replace(" ", "_").replace(".", "").replace("_&", "") + ".png")
        c = tuple([name, universe, weight, moves, debut, tier, image_path])
        characters.append(c)

    pickle.dump(characters, open("characters.pickle", "wb"))

    print("Done.")
