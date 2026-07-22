
Contact_List = []  # initialise list of contact dictionaries

def add_contact():
    C_name = input("\nWhat is the name of the contact: ")
    C_phoneNum = input(f"What is the phone number of {C_name}: ")
    C_Email = input(f"What is the Email of {C_name}: ")
    User_contact = {"Name": C_name, "Phone": C_phoneNum, "Email": C_Email}

    #Store the contact
    Contact_List.append(User_contact)
    return Contact_List

def search_contact(name):
    
    for contact in Contact_List:
        if contact.get("Name") == name:
            print("Found:", contact)
            return contact
            break
        else:
            print("Contact not found")
    return None

def delete_contact(name):
    
    for de_contact in Contact_List:

        if de_contact.get("Name") == name:  
            Contact_List.remove(de_contact)
            print(f"\nContact {de_contact.get("Name")} is deleted.")
            break

        else:
            print("Delete unsuccessful. ")   
def ViewContacts():
    count =1
    print("\n ----- The available contacts store ----- ")
    for tempContact in Contact_List:
     
        print(f"\nContact number {count}")
        print(f"# Name: {tempContact.get("Name")} ")
        print(f"# Phone {tempContact.get("Phone") }")
        print(f"# Email: {tempContact.get("Email") }")
        count +=1


isRunning = True
while isRunning:
    U_option = int(input("----------------\nchoose an action " \
    "\n(1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit) : "))

    if U_option == 1: #Add
       
       # Add the contact list
       Num_add = int(input("How many contacts do you want to add: "))
       
       for number in range(0,Num_add): 
           add_contact()

    elif U_option == 2: # Search the contact in list
         print("\n-----------Search--------")
         S_name = input("Which contact do you want to Search : ")
         search_contact(S_name)     

    elif U_option == 3:    #delete 
        print("\n-----------Delete--------")
        D_name = input("Which contact do you want to delete : ")
        delete_contact(D_name)

    elif U_option == 4: #view
         ViewContacts()    

    elif U_option == 5: # Stop the program
        print("###### Thanks for using the program, Goodby! ######")
        isRunning = False

    else:
        print("Incorect choice, try again !")         

  