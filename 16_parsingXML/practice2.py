import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
parms = urllib.request.urlopen(address, context=ctx).read()
tree = ET.fromstring(parms)
results = tree.findall('comments/comment')
counts = tree.findall('.//count')

print('Retrived:', len(parms), 'characters')

suming = 0
for count in counts:
    suming += int(count.text)
print('Count:', len(results))
print('Sum', suming)


# for item in results:
#     # print(parms.decode())
#     name = item.find('name').text
#     counting = item.find('count').text

#     print('name', name, 'count', counting)
# print('Count:', len(results))