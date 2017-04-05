from bs4 import BeautifulSoup
import requests
import re
import pickle

if __name__ == "__main__":
    base_url = "https://smash.gg/tournaments?per_page=5&filter=%7B%22upcoming%22%3Afalse%2C%22videogameIds%22%3A%221%22%2C%22past%22%3Atrue%7D&page="
    base_url_tournament = "https://smash.gg/tournament/"
    # There are 1514 past tournaments
    # If each page displays 5 tournaments then there are
    # 1514 / 5 = 302 pages + 1 extra for the remaining 1514 % 5 = 4 tournaments
    # So we loop from 1 -> 303 + 1 (since range doesn't include the last iteration)

    tournaments = list()

    for page_num in range(1, 11):
    #for page_num in range(1, int(1514 / 5) + 1 + 1):
        r = requests.get(base_url + str(page_num))
        soup = BeautifulSoup(r.text, "html.parser")
        for each_div in soup.find_all('div', class_="TournamentCardHeading__title"):
            link = each_div.find_all('a')[0]
            link_href = link['href'].split("/")[2]
            link_text = link.text
#            print("\t" + link_href + " " + link_text)
            p = requests.get(base_url_tournament + str(link_href) + "/details")
            soup2 = BeautifulSoup(p.text, "html.parser")

            # find the information div
            info_div = soup2.find_all('div', class_="tournament-info")
            info_div = (info_div[0]).ul
            list_elements = info_div.find_all('li')

            # Find the date and location
            date = str(list_elements[0].text)
            location = str(list_elements[1].text)

            # Find the background image div
            image_div = soup2.find_all('div', class_="PageHeading__placeholder")
            image_div = image_div[0]
            style = str(image_div['style']).replace("background-image:", "").replace(";", "")
            if style == "none":
                image_path = None
            else:
                image_path = style.replace("url(", "").replace(")", "")

#            print(link_text + " " + date + " " + location + " " + str(image_path))
            tournaments.append(tuple([link_text, link_href, date, location, image_path]))
            print(tournaments[-1])
#            print(each_div.find_all('a')['href'])
        print("PAGE: " + str(page_num) + " " + "EXPECTED: " + str(5 * page_num) + " ACTUAL: " + str(len(tournaments)))

    pickle.dump(tournaments, open("tournaments.pickle", "wb"))
    print("Done.")
