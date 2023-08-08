smallest = None

print('Before ', smallest)

for number in [54, 466, 39, 12, 1, 98]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest, number)

print("After ", smallest)