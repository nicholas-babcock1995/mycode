#!/usr/bin/env python3
# Trivia Database Challenge
import requests

API =" https://opentdb.com/api.php?amount=3&category=11&difficulty=easy&type=boolean"
def main():

    #first thing to do is get the data
    resp = requests.get(API)

    #convert the JSON
    trivia = resp.json()
    index = 0 
    #time to give the user a question and gather their answer
    while(index < len(trivia['results'])):
            print("Answer the question with true or false")
            answer = input(trivia['results'][index]['question']).upper()
            if(answer == trivia['results'][index]['correct_answer'].upper()
                    and (answer == "TRUE" or answer == "FALSE")):
                print("You are correct!")
            elif(answer != trivia['results'][index]['correct_answer'].upper() 
                    and( answer == "TRUE" or answer == "FALSE")):
                print("You are incorrect!")
            else:
                index -= 1
                print("bad input try again with true/false")
            index += 1
    
    


if __name__ == "__main__":
    main()
