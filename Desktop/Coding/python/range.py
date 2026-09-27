# The built-in range() function returns an immutable sequence of numbers, commonly used for looping
#  a specific number of times.
# Creating Ranges
# The range() function can be called with 1, 2, or 3 arguments, using this syntax:
# range(start, stop, step)
# Call range() with one argument
x = range(10)
print(x)
print(list(x))
# Call range() with two argument
y = range(3,10)
print(y)
print(list(y))
# Call ramge() with three argument
z = range(1,10,2)
print(z)
print(list(z))
# Using Ranges
# Ranges are often used in for loops to iterate over a sequence of numbers.
for i in range(10):
   print(i)
# Using List to display ranges
print(list(range(5)))
print(list(range(2,8)))
print(list(range(5,12,3)))
# Slicing Range
r = range(5)
print(r[2])
print(r[:2])
# Membership Testing
b = range(0, 10, 2)
print(6 in b )
print(7 in b)
print(list(b))
# Ranges support the len() function to get the number of elements in the range.
print(len(b))

