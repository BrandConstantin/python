import json
data = '''[
    {"name": "Novrodoski",
    "x": "2",
    "id": "002"
    },
    {"name": "Olsvaldo",
    "x": "3",
    "id": "003"
    }
]'''

info = json.loads(data)
print('User counts:', len(info))
for item in info:
    print('Name', item["name"])
    print('Id', item["id"])
    print('Attibute', item["x"])