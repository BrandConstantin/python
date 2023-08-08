c = {'a': 10, 'c': 4, 'b':55}
temp = list()

for k, v in c.items():
    temp.append((v, k))

print(temp)

tmp = sorted(temp, reverse=True)
print(temp)