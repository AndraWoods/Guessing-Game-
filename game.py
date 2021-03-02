""" A number-guessing game."""
import random
print('Hi')
#Prompt user for a name

user = input("What is your name: ")
print("Hello, " + str(user) + ". We are guessing between a number between 1 and 100")

random_num = random.randint(1, 101)
guess = -1
#While the guess is not correct prompt for a guess
while guess != random_num:
    guess = int(input("Choose a number: "))
    #If the guess is too low say so or too high say so.
    if guess < random_num:
        print("Too low! Guess again!")
    if guess > random_num:
        print("Too high! Guess again!")
#If the guess is correct print so and exit the loop 
print("Correct! The number is: " + str(random_num))