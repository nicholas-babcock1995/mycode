#!/usr/bin/env python3

#function 1
"""farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]"""

farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def function_one():
    #returns all animals from NE farm
    animalList = []
    for dict in farms:
        for key in dict:
            if key == "name" and dict[key] == ("NE Farm"):
                for animal in dict["agriculture"]:
                     if animal != "carrots" and animal != "celery" and animal != "bananas" and animal != "apples" and animal != "oranges":
                         animalList.append(animal)
    
    return animalList




def function_two():
    #user chooses farm, i return plants/animals on farm
    user_choice = input("Choose a farm ( NE Farm, W Farm, or SE Farm).")
    agriList = []
    for dict in farms:
            for key in dict:
                if key == "name" and dict[key] == user_choice:
                    agriList.append(dict["agriculture"])

    return agriList



def function_three():
    #user chooses farm, only returns animals
    animalList = []
    user_choice = input("Choose a farm (NE Farm, W Farm, or SE Farm).")
    for dict in farms:
        for key in dict:
            if key == "name" and dict[key] == user_choice:
                for animal in dict["agriculture"]:
                    if animal != "carrots" and animal != "celery" and animal != "bananas" and animal != "apples" and animal != "oranges":
                        animalList.append(animal)

    return animalList 

                        



print(function_one())
print(function_two()) 
print(function_three())
