"""
A simple program to explore the solar system a bit.
"""

import json

def main():
    print("Welcome to the Solar System!")

    print("Please enter your name:")
    user_name = input()

    print(f"Hello {user_name}!")

    print("Would you like to go to a random planet? (Y/N)")
    goto_random_planet = input().strip().lower()
    while goto_random_planet not in 'yn':
        print("Please enter either Y or N.")
        goto_random_planet = input().strip().lower()

    with open("planetarySystem.json", "r") as planets_json:
        planets_json = json.load(planets_json)

        if goto_random_planet == 'y':
            print("Choosing a random planet")
            
            print("Travelling to Earth")
            print(planets_json["planets"][2]["description"])
        else:
            print("What planet would you like to go to?")
            goto_planet = input()
            # TODO Check for valid planet name

            print("Travelling to Earth")
            print(planets_json["planets"][2]["description"])


main()
