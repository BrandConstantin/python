student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
#print(student_scores["Harry"])  #81
#print(student_scores.keys())    #Harry, Ron, etc
#print(student_scores.values())  #81,78, etc
#print(student_scores.items())   #('Harry', 81) etc

for student in student_scores:
    grades = ""
    scores = student_scores[student]

    if scores >= 91 and scores <= 100:
        grades = "Outstanding"
    elif scores >= 81 and scores <= 90:
        grades = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        grades = "Acceptable"
    else:
        grades = "Fail"
    
    student_grades[student] = grades
    

# 🚨 Don't change the code below 👇
print(student_grades)