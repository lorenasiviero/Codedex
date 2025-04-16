# Magic 8 Ball
# This program simulates a Magic 8 Ball, which is a toy used for fortune-telling or seeking advice.

# Random
#___________________________________________
# In Python, modules are .py files containing Python code that can be imported into another program.
# The Python standard library includes over 200 modules that we can use.
#
# We can use the randint() function from the module called 'random' to generate a random number within a given range.
#
# First, we import the random module:
import random
#
# Next, we create a variable to store the randomly generated value.
# We declare a variable called 'num', and assign it the value from the function call:
num = random.randint(1, 9)
#
# The function random.randint(1, 9) generates a random number between 1 and 9 (inclusive of both endpoints).
#
# You can print the number to see the randomly generated value:
print(num)



import random

question = input("What is your question? ")

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Magic 8 Ball:  ' + answer)