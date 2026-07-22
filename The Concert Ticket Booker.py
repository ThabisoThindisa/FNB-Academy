

#Get user input for name and band/artist they want to see
User_name = input("Enter your name: ")

track_number = 1
isRunning = True

#Loop to get more band/artist names
while isRunning == True:
    Band_name = input("Enter the name of the band/artist you want to see: ")
    print("             ") # Seperate the display
    print(f"Hey {User_name}!, Your tickets to see {Band_name} are booked successfully.")
    track_number += 1 