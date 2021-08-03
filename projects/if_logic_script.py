#!/usr/bin/python3

"""                         
                                | AVATAR QUIZ |
    This script will prompt a user with a quiz of multiple choice answers.
    The answers will be stored and then calculated at the end.
                                                                        """

game =  {
            "questions":  [
                            "What is your favorite season?",
                            "Which food would you prefer?",
                            "Which animal do you like best?",
                            "Which sport do you prefer?",
                            "Which game do you prefer?"

                        ],                   
            "answers":    [
                            ["Summer","Winter","Spring","Fall"],
                            ["Hot Wings","Cotton Candy","Soup","Bread"], 
                            ["Fox","leemur","Shark","Mole"],
                            ["Boxing","BMX","Surfing","Football"],
                            ["Call of Duty","Candy Crush","Goldfish","Jumanji"]
                        ],
            "choices":    ["A)","B)","C)","D)"],
            "responses":  [
                         "You are a fire bender!",
                         "You are an air bender!",
                         "You are a water bender!",
                         "You are an earth bender!"
                         ]
        }

player = {
            "fire": 0,
            "air": 0,
            "water": 0,
            "earth": 0
         }
turns = len(game["questions"])
index = 0
answer_index = 0
flag = False
while turns > 0 :
    turns -= 1
    answer = ""
    print("Please enter A,B,C, or D, or exit to quit")
    print(game["questions"][index])
    for choice in game["choices"]:
        print(choice + game["answers"][index][answer_index])
        answer_index += 1

    answer = input()
    answer = answer.upper()
    if answer == "A":
        player["fire"] += 1
    elif answer == "B":
        player["air"] += 1
    elif answer == "C" : 
        player["water"] += 1
    elif answer == "D" : 
        player["earth"] += 1
    elif answer == "EXIT":
        flag = True
        turns = 0
    else:
        print("bad input, try again")
        turns =+ 1
        index -= 1
    index += 1
    answer_index = 0
    print("")
# find out which score is highest 
max_response = max(player, key = player.get)
if flag == False:
    print("Congratulations, you would be excellent at bending {}".format(max_response))
else:
    print("Come back later to play again!")
