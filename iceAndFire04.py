#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_HOUSES = "https://www.anapioficeandfire.com/api/houses/"
def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print("------------------------------------------------------------------")
        print("CODE CUSTOMIZATION")

        #i think we should store the requests for the house information seperatel
        print("Associated HOUSES!")
        if 'allegiances' in got_dj:
            for allegiance in got_dj['allegiances']:
                houseresp = requests.get(allegiance)
                house_json = houseresp.json()
                if 'name' in house_json:
                    print(house_json['name'])
        print("Associated Books!")
        if 'books' in got_dj:
            for book in got_dj['books']:
                bookresp = requests.get(book)
                book_json = bookresp.json()
                if 'name' in book_json:
                    print(book_json['name'])
        if 'povBooks' in got_dj:
            for pov_book in got_dj['povBooks']:
                pov_book_resp = requests.get(pov_book)
                pov_book_json = pov_book_resp.json()
                if 'name' in pov_book_json:
                    print(pov_book_json['name'])
if __name__ == "__main__":
        main()

