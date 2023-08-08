counting = 0
sum = 0

print('Before ', counting, sum)

for value in [9, 41, 12, 3, 74, 15]:
    counting = counting + 1
    sum = sum + value
    print(counting, sum, value)

print("After ", counting, sum, int(sum / counting))