# Description: Character and Inventory Module

import sys

# List of modules
modules = ["map", "characters", "quit"]
# List of available charcaters
characters = ["kuro", "adachi"]

# Nested dict of Kuro and Adachi's inventory
kuro_inventory = {
  "Kuro's Inventory": {
      "Level": 1,
      "Default Weapon": "Sword",
      "Damage": 0,
      "Kills": 0,
      "Max Energy": 1.972,
      "Protection": 10
  }
}
adachi_inventory = {
  "Adachi's Inventory": {
      "Level": 1,
      "Default Weapon": "Bow & Arrow",
      "Damage": 0,
      "Kills": 0,
      "Max Energy": 1.709,
      "Protection": 17
  }
}


def char_inv1():
    """" Output Kuro's inventory"""
    print(kuro_inventory)


def char_inv2():
    """" Output Adachi's inventory"""
    print(adachi_inventory)


print("\n")
# Ask user to choose a character
print("Pick a character:")
for c in characters:
    print(f"* {c}")
characters = input("Character: ")

while True:
    # If user choose Kuro
    if characters == "kuro":
        print("\n")
        char_inv1()
        pass
        print("\n")
        # 'Characters' is removed
        modules.remove("characters")
        # Updated modules list
        print("Choose one of the following: ")
        for m in modules:
            print(f"* {m}")
        modules_input = input("Choice: ")

        while True:
            if modules_input == "map":
                import mapa
                print(mapa.monu_ter())
                sys.exit()
                print(mapa.gozen_ter())
                sys.exit()

            elif modules_input == "quit":
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid Choice!")
                sys.exit()

    # If user choose Adachi
    elif characters == "adachi":
        print("\n")
        char_inv2()
        pass
        print("\n")
        # 'Characters' is removed
        modules.remove("characters")
        # Updated modules list
        print("Choose one of the following: ")
        for m in modules:
            print(f"* {m}")
        modules_input = input("Choice: ")

        while True:
            if modules_input == "map":
                import mapa
                print(mapa.monu_ter())
                sys.exit()
                print(mapa.gozen_ter())
                sys.exit()

            elif modules_input == "quit":
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid Choice!")
                sys.exit()

    # If user chooses an invalid choice from the list
    else:
        print("Invalid Choice.")
        sys.exit()
