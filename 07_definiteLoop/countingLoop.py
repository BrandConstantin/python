counting = 0

print('Before ', counting)

for number in [54, 'Hello', 39, False, 1, 'Good for me']:
    counting = counting + 1
    print(counting, number)

print("After ", counting)