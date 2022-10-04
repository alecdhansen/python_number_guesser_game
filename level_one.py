from random import randint


def level_one():
    print("Let's Play a Game!")

    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    play = True
    while play == True:

        first_guess = input(
            "I'm thinking of a number between 1 and 10. You have 3 guesses. Try and guess! "
        )

        if first_guess not in number:
            print("That's not a number between 1 and 10. Try harder please! ")

        random_number = number[randint(0, 9)]
        if first_guess == random_number:
            print("Wow you're smart. Great guess! The number was", random_number)
        elif first_guess != random_number:
            if first_guess > random_number:
                second_guess = input(
                    "You are too high! You have two more guesses. Guess again! "
                )
            else:
                second_guess = input(
                    "You are too low! You have two more guesses. Guess again! "
                )
            if second_guess == random_number:
                print("That's correct! Great guess! The number was", random_number)
            elif second_guess != random_number:
                if second_guess > random_number:
                    third_guess = input("You are too high! Guess again! ")
                else:
                    third_guess = input("You are too low! Guess again! ")
                if third_guess == random_number:
                    print("You got it! That was close. The number was", random_number)
                elif third_guess != random_number:
                    print("Ouch, that's incorrect. You aren't very good at this. ")
                    print(random_number, "was the number I had in mind.")

        play_again = input(
            "Play again? Enter any key to continue or enter 'n' to quit: "
        ).lower()

        if play_again == "n":
            print("Alright word see ya later!")
            break


if __name__ == "__main__":
    level_one()

# computer = randint()

# for count in range(3):
#     player = int(input("Guess a number between 1 and 10. "))
#     if player == computer:
#         print("Correct! The number is", player)
#         break
#     elif count == 2:
#         print("You ran out of guesses.")
