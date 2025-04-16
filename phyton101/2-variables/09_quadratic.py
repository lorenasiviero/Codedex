# Quadratic Equation Solver
# The quadratic equation is of the form ax^2 + bx + c = 0
# The program calculates the roots of the quadratic equation using the quadratic formula:
# x = (-b ± √(b² - 4ac)) / (2a)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1= (-b + (b**2 - 4*a*c)**0.5) / (2*a)
root2= (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)