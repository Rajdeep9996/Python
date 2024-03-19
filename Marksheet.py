# Marksheet for Six subjects

subject1 = float(input("Enter Marks for Subject 1: "))
subject2 = float(input("Enter Marks for Subject 2: "))
subject3 = float(input("Enter Marks for Subject 3: "))
subject4 = float(input("Enter Marks for Subject 4: "))
subject5 = float(input("Enter Marks for Subject 5: "))
subject6 = float(input("Enter Marks for Subject 6: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5 + subject6

parcentage = (total_marks / 600) * 100

if parcentage >= 60:
    division = "1st Division"
elif parcentage >= 45:
    division = "2nd Division"
elif parcentage >= 30:
    division = "3rd Division"
else:
    division = "Fail"

print("Division is: ", division)