"""
This program implements a menu loop with choices for managing a collection of
critters. It imports a Critter class from critter.py
Name: Andrew Henin
Date: April 2022
"""

from critter import *

def main():
    critters = []
    printMenu()
    choice = getMenuInput()
    while choice != 0:
        if choice == 1:
            if len(critters) == 0:
                print("\nNo critters here yet; try adding one!")
            else:
                print("\nThe room has some critters in it:\n")
                for i in range(len(critters)):
                    print(critters[i].__str__())
                    print()
        if choice == 2:
            addNew(critters)
        if choice == 3:
            feedCritter(critters)
        if choice == 4:
            petCritter(critters)
        if choice == 5:
            playCritter(critters)
        if choice == 6:
            sleepCritter(critters)
        printMenu()
        choice = getMenuInput()

    print("\nGoodbye!\n")


def printMenu():
    """
    This function prints the menu of choices for the user.
    parameters: none
    returns: none
    """

    print("\n--------------------")
    print("Main Menu:")
    print("1. Check on critters")
    print("2. Add new critter")
    print("3. Feed critter")
    print("4. Pet critter")
    print("5. Play with critter")
    print("6. Go to bed")
    print("0. Quit")


def getMenuInput():
    """
    This function prompts the user to input a number from 0 to 6 based on their
    desired choice.
    parameters: none
    returns: choice -the valid choice of the user
    """
    print()
    choice = input("Enter selection: ")
    while choice not in ["0", "1", "2", "3", "4", "5", "6"]:
        print("invalid selection, please try again:")
        choice = input("Enter selection: ")
    return int(choice)


def addNew(critters):
    """
    This function adds a new critter object and appends it to the critters list.
    parameters: critters -the list with all current critters
    returns: none
    """

    print()
    name = input("New critter's name: ")
    status = input("What's an adjective that describes the critter? ")
    personal = input("What's the critter's personal pronoun \
(e.g. she, they, it)? ")
    posessive = input ("What's the critter's posessive pronoun \
(e.g. her, their, its)? ")
    food = input("What does the critter like to eat? ")

    critterobj = Critter(name, status, personal, posessive, food)

    critters.append(critterobj)


def feedCritter(critters):
    """
    This function increases the number of times a critter was fed.
    parameters: critters -the list of all current critters
    returns: none
    """

    if len(critters) == 0:
        print("\nNo critters available, try again later!")
    else:
        print("\nAvailable Critters:")
        for i in range(len(critters)):
            print(str(i+1) + ".", critters[i].get_name())

        choice = critterInput(critters)
        print()
        print(critters[choice-1].feed())


def petCritter(critters):
    """
    This function increases the number of times a critter was petted.
    parameters: critters -the list of all current critters
    returns: none
    """

    if len(critters) == 0:
        print("\nNo critters available, try again later!")
    else:
        print("\nAvailable Critters:")
        for i in range(len(critters)):
            print(str(i+1) + ".", critters[i].get_name())

        choice = critterInput(critters)
        print()
        print(critters[choice-1].pet())


def playCritter(critters):
    """
    This function increases the number of times a critter was played with.
    parameters: critters -the list of all current critters
    returns: none
    """

    if len(critters) == 0:
        print("\nNo critters available, try again later!")
    else:
        print("\nAvailable Critters:")
        for i in range(len(critters)):
            print(str(i+1) + ".", critters[i].get_name())

        choice = critterInput(critters)
        print()
        print(critters[choice-1].play())



def critterInput(critters):
    """
    This function checks the input for the feed, pet, and play menu options.
    parameters: critters -the list of all Critters
    returns: userinput -the input of the user
    """

    userinput = input("Please select a critter: ")
    while (not userinput.isdigit()) or \
    ((int(userinput) <= 0 or int(userinput) > len(critters))):
        userinput = input("Invalid selection, please try again: ")

    return int(userinput)


def sleepCritter(critters):
    """
    This function prints "Goodnight!" and calls the sleep method on each critter
    in the critters list.
    parameters: critters -a list with all current Critters
    returns: none
    """

    for i in range(len(critters)):
        critters[i].sleep()
    print("\nGoodnight!\n")

main()
