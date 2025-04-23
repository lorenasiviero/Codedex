#Mixtape

#For-in loop: 
#For-in loops are used to iterate over a sequence (like a list, tuple, or string) in Python.

#Example:
#snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]
#for i in snowfall:
#  print(i)
#  # Output: 0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8

#For-in with range() and len():
#The range() function generates a sequence of numbers, which can be used to iterate over with a for loop.
#The len() function returns the number of items in an object, such as a list or string.
#Example:
#snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]
#for i in range(len(snowfall)):
#  print(snowfall[i])
#  # Output: 0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8



#💿 Theme: My 2015 Era

playlist = ['Silverstein - Smile in Your Sleep',
            'My Chemical Romance - Helena',
            'Pierce the Veil - Hell Above',
            'Fit for Rivals - Damage',
            'Bring Me the Horizon - Can You Feel My Heart',
            '30 Seconds to Mars - The Kill',
            'A Day to Remember - Mr. Highway\'s Thinking About the End',
            'Soundgarden - Black Hole Sun',
            'Deftones - Be Quiet and Drive',
            'Bullet for My Valentine - Hearts Burst Into Fire',
]

#For-in loop:
for(i) in  playlist:
    print(i)

#For-in with range() and len():
for(i) in range(len(playlist)):
    print(playlist[i])