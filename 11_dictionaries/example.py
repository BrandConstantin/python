purse = dict()
purse['money'] = 12
purse['candy'] = 5
purse['tissues'] = 21

print(purse)
print(purse['candy'])
print(purse.get('candy'), -1)

purse['candy'] = purse['candy'] + 5

print(purse)