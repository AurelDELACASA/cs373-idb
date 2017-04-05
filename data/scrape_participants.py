import requests
import pickle
import json
from bs4 import BeautifulSoup

def isascii(c):
    return ord(c) < 128

def sanitize_clantag(clantag):
    clantag2 = clantag.replace(" ", "")
    for c in clantag2:
#        print(c + " " + str(isascii(c)))
        if not isascii(c):
            return ""
    return clantag

def scrape_pages(tournament_url, total_attendees):
    total_pages = int(total_attendees / 50) + 1 + 1
    tournament_participants = list()
    base_url = "https://smash.gg/tournament/replace/attendees"
    t_url = base_url.replace("replace", tournament_url)
    for page in range(1, total_pages + 1):
        url = t_url + "?per_page=50&filter={}&page=" + str(page)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
#         participants = soup.find_all('div', class_="gamertag-title-lg gamertag-title")
#         for part in participants:
#             text = part.find_all(text=True)
#             if len(text) == 4:
#                 clantag = str(text[0])
#                 tag = str(text[2])
#             else:
#                 clantag = ""
#                 tag = str(text[1])
        rows = soup.find_all('tr', class_="clickable-row")
        for row in rows:
            td_list = row.find_all('td')

            part = td_list[0]
            text = part.find_all(text=True)
            if len(text) == 4:
                clantag = str(text[0])
                tag = str(text[2])
            else:
                clantag = ""
                tag = str(text[1])

            clantag = sanitize_clantag(clantag)

            loc = td_list[1]
            text = loc.find_all(text=True)
            if len(text) > 0:
                location = text[0]
            else:
                location = ""

            tournament_participants.append(tuple([str(clantag), str(tag), str(location), str(tournament_url)]))
#            print(clantag + " " + tag + " " + str(location))
    return tournament_participants


if __name__ == "__main__":
    # Load the tournaments
#     tournaments = pickle.load(open("tournaments.pickle", "rb"))
#     ids = list(tournaments.values())
#     print(ids)
#
#     base_url = "https://api.smash.gg/tournament/replace/event/melee-singles?expand[]=groups&expand[]=entrants"
#
#     participants = list()
#
#     for i,t in enumerate(ids):
#         url = base_url.replace("replace", t)
#         print("TOURNAMENT: " + str(i) + " " + url)
#         json_obj = json.loads(requests.get(url).text)
# #        print(json_obj['entities']['entrants'])
#         try:
#             for player in json_obj['entities']['entrants']:
# #                assert len(player['participantIds']) == 1
#                 pid = str(player['participantIds'][0])
#                 name = str(player['name'])
#                 participants.append(tuple([t, pid, name]))
#                 print(participants[-1])
#         except:
#             pass
#
#     pickle.dump(participants, open("participants.pickle", "wb"))
#     print("Done.")


    base_url = "https://smash.gg/tournament/replace/attendees"

    tournaments = pickle.load(open("tournaments.pickle", "rb"))
    tournament_participants = list()
    for tournament in tournaments[:5]:
        url = base_url.replace("replace", tournament[1])
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        # http://stackoverflow.com/questions/22726860/beautifulsoup-webscraping-find-all-finding-exact-match
        page_num_div = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['text-center'])
        para = page_num_div[0].find('p', class_="text-muted")
        text = str(para.find_all(text=True)[0])
        total_attendees = int(text.split(" ")[-1])
        tournament_participants += scrape_pages(tournament[1], total_attendees)

#        print(text)

    pickle.dump(tournament_participants, open("participants.pickle", "wb"))
