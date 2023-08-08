#Number Guessing Game Objectives:
from replit import clear
from logoGuessingGame import logo
import random

# Include an ASCII art logo.
print(logo)
number = -1
play = True
answer = ""

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in       hard mode).
dificulty = input("What dificult do you wanna, hight or eassy? 'h' or 'e' ").lower()

# Allow the player to submit a guess for a number between 1 and 100.
def getRandomNumber():
  number = random.randint(1, 100)
  return number


def getAnswer():
    answer = int(input("Guess the number between 1 and 100: "))

    return answer
  

def getLevels(dificulty):
  if dificulty == 'h':
    level = 4
  else:
    level = 9
  return level



number = getRandomNumber()
levelSet = getLevels(dificulty)

while play:  
  answer = getAnswer()
  
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the     user's answer. 
  if answer > 1 and answer < 100:
    if answer > number:
      print("Your number it\'s to hight")
    elif answer < number:
      print("Your number it\'s to small")
    else:
      print(f"You win! This is the correct number: [{number}]!")
      play = False
  else:
    print("The number is not less that 1 or bigest that 100.")


# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
  if levelSet < 1:
    print("-------------------------")
    print(f"No more oportunity. The aswer was {number}")
    play = False
    
  levelSet -= 1    
      
  if play == False:
    answerPlayAgain = input("Do you wanna play again? 'y' or 'n' ").lower()
  
    if answerPlayAgain == 'y':
      play = True
      number = getRandomNumber()
      clear()
      print(logo)
      dificulty = input("What dificult do you wanna, hight or eassy? 'h' or 'e' ").lower()
      levelSet = getLevels(dificulty)
  
