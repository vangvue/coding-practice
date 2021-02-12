pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"], "fish": ["undersea caster", "fake coral", "buried treasure"]}

def initPet():
    petType = ""
    petOptions = list(petToys.keys())

    while petType not in petOptions:
        print("Please input a type of pet from the following options: ")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ")

    pet["type"] = petType
    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")

def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Here are your options:")
    print("------")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["text"])


def quitSimulator():
    print("Quit the simulator. Thanks for playing!")

def feedPet():
    pet["hunger"] -= 10
    print("Fed your pet!")

def main():
    initPet()

    menuOptions = {"Q": {"function": quitSimulator, "text": "Quit the game"},
    "F": {"function": feedPet, "text": "Feed " + pet["name"]}}

    keepPlaying = True
    while keepPlaying:

        menuSelection = ""
        while menuSelection not in menuOptions.keys():
            printMenu(menuOptions)
            menuSelection = input("Which of these menu options would you like to use? ").upper()

        if menuSelection == "Q":
            keepPlaying = False

        menuOptions[menuSelection]["function"]()

        print()

main()
