# write a python program to swap two variables
a=input("Enter the value of the first variable (a): ")
b=input("Enter the value of the second variable (b): ")
print(f"Original Value: a={a}, b={b} ")
temp=a
a=b
b=temp
print(f"Swapped Values: a={a}, b={b}")
