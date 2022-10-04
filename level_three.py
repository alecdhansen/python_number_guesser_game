from random import randint

print("Let's Play a Game!")


# def computer_playing():
number = input("Enter a number between 1 and 10 and I will guess it within 3 tries! ")
player_number = int(number)
guesses = 0
one = 1
ten = 10

play = True
while play == True:
    computer_guess = randint(one, ten)
    print("Is your number", computer_guess, "?")

    guesses = guesses + 1

    if computer_guess == player_number:
        print("I guessed your number in ", guesses, "tries!")
        # playing = False
        break
    elif computer_guess < player_number:
        print("My guess is too low!")
        one = computer_guess + 1
    elif computer_guess > player_number:
        print("My guess is too high!")
        ten = computer_guess - 1
