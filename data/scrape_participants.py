import requests
import pickle
import json

if __name__ == "__main__":
    # Load the tournaments
    tournaments = pickle.load(open("tournaments.pickle", "rb"))
    ids = list(tournaments.values())
    print(ids)

    base_url = "https://api.smash.gg/tournament/replace/event/melee-singles?expand[]=groups&expand[]=entrants"

    participants = list()

    for i,t in enumerate(ids):
        url = base_url.replace("replace", t)
        print("TOURNAMENT: " + str(i) + " " + url)
        json_obj = json.loads(requests.get(url).text)
#        print(json_obj['entities']['entrants'])
        try:
            for player in json_obj['entities']['entrants']:
#                assert len(player['participantIds']) == 1
                pid = str(player['participantIds'][0])
                name = str(player['name'])
                participants.append(tuple([t, pid, name]))
                print(participants[-1])
        except:
            pass

    pickle.dump(participants, open("participants.pickle", "wb"))
    print("Done.")

