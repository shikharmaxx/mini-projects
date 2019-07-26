rooms = {
            'room' : {
                'east' : 'corridor'
                },
           
            'corridor' : {
                'north' : 'hotel lobby',
                'south' : 'swimming pool area',
                'east' : 'store room',
                'west' : 'room'              
                },

            'store room' : {
                'west' : 'corridor',
                'item' : 'zombies'
               },
            
            'hotel lobby' : {
                'west' : 'restaurant',
                'south' : 'corridor',
                'north' : 'casino',
                'east' : 'emergency exit'
                },
            
            'casino' : {
                'south' : 'hotel lobby',
                'item' : 'carkey'
                },

            'restaurant' :{
                'east' :'hotel lobby',
                'item' : 'zombies'
                } ,
            'swimming pool area':{
                'west' : 'pump room',
                'north' : 'corridor'
            },
            'pump room' :{
                'east' : 'swimming pool area',
                'item' : 'wrench'
            },

            'emergency exit' : {
                'west' : 'hotel lobby'
            }
        }