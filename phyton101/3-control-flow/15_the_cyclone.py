# The Cyclone

#Logical Operators
#___________________________________________
# Logical operators are used to combine conditional statements.
# In Python, the logical operators are:
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Returns True if the statement is false
#
# The Cyclone
# This program checks if a person is tall enough and has enough credits to ride the Cyclone.
# The Cyclone is a roller coaster at Coney Island, New York.
# The height requirement is 137 cm, and the ride costs 10 credits.


height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif credits < 10 and height >= 137:
  print("You don't have enough credits to ride.")
else:
  print("You are not tall enough for this ride, nor do you have enough credits.")