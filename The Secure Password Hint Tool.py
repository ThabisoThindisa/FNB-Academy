
secret_password = input("Enter the password: ")
secret_password = secret_password.strip() 

#Store the password
print(f"Your password hint: It starts with {secret_password[0]} and ends with {secret_password[-1]}")