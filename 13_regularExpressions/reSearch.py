import re

hand = open('short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

print('--------------')

hand = open('short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)