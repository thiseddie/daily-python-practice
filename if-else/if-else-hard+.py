# number gussing game.

import random

number = random.randint(1, 10)

while true;
   guess = int(input("enter your guess :"))

   if guess < number :
      print("too low ")
   elif guss > number :
      print("too high")

   else:
      print("congratulations ! you gussed the correct number.")
      break
