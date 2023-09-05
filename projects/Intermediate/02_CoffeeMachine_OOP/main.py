import MenuItem, Menu, CoffeeMaker, MoneyMachine
from replit import clear

items = Menu.getItems()
resources = MenuItem.resources
menu = MenuItem.menu

nextUser = True
initialResource = []
isOfTheMachine = True


def OnOfMachine(value):
    if value:
        message = "Turn ON the machine\nIf you wanna turn off please rewrite the secret word. "
    else:
        message = "Turn OFF the machine\nIf you wanna turn on please write the secret word. "

    return print(message)


while nextUser:
    prepareCoffee = False
    existCoffeInDict = False
    coffeeType = input(f'What would you like: {items} ? ').lower()

    if len(initialResource) == 0:
        initialResource = CoffeeMaker.report()

    if coffeeType == "report":
        if len(initialResource) == 0:
            print(f"Report => {initialResource}")
        else:
            print(f"Report => {resources}")

    elif coffeeType == 'report money':
        print(f"Report => {MoneyMachine.reportMoney()}")

    elif coffeeType == 'maintenance':
        OnOfMachine(False)
        isOfTheMachine = False
        onoff = input("Do you know the word? ")

        while onoff != 'on':
            OnOfMachine(True)
            isOfTheMachine = True
            clear()
            print("This is not the correct word to turn on the machine. \nIf you wanna turn off please rewrite the secret word. ")
            onoff = input("Do you know the word? ")

            if onoff == 'on':
                isOfTheMachine = False
                OnOfMachine(False)

    elif isOfTheMachine and (coffeeType != 'maintenance' and coffeeType != 'report') and Menu.find_drink(coffeeType):
        existCoffeInDict = True
    else:
        print("Something was typed badly!")

    if existCoffeInDict:
        coffeeDrink = Menu.getdrink(coffeeType)
        isSufficientResources = CoffeeMaker.is_resource_sufficient(coffeeDrink)
        messageResource = CoffeeMaker.messageResources(initialResource)

        if not isSufficientResources:
            print(f"Sorry is no enough resources: {messageResource} ")
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
                    if totalMoney < coffeeDrink['cost']:
                        print(f"You inserted {round(totalMoney, 2)}€ but the price of coffee is {coffeeDrink['cost']}")
                        print(f"Sorry that's not enough money. Money refunded.")
                        insertMoreMoney = False
                    else:
                        prepareCoffee = True
                        insertMoreMoney = False
                        change = round(totalMoney - coffeeDrink['cost'], 2)
                        print(f"Here is your euro change {change} ...")

        if prepareCoffee:
            CoffeeMaker.make_coffee(coffeeDrink, coffeeType)