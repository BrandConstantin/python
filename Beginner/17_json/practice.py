import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retrieving', address)

data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')

try:
    json_object = json.loads(data)
except:
    json_object = None

# print(json.dumps(js, indent=4))

total = 0
suming = 0
for count in json_object['comments']:
    suming += int(count['count'])
    total += 1
print('Count:', total)
print('Sum', suming)