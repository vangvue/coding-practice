pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

petToys = {
"cat": ["scratching post", "toy mouse", "ball of yarn"],
"dog": ["chew toy", "stick", "frisbee"],
"fish": ["undersea castle", "fake coral", "buried treasure"]
}

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

def playToys():
    print(pet["name"] + " had a wonderful time playing with the toys!")

def getToys():
    print("Yay! Let's get some new toys!")
    toyOptions = petToys[pet["type"]]

    toyNum = -1

    while toyNum < 0 or toyNum > len(toyOptions) - 1:
        for i in range(len(toyOptions)):
            print(str(i) + ": " + toyOptions[i])
        toyNum = input("Input the number of the toy you would like: ")
        print("")

    chosenToy = toyOptions[toyNum]
    pet["toys"].append(chosenToy)
    print("Nice! You selected the " + chosenToy + "!")
    print("")

def quitSimulator():
    print("Quit the simulator. Thanks for playing!")

def feedPet():
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] -= 20
    print("Fed your pet, decreasing hunger by 10!")

def printStats():
    print("Your " + pet["type"] + " " + pet["name"] + " is doing great!")

    if int(len(pet["toys"])) == 1: print("Your pet currently has: " + str(len(pet["toys"])) + " toy, which is: ")
    elif int(len(pet["toys"])) == 0: print("Your pet currently has: " + str(len(pet["toys"])) + " toys.")
    else: print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are: ")

    for toy in pet["toys"]:
        print(toy)

    print("Your pet is currently at hunger of " + str(pet["hunger"]) + " of a max of 100.")

    if int(pet["age"]) == 1: print("Your pet is " + str(pet["age"]) + " day old.")
    else: print("Your pet is " + str(pet["age"]) + " days old.")

def main():
    initPet()

    menuOptions = {
    "Q": {"function": quitSimulator, "text": "Quit the game"},
    "F": {"function": feedPet, "text": "Feed " + pet["name"]},
    "P": {"function": playToys, "text": "Play with " + pet["name"]},
    "G": {"function": getToys, "text": "Get new toys for " + pet["name"] + "!"}
    }

    keepPlaying = True
    while keepPlaying:

        menuSelection = ""
        while menuSelection not in menuOptions.keys():
            printMenu(menuOptions)
            menuSelection = input("Which of these menu options would you like to use? ").upper()
            print("")

        if menuSelection == "Q":
            keepPlaying = False
            quitSimulator()
            break

        menuOptions[menuSelection]["function"]()

        pet["hunger"] += 10
        pet["age"] += 1
        printStats()

        print("")

main()
