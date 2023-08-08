#Calculator

# add 
def add(num1, num2):
  return num1 + num2
  
# substract
def substract(num1, num2):
  return num1 - num2
  
# multiply
def multiply(num1, num2):
  return num1 * num2
  
# divide
def divide(num1, num2):
  return num1 / num2

## Operations
num1 = int(input("What is the first number that you wanna use? "))
num2 = int(input("What is the second number that you wanna use? "))

result = 0
operationString = ""

operation = input("What operation you wanna do? (A. add / S. substract / M. multiply / D. divide) ").upper()

if operation == "A":
  result = add(num1, num2)
  operationString = "+"
  print(f"Result: {num1} {operationString} {num2} = {result}") 
elif operation == "S":
  result = substract(num1, num2)
  operationString = "-"
  print(f"Result: {num1} {operationString} {num2} = {result}") 
elif operation == "M":
  result = multiply(num1, num2)
  operationString = "*"
  print(f"Result: {num1} {operationString} {num2} = {result}") 
elif operation == "D":
  result = divide(num1, num2)
  operationString = "/"
  print(f"Result: {num1} {operationString} {num2} = {result}") 
else:
  print("It\'s not a valid option!")

