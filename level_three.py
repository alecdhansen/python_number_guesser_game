from random import randint
import time


def level_three():
    print("Let's Play a Game!")

    number = input(
        "Enter a number between 1 and 1000 and I will guess it within 3 tries! "
    )
    player_number = int(number)
    guesses = 0
    low = 1
    high = 1000

    play = True
    while play == True:
        computer_guess = randint(
            low, high
        )  # SHOULD USE computer_guess = (low + high) // 2 ----> the double division (floored quotient) sign floors the result, this gives us optimization
        print("Is your number", computer_guess, "?")

        guesses = guesses + 1

        if computer_guess == player_number:
            print("I guessed your number in ", guesses, "tries!")
            break
        elif computer_guess < player_number:
            print("My guess is too low!")
            low = computer_guess + 1
        elif computer_guess > player_number:
            print("My guess is too high!")
            high = computer_guess - 1
        time.sleep(1.5)


if __name__ == "__main__":
    level_three()
