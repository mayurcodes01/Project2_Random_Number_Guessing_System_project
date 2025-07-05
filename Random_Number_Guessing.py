#Project 2 : Random Number Guessing 
from random import *

no = randint(1, 10)
print("\n\t\t\t\t~~~ Guess the number ~~~\n")
print("\t\t\t\tenter between 1 to 10\n")
while True:
    guess = int(input("\t\t\t\tEnter your guess: "))
    if guess<no:
        print("\t\t\t\tTry again with bigger no.")
    elif guess>no:
        print("\t\t\t\tTry again with smaller no.")
    else:
        print(f"\n\t\t\t\tCongratulations! you guessed it right: {no}")
        break
