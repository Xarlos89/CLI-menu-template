from pyboxen import boxen
import sys
import os


def box_print(wut):
    print(boxen(wut))

def menu():
    menu = {}
    menu['1'] = "Option number 1  " + "\n"
    menu['2'] = "Option number 2  " + "\n"
    menu['3'] = "Option number 3  " + "\n"
    menu['4'] = "Option number 4  "
    
    while True:
        pretty_menu = ''
        for entry in menu.keys():
            pretty_menu = f'{pretty_menu} {entry} - {menu[entry]}'
        box_print(pretty_menu)

        selection = str(input("What would you like to do? "))
        if selection == '1':
            os.system('clear')
            box_print('You chose option 1')
        elif selection == '2':
            os.system('clear')
            box_print('You chose option 2')

        elif selection == '3':
            os.system('clear')
            box_print('You chose option 3')

        elif selection == '4':
            os.system('clear')
            sys.exit()
        else:
            os.system('clear')
            box_print("\nYou have to choose an option between 1 and 4. \n")
            

menu()