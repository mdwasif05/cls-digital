# Write a Python program to generate a random number
import random
print(f"Random Number:  {random.randint(1,100)}")
# Write a Python program to Convert Kilometres to Miles
kilometres=float(input("Enter the Distance in kilometres: "))
# Conversion factor 1 km = 0.621317 miles
conversion_factor=0.621317
miles = kilometres * conversion_factor
print(f"{kilometres} km is equals to {miles} miles")
# Write a Python Program to convert celsius into fahrenheit
celsius=float(input("Enter the temperature in celsius: "))
fahrenheit=(celsius * 9/5) + 32
print(f"{celsius} degree Celsius is equals to {fahrenheit} fahrenheit")
# Write a Python Program to display Calendar
import calendar
year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
cal=calendar.month(year,month)
print(cal)