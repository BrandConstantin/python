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
symbols = {"+": add, "-": substract, "*": multiply, "/": divide}

operation = input("What operation you wanna do? ('+' | '-' | '*' | '/') ")

if (operation == '+' or operation == '-' or operation == '*' or operation == '/') :
  for symbol in symbols:
    if operation == symbol:
      theFunction = symbols[operation]
      result = theFunction(num1, num2)
      print(f"Result: {num1} {symbol} {num2} = {result}")       
else:
  print("It\'s not a valid option!")