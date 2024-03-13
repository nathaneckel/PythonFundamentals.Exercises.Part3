#this function asks user for a number 1-10
from random import randrange

#Helper Functions
#Initiate the game
def number_guessing_game():
    guess = int(input("Please enter a number (0 to 10)\n"))
    return(guess)

#Function: Generate and Return a Number
def random_number_generator():
    return randrange(10)

#Function: Compare Number for the Guess; Give Feedback
def number_compare(random, guess):
    if(random > guess):
        print("My number was " + str(random) + ". " + str(guess) + " was too low!\n")
    elif(random < guess):
        if (random < guess):
            print("My number was " + str(random) + ". " + str(guess) + " was too high!\n")
    elif (random == guess):
            print("My number is also " + str(random) + ". " + str(guess) + " IS CORRECT!\n")

#Main Function - This Calls the Helpers In Order
def main():
    random = random_number_generator()
    guess = number_guessing_game()
    number_compare(random, guess)

#Call Main - This Runs the Program
main()