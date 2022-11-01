import sys
import os

def menu():
    menu = {}
    menu['1'] = "- Option number 1"
    menu['2'] = "- Option number 2"
    menu['3'] = "- Option number 3"
    menu['4'] = "- Quit"
    
    while True:
        options = menu.keys()
        for entry in options:
            print (entry, menu[entry])

        selection = str(input("What would you like to do? "))
        if selection == '1':
            os.system('clear')
            print('You chose option 1')
        elif selection == '2':
            os.system('clear')
            print('You chose option 2')

        elif selection == '3':
            os.system('clear')
            print('You chose option 3')

        elif selection == '4':
            os.system('clear')
            sys.exit()
        else:
            os.system('clear')
            print("\nYou have to choose an option between 1 and 4. \n")
            

menu()