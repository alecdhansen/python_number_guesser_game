from level_one import level_one
from level_three import level_three

print("Let's Play a Game!")
choice = input(
    "Hit 'a' for me to choose a number for you to guess, hit 'b' to choose a number for me to guess! "
)

if choice.lower() == "a":
    level_one()
elif choice.lower() == "b":
    level_three()
