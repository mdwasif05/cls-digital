# CALLING A FUNCTION IN PYTHON !
def fun():
    print("function have reusable property!")

fun()


# PYTHON FUNCTION ARGUMENTS !
def evenOdd(x: int) ->str:
   if (x % 2 == 0):
    return "EVEN"
   else:
    return "ODD"

print(evenOdd(10))
print(evenOdd(6))

# THE ABOVE FUNCTION CAN ALSO BE  DECLARED WITHOUT TYPE: HINTS LIKE THIS !
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

# DEFAULT ARGUMENT !
def myFun(x , y = 50):
   print("x: ", x)
   print("y: ", y)

myFun(20)

# KEYWORD ARGUMENTS(NAMED ARGUMENTS) !
def course(fname,lname):
   print(fname,lname)

course(fname="Data" , lname="Science")
course(fname="Data" , lname="Analytics")

# POSITIONAL ARGUMENTS !
def nameAge(name , age):
   print("Hi, I am", name)
   print("My age is", age)

print("CASE 1:")
nameAge("Mohammad Wasif" , 19)
print("\nCASE 2:")
nameAge(19 , "Mohammad Wasif")

# ARBITRARY KEYWORD ARGUMENTS !
# Example 1: Variable length non keyword arguments
def myFun(*argv):
   for arg in argv:
      print(arg)

myFun("Hello" , "Welcome" , "to" , "GeeksForGeeks")
# Example 2: Variable length keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

# DOCSTRING !
# Example: Add docstring to the function
def evenOdd(x):
   """Function to check if the number is even or odd"""

   if(x % 2 == 0):
      print("even")
   else:
      print("odd")

print(evenOdd.__doc__)

# PYTHON FUNCTION WITHIN  THE FUNCTION !
def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()

f1()

# ACRONYMOUS FUNCTION IN PYTHON !
def cube(x): return x*x*x       # without lambda

cube_1 = lambda x : x*x*x       # with lambda

print(cube(7))
print(cube_1(7))

# RETURN STATEMENT IN PYTHON EXPRESSION !
def square_value(num):
   return num**2

print(square_value(2))
print(square_value(-4))

# PASS BY VALUE AND PASS BY REFERENCE !
def myFun(x):
   x[0] = 20

list = [10, 11, 15, 13, 17]
myFun(list)
print(list)
# When we pass a reference and change the received reference to something else, the connection between the passed and received parameters is broken. For example, consider the below program as follows:
def myFun(x):
   x = [20, 30, 40]

list = [10, 11, 12, 15, 18]
myFun(list)
print(list)
# Exercise: Try to guess the output of the following Code
def swap(x, y):
   temp = x
   x = y
   y = temp

x = 2
y = 3
swap(x,y)
print(x,y)

# RECURSIVE FUNCTION IN PYTHON !
def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n-1)
   
print(factorial(4))