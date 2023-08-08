import xml.etree.ElementTree as ET 
data = '''<person>
    <name>Constantin</name>
    <phone type="intl">
        664 664 664
    </phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Mobile:', tree.find('phone').text.strip())
print('Attr:', tree.find('email').get('hide'))