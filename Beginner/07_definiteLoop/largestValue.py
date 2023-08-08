largest = -1

print('Before ', largest)

for number in [54, 466, 39, 12, 1, 98]:
    if number > largest:
        largest = number
    print(largest, number)

print("After ", largest)