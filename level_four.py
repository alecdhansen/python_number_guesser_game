print("Let's Play a Game!")
choice = input(
    "Would you like to choose a number for me to guess or try to guess my number? Enter 'a' for you to choose, enter 'b' for me to choose! "
)

if choice.lower() == "a":
    import level_one
elif choice.lower() == "b":
    import level_three
