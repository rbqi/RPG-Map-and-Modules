# Coarse: CS 30
# Period:3
# Date created: 13/10/21
# Date last modified: 20/10/21
# Name: Rabi Jasteen Juancito
# Description: Main Game File

# Import character_inventory.py and mapa.py

import sys

# Modules list
modules = ["map", "characters", "quit"]

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

    elif modules_input == "characters":
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
