pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"],
 "fish": ["undersea caster", "fake coral", "buried treasure"]}

def initPet():
    petType = ""

    petOptions = list(petToys.keys())

    while petType not in petOptions:
        print("Please input a type of pet from the following options: ")
        for option in petOptions:
            print(option)
        petType = input("please input one of the pets: ")

    pet["type"] = petType

    input("What would you like to name your " + pet["type"] + "?")
    
