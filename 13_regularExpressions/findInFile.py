import re
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

numlist = list()

for line in fhand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
       
print("Maximum:", max(numlist))