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
answer = int(input("Your turn! 0 for Rock | 1 for Paper | 2 for Scissors "))
game_images = [rock, paper, scissors]

print("My choice:")
print(game_images[answer])

pc_answer = random.randint(0, 2);
print("Computer choice:")
print(game_images[pc_answer])

if answer >= 3 or answer < 0:
    print("You typed an invalid number!")
else:
    if answer == 0 and pc_answer == 2:
        print("I\'m win!")
    elif pc_answer == 0 and answer == 2:
        print("Computer win!")
    elif answer > pc_answer:
        print("I\'m win!")
    elif pc_answer > answer:
        print("Computer win!")
    else:
        print("No one win")