# Sorting Hat Quiz
# This is a simple quiz to determine which Hogwarts house you belong to.
# The quiz consists of a series of questions, and based on your answers, you will be sorted into one of the four houses: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.
# The houses are represented by the following emojis:
# Gryffindor: 🦁
# Hufflepuff: 🦡
# Ravenclaw: 🦅
# Slytherin: 🐍



gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~
print("Q2) When I'm dead, I want people to remember me as:")
print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')
answer = int(input('Enter answer (1-4): '))
if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~
print("Q3) What kind of instrument most pleases your ear?")
print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')
answer = int(input('Enter answer (1-4): '))
if answer == 1:
  slytherin += 4
elif answer == 2:
   hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print('Wrong input.')

#Bonus
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
print('====================')
print('Thanks for playing!')
print('====================')


   