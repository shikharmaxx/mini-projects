import time
import resources as R

def showInstructions():
 print('''
    RPG Game
    ========
    Get to the parking lot with a key and avoid zombies! 
    Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))
  if "item" in R.rooms[currentRoom]:
    time.sleep(1)
    print('You see a ' + R.rooms[currentRoom]['item'])
  print("---------------------------")

inventory = []
currentRoom ='room'

showInstructions()

while True:
    showStatus()
    
    move = ''
    while move == '':  
     move = input('->')
    
    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in R.rooms[currentRoom]:
            currentRoom = R.rooms[currentRoom][move[1]]
            print("You entered ",currentRoom)
            if currentRoom=='emergency exit':
                if 'wrench' in inventory:
                    time.sleep(0.6)
                    print("With the help of the wrench you opened the emergency exit")
                    
                    if 'carkey' in inventory :
                        print("You ran downstairs to the underground parking")
                        time.sleep(0.6)
                        print( "With your car's key started the car and escaped the Hotel....")
                        time.sleep(0.6)
                        print('YOU WIN !!')
                        break
                    else:
                        time.sleep(0.6)
                        print("but you need your car keys.")
                else :
                    print("You need a wrench to break open the exit. ")

            
        else:
            print('You can\'t go that way!')

    if 'item' in R.rooms[currentRoom] and 'zombies' in R.rooms[currentRoom]['item']:
        time.sleep(1)
        print('Zombies attacked you ..... \nGAME OVER !!')
        break

    if move[0] == 'get' :
        if "item" in R.rooms[currentRoom] and move[1] in R.rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' acquired !')
            del R.rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    
    

