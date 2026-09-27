# Write a Python Program to solve Quadratic equations
import math
# input variables
a=float(input("Enter Coefficient a: "))
b=float(input("Enter Coefficient b: "))
c=float(input("Enter Coefficient c: "))
# Calculate the discriminant
discriminant=b**2 - 4*a*c
# Check if the descriminant is positive, negative or zero
if discriminant>0:
    # Two real and distinct root
    root1=(-b + math.sqrt(discriminant)) / (2*a)
    root2=(-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant==0:
    # One real root(repeated)
    root=-b / (2*a)
    print(f"Root: {root}")
else:
    # Complex root
    real_root= -b / (2*a)
    imaginary_root= math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_root} + {imaginary_root}i")
    print(f"Root 2: {real_root} + {imaginary_root}i") 
# Write a Python Program to swap two number without temp variable
a = 10
b = 50
print(f"Original Value of a = {a} and b = {b}")
a,b=b,a
print("After Swapping")
print(f"a = {a} and b = {b}")   
    
