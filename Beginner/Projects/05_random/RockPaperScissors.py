# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Rock, paper, scissors")
answer = input("Your turn! R | P | S ").upper()
pcAnswer = ''
myAnswer = ''

pc = random.randint(1, 3);

if pc == 1:
  pcAnswer = rock    
elif pc == 2:
  pcAnswer = paper
else:
  pcAnswer = scissors

if answer == 'R':
  myAnswer = rock
elif answer == 'P':
  myAnswer == paper
elif answer == 'S':
  myAnswer == scissors
else:
  print("Wrong answer!")

printing = f"{myAnswer} \n {pcAnswer}"
print(printing)
print("-----------------")

if myAnswer == scissors and pcAnswer == paper:
  print("I\'m win!'")
elif myAnswer == paper and pcAnswer == rock:
  print("I\'m win!'")
elif myAnswer == rock and pcAnswer == scissors:
  print("I\'m win!'")
elif pcAnswer == scissors and myAnswer == paper:
  print("Pc win!'")
elif pcAnswer == paper and myAnswer == rock:
  print("Pc win!'")
elif pcAnswer == rock and myAnswer == scissors:
  print("Pc win!'")
else:
  print("No one win!")