import xml.etree.ElementTree as ET 
data = '''<persons>
        <users>
            <user x="1">
                <id>001</id>
                <name>Olga</name>
                <phone type="intl">
                    664 664 664
                </phone>
            </user>
            <user x="4">
                <id>004</id>
                <name>Johny</name>
                <phone type="intl">
                    665 665 665
                </phone>
            </user>
        </users>
    </persons>'''

persons = ET.fromstring(data)
lst = persons.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))