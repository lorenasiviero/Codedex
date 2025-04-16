# Coin flip simulation
# This program simulates a coin flip using the random module
# It generates a random number between 0 and 1
# If the number is greater than 0.5, it prints "Heads"
# Otherwise, it prints "Tails"

import random

num = random.randint(0,1)

if num > 0.5:
  print('Heads')
else:
  print("Tails")