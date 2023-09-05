from MenuItem import menu

def getItems():
    namesStr = ""

    for coffee in menu:
        if coffee == "cappuccino":
            removeColon = namesStr[:-2]
            namesStr = removeColon + " or " + coffee
        else:
            namesStr += coffee + ", "

    return namesStr

def find_drink(order_name):
    for drink in menu:
        if order_name.lower() == drink.lower():
            return drink

    return None


def getdrink(order_name):
    for _ in menu:
        if menu[order_name]:
            return menu[order_name]

    return None