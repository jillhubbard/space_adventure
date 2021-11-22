"""
A simple program to explore the solar system a bit.
"""

import json

goto_random_planet = ""


def print_welcome() -> None:
    print("Welcome to the Solar System!")


def get_name() -> None:
    print("Please enter your name:")
    user_name = input()

    print(f"Hello {user_name}!")


def get_random_or_specific() -> None:
    global goto_random_planet

    print("Would you like to go to a random planet? (Y/N)")
    goto_random_planet = input().strip().lower()
    while goto_random_planet not in 'yn':
        print("Please enter either Y or N.")
        goto_random_planet = input().strip().lower()


def print_planet_details() -> None:
    global goto_random_planet
    
    with open("planetarySystem.json", "r") as planets_json:
        planets_json = json.load(planets_json)

        if goto_random_planet == 'y':
            print("Choosing a random planet")
        else:
            print("What planet would you like to go to?")
            goto_planet = input()
            # TODO Check for valid planet name

        # TODO Randomly select a planet or use a given planet
        print("Travelling to Earth")
        print(planets_json["planets"][2]["description"])


def main() -> None:
    print_welcome()
    get_name()
    get_random_or_specific()
    print_planet_details()


if __name__ == "__main__":
    main()
