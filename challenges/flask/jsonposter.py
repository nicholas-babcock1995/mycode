#!/usr/bin/python3
  
import requests
import json

def main():
    url = "http://10.1.225.90:2224/login"
    ans = input("What is your answer?\n")
    ye_olde_dict = {'nm': ans}
    ye_olde_dict = json.dumps(ye_olde_dict)
    x = requests.post(url,data = ye_olde_dict)
    print(x.test)

if __name__ == "__main__":
    main()
