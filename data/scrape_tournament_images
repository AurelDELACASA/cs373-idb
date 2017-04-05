from bs4 import BeautifulSoup
import requests
import re
import pickle

if __name__ == "__main__":
    base_url = "https://smash.gg/tournaments?per_page=5&filter=%7B%22upcoming%22%3Afalse%2C%22videogameIds%22%3A%221%22%2C%22past%22%3Atrue%7D&page="
    # There are 1514 past tournaments
    # If each page displays 5 tournaments then there are
    # 1514 / 5 = 302 pages + 1 extra for the remaining 1514 % 5 = 4 tournaments
    # So we loop from 1 -> 303 + 1 (since range doesn't include the last iteration)

    tournaments = dict()

    #for page_num in range(1, 10):
    for page_num in range(1, int(1514 / 5) + 1 + 1):
        r = requests.get(base_url + str(page_num))
        soup = BeautifulSoup(r.text, "html.parser")
        for each_div in soup.find_all('div', class_="TournamentCardHeading__title"):
            link = each_div.find_all('a')[0]
            link_href = link['href'].split("/")[2]
            link_text = link.text
            print("\t" + link_href + " " + link_text)
            tournaments[link_text] = link_href
#            print(each_div.find_all('a')['href'])
        print("PAGE: " + str(page_num) + " " + "EXPECTED: " + str(5 * page_num) + " ACTUAL: " + str(len(tournaments.items())))

    pickle.dump(tournaments, open("tournaments.pickle", "wb"))
    print("Done.")
