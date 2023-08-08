#Calculator
def theFunction(operation, num1, num2):
  if(operation == '+'):
    return num1 + num2
  elif operation == '-':
    return num1 - num2
  elif operation == '*':
    return num1 * num2
  elif operation == '/':
    return num1 / num2
  else:
    return 0

## Operations
result = 0
answer = True

while answer:
  num1 = int(input("What is the first number that you wanna use? "))
  num2 = int(input("What is the second number that you wanna use? "))
  operation = input("What operation you wanna do? ('+' | '-' | '*' | '/') ")
  
  if (operation == '+' or operation == '-' or operation == '*' or operation == '/') :
    result = theFunction(operation, num1, num2)
    print(f"Result: {num1} {operation} {num2} = {result}")       

    question = input("Do you wanna continue? 'y'|'n' ").lower()
    if question != 'y':
      answer = False
  else:
    answer = False
    print("It\'s not a valid option!")