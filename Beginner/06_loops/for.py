# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Solution 1:
#print(round(int(sum(student_heights)) / int(len(student_heights))))

#Solution 2:
sumOfStudents = 0
countStudents = 0

for heights in student_heights:
  sumOfStudents += int(heights)
  countStudents += 1

print(round(sumOfStudents / countStudents))