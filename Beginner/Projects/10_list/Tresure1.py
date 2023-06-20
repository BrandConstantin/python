# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
mapPosition = list(position)
mapPosition[0] = int(mapPosition[0]) - 1
mapPosition[1] = int(mapPosition[1]) - 1
ex = 'X'

if int(mapPosition[0]) == 0: ## COLUMN 1
    if int(mapPosition[1]) == 0:
        row1 = [ex,'⬜️','⬜️']
    elif int(mapPosition[1]) == 1:
        row2 = [ex,'⬜️','⬜️']
    elif int(mapPosition[1]) == 2:
        row3 = [ex,'⬜️','⬜️']
    else:
        print("Incorrect value!")  
elif int(mapPosition[0]) == 1:  ## COLUMN 2
    if int(mapPosition[1]) == 0:
        row1 = ['⬜️',ex,'⬜️']
    elif int(mapPosition[1]) == 1:
        row2 = ['⬜️',ex,'⬜️']
    elif int(mapPosition[1]) == 2:
        row3 = ['⬜️',ex,'⬜️']
    else:
        print("Incorrect value!")  
elif int(mapPosition[0]) == 2:  ## COLUMN 3
    if int(mapPosition[1]) == 0:
        row1 = ['⬜️','⬜️',ex]
    elif int(mapPosition[1]) == 1:
        row2 = ['⬜️','⬜️',ex]
    elif int(mapPosition[1]) == 2:
        row3 = ['⬜️','⬜️',ex]
    else:
        print("Incorrect value!")  
else:
    print("Incorrect value!")

map = [row1, row2, row3]
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

