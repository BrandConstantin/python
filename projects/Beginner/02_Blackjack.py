############### Blackjack Project #####################
import random
from art import logo
from replit import clear

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def showCards(user_cards):
  print(f"Your cards: {user_cards}")
  print("Computer cards ** \n -------------------------")
def showCards2(user_cards, computer_cards):
  print(f"Your cards: {user_cards}")
  print(f"Computer cards: {computer_cards} \n -------------------------")
  
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and       return 0 instead of the actual score. 0 will represent a blackjack in our game.
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove       the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards:
    if sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  elif sum(cards) == 21:
    return 21
  else:
    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
winner = ""
def gameOver(userScore, computerScore):
  if userScore == 21:
    print(f"Blakjack for user! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!") 
  elif computerScore == 21:
    print(f"Blakjack for computer! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!")
  elif userScore == computerScore:
    print(f"User: {userScore} | Computer: {computerScore}")
    print("No one win! It\'s a draw'")   
  elif (userScore == 21) and (computerScore == 21) and (userScore == computerScore): 
    print(f"User: {userScore} | Computer: {computerScore}")
    print("Blakjack bouth! It\'s a draw! \nGame over!") 
  elif computerScore > 21 and userScore > 21:
    print("Lose both!")
  elif userScore > 21:
    winner = "Computer"
    print(f"{winner} win! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!")
  elif computerScore > 21:
    winner = "User"
    print(f"{winner} win! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!")
  elif computerScore > userScore:
    winner = "Computer"
    print(f"{winner} win! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!")
  elif userScore > computerScore:
    winner = "User"
    print(f"{winner} win! \nUser: {userScore} | Computer: {computerScore}")
    print("Game over!")
  else:
    print("Something go rong with the game")
    
######################
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
restart = True
while restart:  
  clear()
  print(logo)
  
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  showCards(user_cards)
  
  ######################
        
  #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  userScore = calculate_score(user_cards)
  computerScore = calculate_score(computer_cards)
  
  ######################


  #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  answer = input("You wanna draw another card? 'y|'n ").lower()
  if answer == 'y':
    user_cards.append(deal_card())
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep       drawing cards as long as it has a score less than 17.
  if computerScore < 17:
    computer_cards.append(deal_card())
  
  ######################
  
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  userScore = calculate_score(user_cards)
  computerScore = calculate_score(computer_cards)
  showCards2(user_cards, computer_cards)
  gameOver(userScore, computerScore)

  print("-------------------------")
  restart_answer = input("You wanna restart the game? 'y|'n ").lower()
  if restart_answer == 'n':
    restart = False