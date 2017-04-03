from bs4 import BeautifulSoup
import requests
import re
import pickle
import HTMLParser
import sys
import string

if __name__ == "__main__":
    base_url = "https://www.ssbwiki.com"

    names = ["Mario_","Luigi_","Yoshi_","Donkey_Kong_","Link_","Samus_","Kirby_","Fox_","Pikachu_","Captain_Falcon_","Ness_",
    "Peach_","Bowser_","Dr._Mario_","Zelda_","Sheik_","Ganondorf_","Young_Link_","Falco_","Mewtwo_","Pichu_","Ice_Climbers_","Marth_",
    "Roy_","Mr._Game_%26_Watch_"]
    # names = ["Mario_"]

    parser=HTMLParser.HTMLParser()

    movetypes = dict()
    movenames = dict()
    char_index = 0
    for character in names:
        tuples = [0] * 30
        move_types = [0] * 60
        move_names = [0] * 60
        index = 0
        # Grabbing Move types
        r = requests.get(base_url + "/" + character + "(SSBM)")
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', {"class" : "wikitable"})
        index = 0
        for th in table('tr')[2:]:
            move = th.find_all('th')
            for t1 in move:
                move_name = t1.find(text=True)
                if move_name.isalpha() or (' ' in move_name) == True:
                    move_types[index] = move_name
                    index += 1
        move_types = [x for x in move_types if x != 0]
        movetypes[character] = move_types
        # print(movetypes[character])



        # Grabbing Move names            
        index = 0
        for tr in table('tr'):
            td_list = tr.find_all('td')
            if len(td_list) > 0:
                # print(td_list[0])
                t2 = td_list[0]
                text = t2.find(text=True)
                if text == None or text == parser.unescape("&#160;") or text == "":
                    text = " "
                # print(text)
                if text[0].isalpha() or text == " ":
                    # print(text)
                    move_names[index] = text
                    index += 1
        move_names = [x for x in move_names if x != 0]
        movenames[character] = move_names
        # print(movenames[character])
        print("FINISHED SCRAPING")
        print(character)
        print("\n")






            # if len(td_list) > 0:
            #     # print(td_list[0].text)
            #     # print(" " in td_list[0].text)
            #     t2 = td_list[0].text
            #     if t2 == parser.unescape("&#160;") or t2 == "" or t2 == None:
            #         t2 = " "
            #     # print(t2)
                                
            #     if t2[0].isalpha() or t2 == " ":
            #         t2 = unicode(t2)
            #         print(t2)
            #         # move_name[index] = t2


        #             move_name[index] = t2
        #             index += 1
        # move_name = [x for x in move_name if x != 0]
        # print(move_name)

        # Grabbing Move names and Description
        # index = 0
        # for tr in table('tr'):
        #     data = tr.find_all('td')
        #     for t2 in data:
        #         texts = t2.find_all(text=True)
        #         final = ""
        #         for s in texts:
        #             final = final + s;
                
        #         if final == "" or final == " " or final == parser.unescape("&#160;"):
        #             final = " " 
        #         if (final[0].isalpha() or final == " "):
        #             print("'" + final + "'")
        #             # print(final)
        #             text_data[index] = final
        #             index += 1
        # # print(text_data)
        # index = 0
        # count1 = 0
        # count2 = 0
        # for elem in text_data:
        #     if elem != 0 and ('Ground:' not in elem) == True and ('NTSC: 4%' not in elem) == True and ('Depends on projectiles' not in elem) == True:
        #         # print(index)
        #         # print(elem)
        #         # print("\n")
        #         true_data[index] = elem
        #         index += 1
        # index = 0
        # # print(text_data)
        # # print("\n")
        # # print(true_data)
        # for s in range(0,len(true_data),2):
        #     v = s + 1
        #     if true_data[s] != 0 and true_data[v] != 0:
        #         val = (true_data[s], true_data[v])
        #         # print(index)
        #         # print(val)
        #         # print("\n")

        #         tuples[index] = val
        #         index += 1
        #     # print("'" + s + "'")
        # # print(tuples)
        # tuples = [x for x in tuples if x != 0]
        # test=deepcopy(tuples)
        # movesets[character] = test
        # char_index += 1
        # print("CHARACTER FINISHED")
        # print(character)
        # print(tuples)
        # print()
        # print()
    # print(list_tuples)

    # print("PRINTING MOVESET")
    # for c in names:
    #     print(c)
    #     print(movesets[c])
    #     print()
    #     print()
            
    sys.setrecursionlimit(4000)
    pickle.dump(movetypes, open("movetypes.pickle", "wb"))
    pickle.dump(movenames, open("movenames.pickle", "wb"))
    print("Done.")