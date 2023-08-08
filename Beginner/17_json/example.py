import json
data = '''{
    "name": "Constantin",
    "phone": {
        "type": "intl",
        "number": "664664664"
    },
    "email":{
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name', info["name"])
print('Hidee', info["email"]["hide"])