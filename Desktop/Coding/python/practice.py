# Write a Python program to perform arithmetic addition and division operation
# division
num1=float(input("Enter the first number for addition: "))
num2=float(input("Enter the second number for addition: "))
sum_result=num1+num2
print(f"sum: {num1} + {num2} = {sum_result}")
# division
num3=float(input("Enter the first number for division: "))
num4=float(input("Enter the second number for division: "))
if num4==0:
    print("Error: Division by Zero is not allowed")
else:
    div_result=num3/num4
    print(f"Division: {num3} / {num4} = {div_result}")
# input the base and height from the user
base=float(input("Enter the length of the base of a Triangle: "))
height=float(input("Enter the height of the triangle: "))
area=0.5*base*height
print(f"Area of Triangle is: {area}")
