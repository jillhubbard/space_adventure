"""
A simple program to explore the solar system a bit.
"""

print("Welcome to the Solar System!")

print("Please enter your name:")
user_name = input()

print(f"Hello {user_name}!")

print("Would you like to go to a random planet? (Y/N)")
goto_random_planet = input()
# TODO Check for valid input

if goto_random_planet:
    print("Choosing a random planet")
    
    print("Travelling to ")
    # TODO Print planet details
else:
    print("What planet would you like to go to?")
    goto_planet = input()
    # TODO Check for valid planet name

    print("Travelling to ")

