#Step 1 
import random

word_list = ["manzanar", "telefono", "camello", "guarderia", "planeta", "cordobesa", "alicate", "mamaracho", "tribunal", "notable", "casoplon", "girasol", "desgraciado", "handicap", "instagram", "mediano", "listado", "cuerda", "social", "jueces", "policia", "pelicula"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print("HANGMAN / SPANZURATOAREA")

#TODO-4 - Create an empty list called display, for each letter in the chosen_word, add a "_".
display = []
for position in range(len(chosen_word)):
  display += "_"
print(display)
  
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
lives = 6
while "_" in display and lives > 0:
  answer = input("Adivina una letra: ").lower()

  if len(answer) > 1 or len(answer) < 1:
    print("Debes elegir una sola letra")
  
  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  if answer in chosen_word:
    for position in range(len(chosen_word)):
      if answer in chosen_word[position]:
        if "_" in display[position]:
          display[position] = answer
        else:
          print("Ya has ecogido está letra")
  else:
      lives -= 1

  print(stages[lives])
  print(display)
    
if "_" not in display and lives > 1:
  print("Has ganado!")  
else: 
  print("Has perdido!")
  print(f"La palabra era: {chosen_word}")