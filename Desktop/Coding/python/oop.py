class myclass:
    x = 5
p1 = myclass()
print(p1.x)
# The __init__() Method
# The examples above are classes and objects in their simplest form, and are not really 
# useful in real life applications.
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
p1 = Person("Wasif",19)
print(p1.name)
print(p1.age)
# Note: The __init__() method is called automatically every time the class is being used to create a new object.
# The __str__() Method
# The __str__() method controls what should be returned when the class object is represented as a string.
# If the __str__() method is not set, the string representation of the object is returned:
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    s1 = Student("John",17)
    print(s1)
