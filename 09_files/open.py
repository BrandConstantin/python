fhand = open('mbox.txt', 'r')
print(fhand)

print('---------------')

xfile = open('mbox.html')
for x in xfile:
    print(x)

print('---------------')

yfile = open('mbox.txt')
count = 0
for line in yfile:
    count += 1
print('Line count:', count)

print('---------------')

zfile = open('mbox.txt')
inp = zfile.read()
print(len(inp))
print(inp[:20])

print('---------------')

wfile = open('mbox.txt')
for line in wfile:
    if line.startswith('Hola'):
        print(line)