# 99 Bottles of Beer on the Wall
# This program prints the lyrics to the song "99 Bottles of Beer on the Wall"

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')