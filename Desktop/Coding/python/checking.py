"""letter=input("Enter a letter here: ")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("Entered letter is Vowel")
else:
    print("Not a Vowel")"""

num=int(input("Enter a number here upto 5 digits: "))
if num>=0 and num<=9:
    print("Single Digit Number")
elif num>=10 and num<=99:
    print("Double Digit Number")
elif num>=100 and num<=999:
    print("Three Digit Number")
elif num>=1000 and num<=9999:
    print("Four Digit Number")
else:
    print("It is a five digit number")
# Write a Python Program to check number is positive negative or zero
num1=float(input("Enter a Number: "))
if num1 > 0:
    print(f"{num1} is a Positive Number")
elif num1 == 0:
    print("Zero")
else:
    print(f"{num1} is a Negative Number")
# Write a Python Program to check if a Number is odd or even
num2=float(input("Enter a NUmber: "))
if num2 % 2 == 0:
    print(f"{num2} is an Even Number")
else:
    print(f"{num2} is an Odd Number")
# Write a Program to check Leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")