#!/usr/bin/env python3

import requests
import datetime
URL ='http://api.open-notify.org/iss-now.json'

def main():
    resp= requests.get(URL).json()
    print("ISS time stamp : {} ".format(datetime.datetime.fromtimestamp(resp['timestamp']) ))
    print("Current location of the ISS")
    print(" Longitude : {}".format(resp['iss_position']['longitude']))
    print(" Latitude : {}".format(resp['iss_position']['latitude']))
main()
