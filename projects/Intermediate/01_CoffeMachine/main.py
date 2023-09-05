from replit import clear
from menu import resources
from menu import MENU

serveNextUser = True
coffeTypeDict = {'espresso', 'latte', 'cappuccino'}
coffeType = ''
isTurnOfTheMachine = True
existCoffeInDict = False
global resource


def askTypeCoffe():
    return input('What would you like? (espresso/latte/cappuccino): ').lower()


# off to turn of the machine and on to turn on
def turnOnOfMachine(value):
    if value:
        message = "Turn ON the machine\nIf you wanna turn off please rewrite the secret word. "
    else:
        message = "Turn OFF the machine\nIf you wanna turn on please write the secret word: "

    return print(message)


def checkResources(resource):
    message = ""

    if resource[0] < 50:
        message += " water"
    if resource[1] < 100:
        message += " milk"
    if resource[2] < 18:
        message += " coffee"

    return message


def coffeTypeExist(typeOfCoffe):
    found = False
    for typeElement in coffeTypeDict:
        if typeOfCoffe.lower() == typeElement.lower():
            found = True

    return found


def getResources(resources):
    resourcesDict = []

    for _ in resources:
        resourcesDict.append(resources[_])

    return resourcesDict

def getMenu(MENU, coffeType):
    for element in MENU:
        if coffeType == element:
            return MENU[element]

    return 0

resource = []
while serveNextUser:
    coffeType = askTypeCoffe()

    if len(resource) == 0:
        resource = getResources(resources)

    if coffeType == "report":
        print(resource)

    elif coffeType == 'maintenance':
        turnOnOfMachine(False)
        onoff = input()

        if onoff == 'on':
            turnOnOfMachine(True)
            isTurnOfTheMachine = True
            clear()
        else:
            turnOnOfMachine(False)

    elif isTurnOfTheMachine and coffeType != 'maintenance' and coffeType != 'report':
        if not coffeTypeExist(coffeType):
            print("Error: this coffe not exist!\nTry again!")
        else:
            existCoffeInDict = True
    else:
        print("Something was typed badly!")

    if existCoffeInDict:
        coffee = getMenu(MENU, coffeType)
        message = checkResources(resource)

        if message != "":
            print(f"Sorry is no enough resources: {message} ")
            serveNextUser = False
            print("Will shut down the machine. Bye!")
        else:
            print("Please insert coins!")

            insertMoreMoney = True
            totalMoney = 0
            prepareCoffee = False
            while insertMoreMoney:
                moneyType = input("Select type of money and insert coins:\n* euro\n* 50c\n* 10c ").lower()

                if moneyType == 'euro':
                    # cantidad de monedas
                    coins = float(input("How much coins? "))
                    # multiplicado por moneda
                    totalMoney += (coins * 1)
                elif moneyType == '50c':
                    coins = float(input("How much coins? "))
                    totalMoney += (coins * 0.5)
                elif moneyType == '10c':
                    coins = float(input("How much coins? "))
                    totalMoney += (coins * 0.1)
                else:
                    print("Incorrect money type")

                print(f"Total coins: {round(totalMoney, 2)}€")
                yesOrNot = input("Do you wanna insert more coins? 'y' or 'n' ")

                if yesOrNot == 'n':
                    if totalMoney < coffee['cost']:
                        print(f"You inserted {round(totalMoney, 2)}€ but the price of coffee is {coffee['cost']}")
                        print(f"Sorry that's not enough money. Money refunded.")
                        insertMoreMoney = False
                    else:
                        prepareCoffee = True
                        insertMoreMoney = False
                        change = round(totalMoney - coffee['cost'], 2)
                        print(f"Here is your change {change} ...")

            if prepareCoffee:
                print("Prepare the coffee...")
                # rest water
                resource[0] -= coffee['ingredients']['water']
                print("####")
                print("Turn water")
                # rest milk
                if coffeType != 'espresso':
                    resource[1] -= coffee['ingredients']['milk']
                print("########")
                print("Turn milk")
                # rest coffee
                resource[2] -= coffee['ingredients']['coffee']
                print("############")
                print("Turn coffee")
                # add money
                resource[3] += coffee['cost']
                print("################")
                print(f"Here is your {coffeType}. Enjoy!")
                print("####################")
                existCoffeInDict = False