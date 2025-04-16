# Guess the number
# The computer has a number between 1 and 10
# You have 5 tries to guess the number
# The number is 6
# The computer will tell you if you are right or wrong
# The computer will also tell you if you are out of tries

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')