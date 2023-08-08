hrs = input("Enter Hours:")

try:
    h = float(hrs)
    rate = float(input("Enter Rate:"))
except Exception as e:
    print("Error, please enter numeric númber")
    quit()

def computepay(hrs, rate):
    if (h > 40 and rate > 0):
        return (40 * rate + ((h - 40) * rate * 1.5))
    elif ((h > 0 or h <= 40) and rate > 0):
        return h * rate

p = computepay(hrs, rate)


if (h <= 0 or rate <= 0):
    grossPay = 0
    print("Zero is not a good result!")
else:
    print("Pay",p)