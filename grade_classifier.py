
#Build a student grade classifier called grade_classifier.py that takes a learner’s name 
# and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail),
# and displays a full report card. The program must correctly use conditionals for all grade and status logic.

Learner_name = input("What is your name: ")

#input marks
L_Maths = int(input("What are the marks for Mathematics: "))
L_Sepedi = int(input("What are the marks for Sepedi: "))
L_English = int(input("What are the marks for English: "))

#Store the data
L_Subjects = {
    "Maths": L_Maths, 
    "Sepedi": L_Sepedi, 
    "English": L_English
    }

#Store user info
L_info = {"Learner name": Learner_name }

# Must be in the range of [0 to 100]
#if (L_Maths >= 0 and L_Sepedi >= 0 and L_English >= 0) and (L_Maths <= 100 and L_Sepedi <= 100 and L_English <= 100):
if all(0 <= mark <= 100 for mark in L_Subjects.values()):    
    #Store the data
    L_Subjects = {"Maths": L_Maths,
                   "Sepedi": L_Sepedi,
                     "English": L_English}

    # Calculate the average mark across the three subjects
    Cal_Average = sum(L_Subjects.values()) // 3
    
    L_info.update({"Subjects": L_Subjects, "Avarage mark": Cal_Average})

    # Assign grade
    if L_info.get("Avarage mark") >= 80:
        L_info.update({"Grade:": "A","Pass status": "Yes"
                       ,"needs intervention:": "No"})
    elif L_info.get("Avarage mark") >= 70 and L_info.get("Avarage mark") <= 79:
        L_info.update({"Grade:": "B","Pass status": "Yes",
                       "needs intervention:": "No"})
    elif L_info.get("Avarage mark") >= 60 and L_info.get("Avarage mark") <= 69:
        L_info.update({"Grade:": "C","Pass status": "Yes",
                       "needs intervention:": "No"})
    elif L_info.get("Avarage mark") >= 50 and L_info.get("Avarage mark") <= 59:
        L_info.update({"Grade:": "D","Pass status": "Yes",
                       "needs intervention:": "No"})
    elif L_info.get("Avarage mark") >= 40 and L_info.get("Avarage mark") <= 49:
        L_info.update({"Grade:": "F","Pass status": "No",
                       "needs intervention:": "No"})
    else:
        L_info.update({"Grade:": "F","Pass status": "No",
                       "Needs intervention:": "Yes"})
        
    print(L_info)
else:
    print("You entered incorrect mark!")     
 