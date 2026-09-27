thislist=["Apple","Banana","Cherry"]
print(thislist)
# List items are ordered, changeable, and allow duplicate values.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list4=["abc",123,True,"male"]
print(list4)
print(type(list4))
# It is also possible to use the list() constructor when creating a new list.
thatlist = list(("Apple","Banana","Cherry"))
print(thatlist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
mylist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[:4])
print(mylist[2:])
print(mylist[-4:-1])
# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in mylist:
    print("yes 'apple' is in the fruit lists")
# Change Item Value
# To change the value of a specific item, refer to the index number:
youlist=["apple","banana","cherry"]
youlist[1]="orange"
print(youlist)
# if you want to change the range of item values
thislist[1:3]=["blackberry","jelly"]
print(thislist)
list5=["apple","banana","cherry"]
list5[1:3]=["watermelon"]
print(list5)
# The insert() method inserts an item at the specified index:
list6=["apple","banana","cherry"]
list6.insert(2,"watermelon")
print(list6)
# To add an item to the end of the list, use the append() method:
list7=["apple","banana","cherry"]
list7.append("orange")
print(list7)
# The remove() method removes the specified item.
list8=["apple","banana","cherry"]
list8.remove("banana")
print(list8)
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
list9=["apple","banana","cherry","banana","kiwi"]
list9.remove("banana")
print(list9)
# The pop() method removes the specified index.
list10=["apple","banana","cherry"]
list10.pop(1)
print(list10)
# If you do not specify the index, the pop() method removes the last item.
list11=["apple","banana","cherry"]
list11.pop()
print(list11)
# The del keyword also removes the specified index:
list12=["apple","banana","cherry"]
del list12[0]
print(list12)
# The del keyword can also delete the list completely.
list13=["bmw","volvo","benz"]
del list13
# The clear() method empties the list.
# The list still remains, but it has no content.
list14=["pencil","notebook","bag"]
list14.clear()
print(list14)
# You can loop through the list items by using a for loop:
mycar=["scorpio","fortuner","swift"]
for x in mycar:
    print(x)
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
myday=["sunday","monday","tuesday"]
for i in range(len(myday)):
    print(myday[i])
# The iterable created in the example above is [0, 1, 2].
thislist1 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist1):
  print(thislist1[i])
  i = i + 1
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Python - List Comprehension
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# With list comprehension you can do all that with only one line of code:
fruits1=["apple","banana","cherry","mango","kiwi"]
newlist=[x for x in fruits1 if "a" in x]
print(newlist)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits2 if x != "apple"]

print(newlist1)

fruits3= ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits]

print(newlist2)

fruits4 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist3 = [x.upper() for x in fruits4]

print(newlist3)

fruits5=["apple","banana","cherry","mango","kiwi"]
newlist4=['hello' for x in fruits5]
print(newlist4)

fruits6 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist5 = [x if x != "banana" else "orange" for x in fruits6]

print(newlist5)
