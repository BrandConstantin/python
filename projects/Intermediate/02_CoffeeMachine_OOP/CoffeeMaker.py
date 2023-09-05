from MenuItem import resources, menu

def report():
    resourcesDict = []
    for resource in resources:
        resourcesDict.append(resources[resource])

    return resourcesDict

def is_resource_sufficient(drink):
    for _ in drink['ingredients']:
        if (drink['ingredients']['coffee'] > resources['coffee'] or drink['ingredients']['milk'] > resources['milk'] or
                drink['ingredients']['water'] > resources['water']):
            return False
    return True


def messageResources(resource):
    message = ""

    if resource[0] < 50:
        message += " water"
    if resource[1] < 100:
        message += " milk"
    if resource[2] < 18:
        message += " coffee"

    return message

def make_coffee(order, coffeType):
    print("Prepare the coffee...")
    # rest water
    resources['water'] -= order['ingredients']['water']
    print("####")
    print("Turn water")
    # rest milk
    if coffeType != 'espresso':
        resources['milk'] -= order['ingredients']['milk']
    print("########")
    print("Turn milk")
    # rest coffee
    resources['coffee'] -= order['ingredients']['coffee']
    print("############")
    print("Turn coffee")
    # add money
    resources['money'] += order['cost']
    print("################")
    print(f"Here is your {coffeType}. Enjoy!")
    print("####################")
    existCoffeInDict = False