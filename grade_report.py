
#----------------------Global variables -------------------------
isRunning = True
Students_List = []

#-------------------Helping functions-----------------------------
def Give_Grade(avarage):
   #Calculate the average mark across the three subjects
   #1. Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
   #2. Assign Pass status if the average is 50 or above, Fail otherwise
   #3. Flag any individual subject mark below 40 as ‘needs intervention’
   #4. Display a formatted report card showing all inputs, the average, the grade, the status,
   #  and any intervention flags
    
    
   if avarage < 40:
      Stutus = {"Grade": "F", "Intervation": "Yes" }
      return Stutus
   elif avarage >= 40 and avarage < 50 :
      Stutus = {"Grade": "F", "Intervation": "No" }
      return Stutus
   elif avarage >= 50 and avarage <= 59:
     Stutus = {"Grade": "D", "Intervation": "No" }
     return Stutus
   elif avarage >= 60 and avarage <= 69:
     Stutus = {"Grade": "C", "Intervation": "No" }
     return Stutus     
   elif avarage >= 70 and avarage <= 79:
     Stutus = {"Grade": "B", "Intervation": "No" }
     return Stutus 
   elif avarage >= 80:
     Stutus = {"Grade": "A", "Intervation": "No" }
     return Stutus 

def CalC_Class_Average():
   
   #initialise the variables
   Class_av = 0
   total = 0
   num_students =0

   for student in Students_List:
       total += student["average"]
       num_students +=1
   
   if num_students > 0:
       Class_av =total /num_students
       return round(Class_av,1)
   else:
      print("---- No students available ----")
def Calc_Highest():
   #initialise the variables
   Highest = 0

   for student in Students_List:
       if student["average"] > Highest:
          Highest = student["average"]
  
   return Highest
def Calc_Lowest():
   
   #Compare with the highest
   lowest_mark = Calc_Highest()

   for student in Students_List:
       if student["average"] < lowest_mark:
          lowest_mark = student["average"]

   return lowest_mark

     #-----------------------------------The main rogram ------------------------------------------
def DisplayAll():
   index = 1
   print("\n------ Display all students information------")
   for temp_student in Students_List:
      #dislay student info
      print(f"{index}. name: {temp_student["Name"]} ")
      print(f"Maths: {temp_student["maths"]} ")
      print(f"English: {temp_student["english"]} ")
      print(f"Science: {temp_student["science"]} ")
      print(f"Average: {temp_student["average"]} ")
      print(f"Grade: {temp_student["Grade"]} ")
      print(f"Intervation: {temp_student["Intervation"]} ")
      index +=1 
      print("------------------")  
def Search_Student(name):
   isFound = False
   for student in Students_List:
      if student["Name"] == name.strip(),:
         print("\n------Searching-----")
         print(f"Student name: {student["Name"]} ")
         print(f"Maths: {student["maths"]} ")
         print(f"English: {student["english"]} ")
         print(f"Science: {student["science"]} ")
         print(f"Average: {student["average"]} ")
         print(f"Grade: {student["Grade"]} ")
         print(f"Intervation: {student["Intervation"]}\n ")
         isFound = True

         print("------")
         break
  
   if(isFound !=True):
      print("Error: Student not found! ") 

while isRunning:
    try:
        num_Students = int(input("\nEnter number of students: "))

        if num_Students > 2: # Store at least 5 students as a list of dictionaries
            for index in range(0, num_Students):
                # Student info
                Stu_name = input(f"\nWhat is the student ({index+1}) name: ")
                maths_Marks = int(input("1. Maths marks: "))
                English_Marks = int(input("2. English marks: "))
                Science_Marks = int(input("3. Science marks: "))

                # Check if the user entered a number
                # within range of 0 and 100
                if all(0 <= mark <= 100 for mark in [maths_Marks, English_Marks, Science_Marks]):
                    # calculate the student marks
                    Mark_average = (maths_Marks + English_Marks + Science_Marks) // 3

                    Current_Student = {
                        "Name": Stu_name.strip(),
                        "maths": maths_Marks,
                        "english": English_Marks,
                        "science": Science_Marks,
                        "average": Mark_average
                    }

                    # update student info
                    uptated_Student = Current_Student | Give_Grade(Mark_average) # combine
                    Students_List.append(uptated_Student)  # Add the student
                
                else:
                    print("---- please enter least 5 students -----")


            print(f"\n------ Students -----")
            DisplayAll()
            print(f"\nClass avareage is: {CalC_Class_Average()}")
            print(f"Class Highest mark is: {Calc_Highest()}")
            print(f"Class Lowest mark is: {Calc_Lowest()}")

            str_Search =input("Search for the student by name: ")
            Search_Student(str_Search)

        else:
          print("---- please enter least 5 students -----")
    except:
        print("An exception occurred, try again! ")
      



   

         
      