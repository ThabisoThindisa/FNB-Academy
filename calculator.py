

#---------------Multi-Function Calculator------------------

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))


if second_number == 0:
    print("Sorry but the second number can not be zero! ")

else:
 C_addition = first_number + second_number
 C_subtraction = first_number - second_number
 C_multiplication = first_number * second_number
 C_division = first_number / second_number
 C_floor_division =first_number // second_number
 C_modulus = first_number % second_number

 print(f"\nAddition Ans: {round(C_addition,2)}")
 print(f"subtraction Ans: {round(C_subtraction,2)}")
 print(f"multiplication Ans: {round(C_multiplication,2)}")
 print(f"division Ans: {round(C_division,2)} \n")

 print(f"floor division Ans: {round(C_floor_division,2)}")
 print(f"modulus Ans {round(C_modulus,2)}")