from bs4 import BeautifulSoup
import requests
import re
import pickle

if __name__ == "__main__":
    base_url = "https://www.ssbwiki.com"

    names = ["Mario_","Luigi_","Yoshi_","Donkey_Kong_","Link_","Samus_","Kirby_","Fox_","Pikachu_","Captain_Falcon_","Ness_",
    "Peach_","Bowser_","Dr._Mario_","Zelda_","Sheik_","Ganondorf_","Young_Link_","Falco_","Mewtwo_","Pichu_","Ice_Climbers_","Marth_",
    "Roy_","Mr._Game_%26_Watch_"]

    names2 = ["Mario_"]

    movesets = dict()

    for character in names2:
        r = requests.get(base_url + "/" + character + "(SSBM)")
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', {"class" : "wikitable"})
        for th in table('tr'):
            move_type = th.find_all('th')
            print(move_type)
        for tr in table('tr'):
            tds = tr.find_all('td')
            
        # for elem in tds:
        #         print(elem)
            

    # pickle.dump(tournaments, open("tournaments.pickle", "wb"))
    print("Done.")