largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done": 
        break

    try:   
        num = int(num)
        if smallest is None or smallest > num:
            smallest = num

        if largest is None or largest < num:
            largest = num
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)