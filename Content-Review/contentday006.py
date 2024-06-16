# Iteration in coding

#Iteration is the repetition of a process in a computer program, usually done with the help of loops.

# Two types of loops: For Loops and While Loops

# For Loops
# The for loop repeats part of the programa based on a sequence, an ordered list of things
# A for loop repetas through each element of a sequence in order, when it reaches the end of the sequence the loop ends.

#For loop example

coffee_order = ["americano", "cortado", "espresso", "cappuccino"]

for i in coffee_order:
    print(i)

#For loop example using range

for i in range(10): # i stands for index, but can be any name # range(10) means 0-9
    print(i)

for i in range(0,10): #First value is the start position
    print(i)

for i in range(0, 10, 2): #second value is stop position (not including 10)
    print(i)

for i in range(0,10,2): #third value is "step", by default it is 1
    print(i)

"""
Create a list of 4 favourite countries to visit.
 Use a for loop to show each country in the list.
 if the 3rd country in the list is Spain.
 If it is print  “Yaaay Spain is 3rd in your list of favourite countries”. 
If it isn’t print “Boo, I can’t believe Spain isn’t your 3rd favourite 
country!”"""

favouriteCoutries = ["Brasil", "Spain", "Portugal", "Greek"]

for index, country in enumerate(favouriteCoutries, start=1):
    if index == 3:
        if country == "Spain":
            print("Yaaay Spain is 3rd in your list of favourite countries")
        else:
            print("Boo, I can’t believe Spain isn’t your 3rd favourite country!")
    else:
        print(country)

"""
Activity 2:
If you can create a for loop to output 0-9, how can you create 
one to count backwards 9-0? You will have to use your research 
skills to find out how to do this. 
"""

for i in range(9, -1,-1):
    print(i)

"""
In this range() function:
The first argument 9 is the start value.
The second argument -1 is the end value (exclusive), meaning the loop will stop before reaching -1.
The third argument -1 is the step value, indicating that the loop should decrement by 1 each time.
When you run this code, it will print the numbers from 9 down to 0 in descending order.
"""

for i in range(5):
    print("Karina")

# While Loops:
# The while loop can execute a set of statements as long as a condition is True.

num = 0
while num < 10: # The while loop only runs whilst this statement is True
    num += 1 # Adds 1 to num variable. Once num becomes >=10, the statement is no longer True so the while loop stops
    print(num)

# while statement_is_true:
#do this

"""
I want to generate a random 
number until a certain integer 
is found

I can’t use a for loop because I 
don’t know how many times 
the loop will have to iterate…..
 So I’m going to use a while loop

"""

import random

rand_num = random.randint(0,50)
my_num = 50

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,50)

print(f"You found my number! {my_num}")

"""
Activity 3

Create a for loop that outputs “Hello World” 12 times. 
Now convert this into a while loop that does the same thing.

"""
for i in range(12):
    print("Hello World")

count = 0
while count < 12: 
    count +=1
    print("Hello World")
