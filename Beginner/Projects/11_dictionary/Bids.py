from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

anyOneToBid = True
bid_info = {}

while anyOneToBid:
  name = input("What\'s your name? ").upper()
  price = int(input("What\'s the bid price? "))
  bidagain = input("It\'s anyone here to one to bid? ").lower()

  if bidagain == 'yes' or bidagain == 'no':
    if bidagain == 'no':
      anyOneToBid = False
      bid_info[name] = price
    else:
      bid_info[name] = price
      clear()
  else:
    anyOneToBid = False
    print("It\'s not a correct answer!")

# find the highest bid     
print("All the players: \n", bid_info, "\n")

def getHigestBid(bid_info):
  highest_bid = 0
  winner = ""
  
  for bid in bid_info:    
    bid_price = bid_info[bid]
  
    if bid_price > highest_bid:
      highest_bid = bid_price
      winner = bid
      
  return print(f"The Winner is {winner} with a bid of {highest_bid}")

getHigestBid(bid_info)