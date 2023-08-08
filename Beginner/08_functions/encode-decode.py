from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by   the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def directionToGo(direction): 
  if direction in "":
    print("You type nothing")
  elif (direction == "encode") or (direction == "decode"):
    should_continue = True
    while should_continue:
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      shift = shift % 26 ## if the user insert a number major like 26
      caesar(direction = direction, plain_text = text, shift_amount = shift)      

      result = input("Type 'Yes' if you want to go again. Otherwise type 'no'. ").lower()
      if result == 'no':
        should_continue = False
        print("Goodbye!")
        
  else: 
    print("Rong answer!")

def caesar(direction, plain_text, shift_amount):
  cipher_text = ""
  new_position = -1
  
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      
      if direction == "encode" or  direction == "decode":
        new_position = encryptDecrypt(direction, position, shift_amount)
      else:
        print("Something go rong!")    
  
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    else:
      cipher_text += letter


  print(f"The {direction} test is {cipher_text}")
  

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encryptDecrypt(direction, position, shift_amount):
  if direction == "encode":
    if position == 25: #last letter
      new_position = 0 + (shift_amount - 1)
    else: 
      new_position = position + shift_amount
  elif direction == "decode":
    if position == 25: #last letter
      new_position = 25 - shift_amount
    else: 
      new_position = position - shift_amount
  else:
    new_position = position - shift_amount
    
  return new_position

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
directionToGo(direction = direction)