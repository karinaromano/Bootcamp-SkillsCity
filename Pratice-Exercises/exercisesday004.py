#  If Statement 
"""
Exercise 1: Check if the number is even.
Define the number you want to check in “Num” variable. e.g.: Num = 6 
→ Use the modulo operator (%) to check if the number is divisible by 2. e.g.: if Num % 2 == 0: 
→ If the remainder is 0, the number is even. Print a message indicating that. e.g.: print(‘The 
number is even.’) 
"""

num = 10
if num % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

"""
Exercise 2: Display a message if a list is empty. 
 
→ Define the list you want to check in “my_list” variable. e.g.: my_list = [ ] 
→ Check the length of the list e.g.: if len(my_list) == 0: 
→ If the length is 0, the list is empty. Print a message indicating that. e.g.: print ('list is 
empty') 
"""
my_List = []
if len(my_List) == 0:
    print("list is empty")
else:
    print(my_List)

#else Statement

"""
Exercise 1: Write a script to check if a number as odd or even. 
 
→ Define the number you want to check in “Num” variable e.g.: Num = 6 
→ Use the modulo operator (%) to check if the number is divisible by 2. e.g.: if Num % 2 == 0: 
→ If the remainder is 0, the number is even. Print a message indicating that. e.g.: print(‘The 
number is even.’) 
→ If the condition in step 2 is false (i.e., the number is odd), print a message indicating that. 
"""
num = 8
if num % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

# elif Statement

"""
Exercise 1: Write a script for Temp categories. 
Define the temperature in “temp” variable. e.g.: temp = 15.07
Check if the temperature is less than or equal to 0 degrees. e.g.: if temp <= 0:
If true, it means the temperature is freezing. Print a message indicating that. e.g.: print(‘Its 
Freezing Colddd!’) 
Else if the temperature is less than 10 degrees, e.g.: elif temp <= 10: 
If true, it means the temperature is cold. Print a message indicating that. e.g.: print(‘Its 
Cold’) 
→ You can add as many elif statements.  
→ Else if the temperature is less than 20 degrees, e.g.: elif temp <= 20: 
→ If true, it means the temperature is moderate. Print a message indicating that. e.g.: 
print(‘Its Moderate’) 
→ Else if the temperature is less than 25 degrees, e.g.: elif temp <= 25: 
→ If true, it means the temperature is warm. Print a message indicating that. e.g.: print(‘Its 
warm’) 
→ Else none of the above conditions are met (i.e., the temperature is 35 degrees or higher), 
it means that the temperature is hot. Print a message indicating that. e.g.:  
else: 
print(‘Its Hotttt!’)

"""
temp = 10
if temp <= 0:
    print("Its Freezing Colddd!")
elif temp < 10:
    print("Its Cold")
elif temp < 20:
    print("Its Moderate")
elif temp < 25:
    print("Its warm")
elif temp < 35:
    print("Its hot")
else:
    print("Its hot")

# for Loop

"""
Exercise 1: Print each character in a string. 
→ Define the string in “string” variable. e.g.: string = ‘Hello, World’ 
→ Use for loop to iterate through each character in the string. e.g.: for char in string: 
→ Print each character in the string during each iteration of the loop. e.g.: print(char) 
"""
string = "Hello World"
for x in string:
    print(x)

"""
Exercise 2: Create a list of squares of the first 10 natural numbers. 
→ Generate a list of squares of the first 10 natural numbers by iterating each value “I” in the 
range from 1 to 10 (inclusive) and calculates its square i ** 2. The resulting squares are 
collected into a list called squares. e.g.: squares = [i ** 2 for i in range(1, 11)] 
→ Print the list. e.g.:  print(squares) 
"""
squares = [ i ** 2 for i in range(1,11)]
print(squares)

# While Loop

"""
Exercise 1: Add numbers until sum reaches 100. 
→ Start by initializing two variables “total_sum” to keep track of the sum of numbers and 
“current_number” to represent the current number to be added. e.g.:  
total_sum = 0 
current_number = 1 
→ Use a while loop to add numbers until the “total_sum” reaches or exceeds 100. Inside the 
loop:  
• Add the “current_number” to the “total_sum”. 
• Increment the “current_number” by 1. e.g. 
"""
total_sum = 0
current_number = 0
while total_sum <= 100:
    total_sum += current_number
    current_number +=1

print("The sum of numbers until reaching 100 is: ", total_sum)

#added this line only for pratice

