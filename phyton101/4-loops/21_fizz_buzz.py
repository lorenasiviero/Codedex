# FizzBuzz is a classic programming problem that is often used in coding interviews.
# The task is to print the numbers from 1 to 100, but for multiples of 3 print "Fizz" instead of the number,
# and for the multiples of 5 print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# The solution uses a for loop to iterate through the numbers from 1 to 100.
# The modulo operator (%) is used to check if a number is divisible by another number.
# The code uses if-elif-else statements to determine what to print for each number.

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)