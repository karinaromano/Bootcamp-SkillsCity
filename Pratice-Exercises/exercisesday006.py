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

"""
Activity 4:

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

"""
Create a while loop to randomly cycle through a list of cards until 
a given card is found.

cards=[“Diamond”, “Spade”, “Club”, “Heart”]

Create a variable called current_card and use a list method to 
randomly give it a value from the list every time the loop runs. 
Then compare this to the card you want to find to stop the while 
loop.

"""

