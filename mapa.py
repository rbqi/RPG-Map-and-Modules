# Description: Map Module

import sys
import numpy as np

# List of modules
modules = ["map", "characters", "quit"]
# List of the territories on the map
territories = ["monu", "gozen"]

# Layout of Monu Territory (South Side 4x4 grid)
# MonuBorder is the starting base of the first quest
# MoNO is an area filled with hidden enemies
# MV is an empty area
# Mource is where you can find weapons, food and treatment
# Mountik is the mountain 800km away where the first amulet is hidden
# MonuLiberty is where the first quest is completed

monu_territory = np.array([
      ["MonuBorder", "MV", "MV", "MoNo"],
      ["MoNo", "Mource", "MV", "MoNo"],
      ["MV", "MoNo", "Mource", "Mountik"],
      ["MonuLiberty", "MV", "MoNo", "MV"]
 ])

# Layout of Gozen Territory (North Side 4x4 grid)
# GozenBorder is where the starting base & second quest begins
# Gwar is an area filled with scattered enemies
# GV is an empty area
# Goreload is where you can find weapons, food and treatment
# Gwind is the windmill 600km away and where the last amulet is hidden
# GozenLiberty is where the final quest is completed

gozen_territory = np.array([
      ["GozenBorder", "GV", "GV", "Gwar"],
      ["Gwar", "Goreload", "GV", "Gwar"],
      ["Gwind", "Gwar", "Goreload", "GV"],
      ["GV", "GV", "Gwar", "GozenLiberty"]
 ])


def monu_ter():
    """" Output Monu Territory"""
    print(monu_territory)


def gozen_ter():
    """" Output Gozen Territory"""
    print(gozen_territory)


print("\n")
print("Welcome to the Mantik Village Map!")
print("\n")
# Ask user which territory they would like to go
print("Which territory would you like to go? ")
for t in territories:
    print(f"* {t}")
map_input = input("Choice: ")


while True:
    # If user choose Monu
    if map_input == "monu":
        print("\n")
        print("MONU TERRITORY: ")
        monu_ter()
        pass
        print("\n")
        # 'Map' is removed
        modules.remove("map")
        # Updated Modules List
        print("Choose one of the following: ")
        for m in modules:
            print(f"* {m}")
        modules_input = input("Choice: ")

        while True:
            if modules_input == "characters":
                import character_inventory as ci
                print(ci.char_inv1())
                sys.exit()
                print(ci.char_inv2())
                sys.exit()

            elif modules_input == "quit":
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid Choice!")
                sys.exit()

    # If user choose Gozen
    elif map_input == "gozen":
        print("\n")
        print("GOZEN TERRITORY: ")
        gozen_ter()
        pass
        print("\n")
        # 'Map' is removed
        modules.remove("map")
        # Updated Modules List
        print("Choose one of the following: ")
        for m in modules:
            print(f"* {m}")
        modules_input = input("Choice: ")

        while True:
            if modules_input == "characters":
                import character_inventory as ci
                print(ci.char_inv1())
                sys.exit()
                print(ci.char_inv2())
                sys.exit()

            elif modules_input == "quit":
                print("Goodbye!")
                sys.exit()

            else:
                print("Invalid Choice!")
                sys.exit()

    # If user chooses an invalid choice from the list
    else:
        print("Invalid Choice!")
        sys.exit()
