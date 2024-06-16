"""
#   File link: file:///C:/Users/LENOVO-LOQ1/OneDrive/Documents/SkillsCity%20-%20Content/Week1/Week%201%20-%20Day%205/1.2.3%20Introduction%20to%20SE%20-%20Python%20-%20Data%20Collection%20Types.pdf

Python Lists
Lists are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.
List items are indexe
"""

"""
ORDERED
 When we say that lists are ordered, it means that the items have a defined 
order, and that order will not change.
 If you add new items to a list, the new items will be placed at the end of the 
list.
Changeable
The list is changeable, meaning that we can change, add, and remove items 
in a list after it has been created.

"""
# Add Item to list

#append()

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert item to list
#insert() 

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend list
#extend() -> to append elements from another list to the current list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Remove item from list
#remove()

thislits = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry', 'mango', 'pineapple', 'papaya']

#Remove Specified Index
#pop()

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']

#Remove Specified Index
#pop() -> withput any index
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove item from list
#del

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist) # ['apple', 'cherry']

#Delete the list
#del
thislist = ["apple", "banana", "cherry"]
del thislist #delete from memory

#length of a list
#Len()

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Python Tuples
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and #unchangeable.
Tuples are written with #round brackets.

"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#To create a tuple with only one item, you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.

thistuple = ("apple", )
print(type(thistuple)) # class tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "papaya"
x = tuple(y)
print(x)

"""
Python Sets
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
#do not allowed duplicated values
Sets are written with curly brackets.
{ }

"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

#do not allow duplicate values
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, False, 0, 2}
print(thisset)

#  add() , remove()

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset.remove("banana")
print(thisset)

"""
Dictionaries are used to store data values in key:value pairs.
 A dictionary is a collection which is ordered*, changeable and do not allow 
duplicates.
 Dictionaries are written with curly brackets, and have keys and values
"""
thisdict = {
    "name": "Karina RP",
    "designation": "Student",
    "year": 2024
}
print("dict:", thisdict)

#Access
thisdict = {
    "name": "Karina RP",
    "designation": "Student",
    "year": 2024
}
print("dict:", thisdict["name"])

#  As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, 
# dictionaries are unordered.

#Changeable
thisdict["name"] = "New Name"

# Duplicates Not Allowed
thisdict = {
    "name": "Karina RP",
    "designation": "Student",
    "year": 2024,
    "year": 2024 #do not allow duplicate
}
print(thisdict["name"])

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

#Add Item to the dictionary
thisdict = {
    "name": "Muhammed Aziz",
    "designation": "Instructor",
    "year": 2024
}

thisdict["organization"] = "skill city"
print(thisdict)

#Remove Item from the dictionary
thisdict = {
    "name": "Muhammed Aziz",
    "designation": "Instructor",
    "year": 2024
}

thisdict.pop("year")
print(thisdict)
# thisdict["year"] = 2024 -> to add
# print(thisdict)

#popitem()
thisdict = {
    "name": "Muhammed Aziz",
    "designation": "Instructor",
    "year": 2024
}
thisdict.popitem() #delete the last column
thisdict.popitem()
thisdict.popitem()
print(thisdict)

"""
Python Nested Dictionaries. A dictionary can contain dictionaries, this is called nested dictionaries.
"""

myfamily = {
 "child1" : {
 "name" : "Emil",
 "year" : 2004
 },
 "child2" : {
 "name" : "Tobias",
 "year" : 2007
 },
 "child3" : {
 "name" : "Linus",
 "year" : 2011
 }
 }

print(myfamily)

