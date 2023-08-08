# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')

score1 = t + r + u + e
score2 = l + o + v + e
scoreLove = int((f"{score1}{score2}"))
message = (f"Your score is {scoreLove}")

if(scoreLove < 10 or scoreLove > 90):
    message += (", you go together like coke and mentos.")
elif(scoreLove >= 40 and scoreLove <= 50):
    message += ", you are alright together."
else:
    message += "."

print(message)