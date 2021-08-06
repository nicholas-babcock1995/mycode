#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Haunted Hospital
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
#I will be using a haunted hospital you have to escape from 
rooms = {

            'Hall' : {
                  'south' : 'Doctors Office',
                  'east'  : 'Nurses Station',
                  'items' : {
                                'bandage' : {
                                                'name' : 'bandage',
                                                'status' : 'not taken',
                                                'desc' : 'This could be useful'
                                            },
                                'defribilator' : {
                                                    'name' : 'defribilator',
                                                    'status' : 'not taken',
                                                    'desc' :  'This could shock anythin                                                                 g'
                                                 },
                            }
                },
            'Hospital Room' : {
                    'description': 'A dingy abandoned hospital room, I hope my healthca                                     re covers this',
                    'south' : 'Hall',
                    'north' : 'Bathroom'
                },
            'Bathroom' : {
                    'south': 'Hospital Room'
                },
            'Doctors Office' : {
                    'north' : 'Hall'
                },
            'Nurses Station' : {
                     'items' : {
                                'car key' : {
                                                'name' : 'car key',
                                                'status' : 'not taken',
                                                'desc' : 'This could be useful'
                                            }
                            },
                    'west' : 'Hall',
                    'north' : 'Hall_2',                                             
                    'east' : 'Stairwell'
                },
            'Stairwell' : {
                    'south' : 'Parking Lot'
                },
            'Hall_2' : {
                    'south' : 'Nurses Station',
                    'north' : 'Hospital Ward'
                },
            'Hospital Ward' : {
                    'south' : 'Hall_2',
                    'east' : 'Bathroom_2'
                },
            'Bathroom_2' : {
                    'west' : 'Hospital Ward'
                },
            'Parking Lot' : {
                    'south' : 'Car',
                    'north' : 'Stairwell'
                },
            'Car' : {
                'north' : 'Parking Lot'
                    }
         }

#start the player in the Hall
currentRoom = 'Hospital Room'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
     #if the room contains an item, and the item is the one they want to ge
     # this should test that a particular item is in the items list of the current room
     if 'items' in rooms[currentRoom] and move[1] in rooms[currentRoom]['items'] and rooms[currentRoom]['items'][move[1]]['status'] != "taken":
         #add the item to their inventory
         inventory.append(rooms[currentRoom]['items'][move[1]]['name'])

         #remove from the dictionary
         rooms[currentRoom]['items'][move[1]]['status'] == "taken"
          #display a helpful message
         print(move[1] + ' got!')
         #description of your newly aquired loot
         if 'desc' in rooms[currentRoom]['items'][move[1]]:
             print(rooms[currentRoom]['items'][move[1]]['desc'])
     else:
             print('Can\'t get ' + move[1] + '!')
        
  #ok so here we will make it to where you can observe a room for description    
  if move[0] == 'observe':
        if 'description' in rooms[currentRoom]  and  move[1] == currentRoom.lower():
            print(rooms[currentRoom]['description'])
        else:
            print("You cant observe that")
  ## Define how a player can win
  ##first wel say if they get to the parking lot with the car keys the can drive off
  if currentRoom == 'Car' and 'car key' in inventory :
    print('You drive off and escape the haunted hospital!!!... YOU WIN!')
    break
  if currentRoom == 'Doctors Office' and not("defribilator" in inventory):
      print('Without the defribilator the Zombie Doctor kills you.')
      break 
  elif currentRoom =='Doctors Office' and "defribilator" in inventory:
      print("You see a reanimated zombie doctor, you use the defribilator from your inventory to electrocute his brain, rendering him deanimated")
