
#---------- Global variables ---------------
All_Contacts = []

#-------------------Helping function------------------

def Search_Contact(name):
   result = {}
   for contact in All_Contacts:
       if contact["name"].lower() == name.lower():
           result = contact
           print(f"Found! {result["name"]}’s number is {result["number"]} \n")
           break
   return result   

def CheckIfPresent(contact):
    check_Flag = False
    for tempContact in All_Contacts:
        if tempContact["name"] == contact["name"] and tempContact["number"] == contact["number"] :
            check_Flag = True
            #break
    return check_Flag  

#----------------- Main program -----------------------
#try:
for index in range(1,4): #Fill it with 3 people 
       Friend_name = input(f"\nEnter friend {index} name: ").strip()
       Friend_number = input("Enter friend number: ").strip()
       current_contact = {'name':Friend_name,'number':Friend_number}

       if(CheckIfPresent(current_contact) == False):
           All_Contacts.append(current_contact)
       else:
           print (f"\nContact for {Friend_name} already exist \n")


print("\n------------Search contact ---------------")
S_name = input("Type name to Search: ")
Result = Search_Contact(S_name)
if Result is None:
    print("\n# Fail: Contact not found.")   
else:
     print(f"# Pass: Contact is found.\nName: {Result['name']}\nNumber: {Result['number']}")

#except Exception as e:
    #print(f"Error occured during run time.")    