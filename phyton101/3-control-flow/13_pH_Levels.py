# Relational Operators
# ---------------------
# Use these operators to compare two values:
#   ==  (equal to)
#   !=  (not equal to)
#   >   (greater than)
#   <   (less than)
#   >=  (greater than or equal to)
#   <=  (less than or equal to)

# Elif
# ----
# Use 'elif' (short for 'else if') to check additional conditions between an if and an else.
# It allows you to create multiple condition checks within a decision structure.

pH = int(input("Enter the pH level: "))
if pH < 0 or pH > 14:
    print("Invalid pH level")
elif pH < 7:
    print("Acidic")
elif pH == 7:
    print("Neutral")
else:
    print("Basic")