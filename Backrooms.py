import time
def ending(num,reason):
        print('''
'''
,reason,'''
  _____                 ____              
 / ___/__ ___ _  ___   / __ \_  _____ ____
/ (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/
\___/\_,_/_/_/_/\__/  \____/|___/\__/_/   Ending''', num,
                                          '''

''')
        time.sleep(99) 
print('''Welcome to the Backrooms.''')
time.sleep(2)
print("Have Fun!!!")
time.sleep(2)
print('''
  ___          _                         
 | _ ) __ _ __| |___ _ ___  ___ _ __  ___
 | _ \/ _` / _| / / '_/ _ \/ _ \ '  \(_-<
 |___/\__,_\__|_\_\_| \___/\___/_|_|_/__/
                                         by Mehmet Akif
''')
time.sleep(3)
print("You are in a room.")
time.sleep(1)
print('''
1-Find a Key
2-Punch Door
3-Scream
Select a way:\n'''
    )
choise = input()
    
if choise == "1":
    print("You look for the key.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("You see a key on the ground.")
    time.sleep(2)
    print("You take the key.")
    time.sleep(2)
    print("You came out from the room.")
    time.sleep(2)
    print('''
        1-Left
        2-Right
        Where do you want to go?''')
    choise3= input()
    if choise3 == "1"or "2":
        print("There is nothing on the right")
        time.sleep(2)
        print("So you need to go left.")
        time.sleep(2)
        print('''
Do you want to go left? There is blood on the ground.
1-Yes       2-No''')
        choise4 = input()
        if choise4 == "1" or "yes" or "Yes":
            print("There is a door but the door is bloody")
            time.sleep(2)
            print("The door is open with the code.")
            time.sleep(2)
            print("Find the code.")
            time.sleep(2)
            while True:
                print('''
Write the code.
                ''')
                choise5= input()
                if choise5 == "1234":
                    print("You escaped the Backrooms.")
                    time.sleep(2)
                    print('''
                
____    __    ____  __  .__   __.    
\   \  /  \  /   / |  | |  \ |  |    
 \   \/    \/   /  |  | |   \|  |    
  \            /   |  | |  . `  |    
   \    /\    /    |  | |  |\   |    
    \__/  \__/     |__| |__| \__|    Ending 1
                                     
''')
                    time.sleep(99)
                else:
                    print("Wrong Password")          
        else:
            print("You don't do anything and the monster found you")
            ending(2)
            time.sleep(99)
    else:
        print("You don't do anything and the monster found you")
        print('''
            
  _____                 ____              
 / ___/__ ___ _  ___   / __ \_  _____ ____
/ (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/
\___/\_,_/_/_/_/\__/  \____/|___/\__/_/   Ending 2
                                          
        ''')
        time.sleep(99)
        
elif choise == "2":
    print("You punch the door.")     
    time.sleep(2)
    print("The door does not open.")
    time.sleep(2)
    print("And you are bleeding.")
    time.sleep(2)
    print('''
1-Cut your clothes and make bandage
2-Wait for it to heal
What your choise?''')
    choise6 = input()
    if choise6 == "1":
        print("You cut your clothes and bandaged them to stop the bleeding.")
        time.sleep(2)
        print("There is a ventilation enter in the ceiling")
        time.sleep(2)
        print('''
        1-Enter the ventilation
        2-Find Another Way
        Which one do you prefer''')
        choise7= input()
        if choise7 == "1":
            print("You entered ventilation.")
            time.sleep(2)
            print("You moved forward and crashed into another area.")
            time.sleep(2)
            print("There are two slides opposite.")
            time.sleep(2)
            print("One has a picture of a ball pool on it, and the other a picture of a hotel.")
            time.sleep(2)
            print('''
            1-Ball Pool
            2-Hotel
            Where do you want to go?''')
            choise8 = input()
            if choise8 == "1":
                print("You are fall into a ball pool.")
                time.sleep(2)
                print("Get out there!")
                number = 10
                for i in range(10):
                    print(number)
                    time.sleep(1)
                    number -= 1
                    if number == 0:
                        ending(5,"You are drowned")
                    else:
                        continue
            elif choise8 == "2":
                print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠶⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠶⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⡀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⢀⡿⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠙⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀
⠀⠀⢸⡟⢁⣼⣿⠟⢡⣾⣿⠋⣠⣿⡿⠋⣴⣿⡟⢁⣼⣿⠟⢡⣾⣿⠋⡀⠀⠀
⠀⠀⠘⢀⣾⡿⠃⣰⣿⡿⠃⣰⣿⠟⢀⣾⣿⠟⢀⣾⡿⠃⣰⣿⡿⠃⣰⡇⠀⠀
⠀⠀⠀⠉⣉⣁⡈⠉⠉⠁⠈⠉⠉⠀⠉⠉⠉⠀⠉⠉⠁⠈⠉⢉⣁⣈⠉⠁⠀⠀
⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠐⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠂⠀⠀⠀
⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀
⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⠀⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀
⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡄⠀⠀
⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀''')
                print("Bu kısım yapım aşamasînda.")
                time.sleep(99)
            else:
                print("All entrances are closed and you're drowning")
                time.sleep(2)
    else:
        print("You bled.")
        print('''


  _____                 ____              
 / ___/__ ___ _  ___   / __ \_  _____ ____
/ (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/
\___/\_,_/_/_/_/\__/  \____/|___/\__/_/   Ending 3
                                          

''')
    time.sleep(99)
        
    
elif not choise == "1" or "2" or "3":
    import time
    print('''I guess you want to die in the Backrooms
 without doing anything.''')
    time.sleep(2)
    print("As you wish.")
    time.sleep(2)
    print('''


  _____                 ____              
 / ___/__ ___ _  ___   / __ \_  _____ ____
/ (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/
\___/\_,_/_/_/_/\__/  \____/|___/\__/_/   Ending 4
                                          

''')
    time.sleep(99) 