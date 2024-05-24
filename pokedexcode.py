import json

with open('pokedex.json', 'r') as in_file:
    pokedex = json.load(in_file)

def get_pokemon(type="all"):
    if type == "all":
        names = [p['name'] for p in pokedex['pokemon']]
    else:
        names = [p['name'] for p in pokedex['pokemon'] if type in p['type']]

    return names
def list_all():
    print("/n")
    names = get_pokemon()
    for i, name in enumerate(names):
        print(f"{i + 1}: {name}")
    print("/n")

def list_by_type():
    print("/n")
    poke_type = input("Give a type: ")
    names = get_pokemon(poke_type)
    print(f"{poke_type} pokemon:")
    for i, name in enumerate(names):
        print(f"{i + 1}: {name}")
    print("/n")
def display_pokemon():
    poke_select = input("Please select a pokemon")
    for i in range(151):
        if pokedex["pokemon"][i]["name"] == poke_select:
            print(json.dumps(pokedex["pokemon"][i], indent=4))
def get_evelutions():
    poke_select = input("Please select a pokemon")
    for i in range(151):
        if pokedex["pokemon"][i]["name"] == poke_select:
            try:
                print(json.dumps(pokedex["pokemon"][i]["prev_evolution"]))
            except KeyError:
                print("")
            try:
                print(json.dumps(pokedex["pokemon"][i]["next_evolution"]))
            except KeyError:
                print("")


            
                  
def user_interface():

    print("******** POKEDEX ********\n")

    while True:
        print("________ Menu ________")
        print("1: List all pokemon")
        print("2: List pokemon by type")
        print("3: Get a pokemon")
        print("4: Get pokemon evelutions")
        print("0: Quit")

        choice = input("Make a selection: ")
        if choice == "1":
            list_all()
        elif choice == "2":
            list_by_type()
        elif choice == "3":
            display_pokemon()
        elif choice == "4":
            get_evelutions()
        elif choice == "0":
            break
        else:
            print("Invalid Selection!")
user_interface()
