#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    ## make a call to NASAAPI with our key
    user_date ="&date=" +  input("Please choose a date YYYY-MM-DD format")
    apodresp = requests.get(NASAAPI + nasacreds + user_date)

    ## strip off json
    apod = apodresp.json()


    pic_response = requests.get(apod['url'])
    if pic_response['media_type'] == "image":
        file = open("nasa_images/"+ apod['title'] + ".png" , "wb")
        file.write(pic_response.content)
        file.close()
    
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()

