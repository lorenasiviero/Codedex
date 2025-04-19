todo = ['🏦 Get quarters.', 
        '🧺 Do laundry.',
        '🌳 Take a walk.',
        '💈 Get a haircut.',
        '🍵 Make some tea.',
        '💻 Complete Lists chapter.',
        '💖 Call mom.',
        '📺 Watch My Hero Academia.']

print(todo[0])
print(todo[1])
print(todo[2 : 5])
print(todo[9]) # IndexError

#Index

## Lists: changeable sequence of items
# Index: item’s position in list (0-indexed; starts at 0)
# Negative indices: -1 last item; count backwards
# Slicing: list[start:end] returns items start (inclusive) to end (exclusive)
# Invalid index → IndexError: list index out of range

