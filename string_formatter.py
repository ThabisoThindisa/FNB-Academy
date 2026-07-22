#Write a Python script called string_formatter.py that takes a user’s first name, last name, and a 
# short bio message as input, then applies multiple string transformations to produce a formatted 
# user profile output.This simulates how a real app backend processes user-submitted text.

#Remove the leading and trailing whitespace from the input strings using the strip() method.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

#Get the bio message input
bio_message = input("Enter a short bio message: ").strip()
Username = first_name[0]+ last_name
print(f"{first_name.title()} {last_name.title()} ")

#Count and display the number of characters in the bio 
Bio_length = len(bio_message)
print(f"Bio message length: {Bio_length} characters")

#Replace any occurrence of ‘I am’ in the bio with ‘I’m
bio_message = bio_message.replace("I am", "I'm")
print(f"Formatted Bio: {bio_message}")