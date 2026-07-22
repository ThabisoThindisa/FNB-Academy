#Practical Task 1: Write a Python script called student_info.py that collects personal 
# information from the user and displays it in a formatted profile card. The program 
# must demonstrate correct use of all four data types, string manipulation, arithmetic, 
# and the f-string output format.

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

print(f"\nWelcome, {first_name.upper()} {surname.upper()}")
print(f"Hello, {first_name.title()} {surname.title()}")
display_age = age * 12
print(f"Round the favourite number to 2 decimal places: {favourite_number:.2f}")
print(f"You are {display_age} months old.")
  