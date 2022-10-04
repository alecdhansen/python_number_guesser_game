from random import randint

print("Let's Play a Game!")

guesses = 0

number = input("Enter a number between 1 and 10 and I will guess it within 3 tries! ")
player_number = int(number)

guesses = 0

while guesses < 3:
    computer_guess = randint(1, 10)
    print("Is you number", computer_guess, "?")

    guesses = guesses + 1

    if computer_guess == player_number:
        break
    elif computer_guess < player_number:
        print("My guess is too low!")
    elif computer_guess > player_number:
        print("My guess is too high!")

if computer_guess == player_number:
    print("You lose! I guessed your number!")
elif computer_guess != player_number:
    print("You win! Your number was", player_number)
