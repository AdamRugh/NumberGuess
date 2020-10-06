"""Guess the sum of the dice"""
from random import randint
from time import sleep 

"""Holds what the user enters"""
def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess;

"""Rolls die and identifies if user guess and die value equal or not"""
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("No guessing higher than the maximum possible value!")
  else:
    print("Rolling...")
    sleep(2)
    print("The 1st roll is: %d" % first_roll) 
    sleep(1)
    print("The 2nd roll is: %d" % second_roll) 
    sleep(1)
    total_roll = first_roll + second_roll
    print(total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
        print("You WIN!!")
    else:
        print("You lost, try again")

"""Enter how many sides the individual die has. Example: A normal 6 sided die would be roll_dice(6) and a 12 sided die would be roll_dice(12)"""
roll_dice(6)
