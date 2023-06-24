#Write your code below this row 👇
numbArray = list(range(2, 102))
newNumbArray = list()

for n in numbArray:
    if n % 2 == 0:
        newNumbArray.append(n)

print(sum(newNumbArray))