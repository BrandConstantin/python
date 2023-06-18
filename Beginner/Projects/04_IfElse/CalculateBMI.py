# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
message = (f"Your BMI is {bmi}, you are ")

if(bmi < 18.5):
    print(message + "underweight")
elif(bmi >= 18.5 and bmi < 25):
    message = (f"Your BMI is {bmi}, you have a ")
    print(message + "normal weight.")
elif(bmi >= 25 and bmi < 30):
    print(message + "slightly overweight.")
elif(bmi >= 30 and bmi < 35):
    print(message + "obese.")
else:
    print(message + "clinically obese.")