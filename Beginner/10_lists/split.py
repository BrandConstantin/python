abc = 'With three words'
stuff = abc.split()
print(stuff)
print('------')
for w in stuff:
    print(w)


print('------')
line = 'first;second;third'
thing = line.split()
print(line)
thing2 = line.split(';')
print(thing2)

print('------')
text = open('mbox.txt')
for line in text:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[2])