# By: Magnus Crooke, File Name: unit5.py, last modified: 10-5-17, This programs is a guessing game.
import random


def start_game():
    """
    This function asks user if they would like to play the game, the function counts how many guesses it takes for
    the user  to guess the correct number. Once the user guesses the right number the function asks if the user
    would like to play again.
    """
    correctnumber = random.randint(1, 100)
    print("Would you like to try and guess my number?")
    userguess = int(input("Guess:"))
    numberguess = 0
    while userguess != correctnumber:
        if userguess < correctnumber:
            print("Your guess was to low, would you like to try again?")
        elif userguess > correctnumber:
            print("Your guess was to high, would you like to try again?")
        numberguess += 1
        userguess = int(input("Guess:"))
    numberguess += 1
    print("Nice job you got my number! It took you", numberguess, "guesses to get my number!")


def main():
    """
    This function runs the guessing game, asking the user if they would like to play or not.
    """
    print("Would you like to guess my number? press 'y' for yes, and 'n' for no?")
    yes = input("Start?")
    while yes == 'y':
        start_game()
        yes = input("Would you like to play again?")
    print("Sorry, have a nice day")


main()

