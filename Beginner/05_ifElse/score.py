score = input("Enter Score: ")

try:
    s = float(score)
except Exception as e:
    print("Error, please enter numeric númber")
    quit()

if(s < 0.0 or s > 1.0):
    print("Error, the score is out of range")
else:
    if(s >= 0.9):
        print("A")
    elif(s >= 0.8):
        print("B")
    elif(s >= 0.7):
        print("C")
    elif(s >= 0.6):
        print("D")
    else:
        print("F")
