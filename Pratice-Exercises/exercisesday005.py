"""
Activity
Write a program that asks for a data collection type from user and creates 
that data collection with minimum 3 data items and print it
"""
#input()

firstname = input("enter your first name: ")
lastname = input("enter your last name: ")
dob = input("enter your date of birth: ")
address = input("enter your address: ")

user = {
    "firstname" : firstname,
    "lastname" : lastname,
    "dob" : dob,
    "address" : address
}

print(user)

