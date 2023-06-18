import re
x = 'From stephen.marqueard@uct.es.es Sat Jan 5 02:34:43 2020'

y = re.findall('\S+@\S+', x)
print(y)

d = re.findall('^From (\S+@\S+)', x)
print(y)

e = re.findall('@([^ ]*)', x)
print(e)

z = 'We just received $10.00 for cookies'
f = re.findall('\$[0-9.]+', z)
print(f)