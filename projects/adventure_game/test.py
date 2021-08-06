#!/usr/bin/python3
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'items' : {
                                'Bandage' : {
                                                'status' : 'not taken',
                                                'desc' : 'This could be useful'
                                            },
                                'Defribilator' : {
                                                    'status' : 'not taken',
                                                    'desc' :  'This could shock anythin                                                                 g'
                                                 },
                            }
                },
            
            }

print(rooms['Hall']['items'])
