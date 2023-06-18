fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

for line in fhand:
    print(line.strip().upper())