import re
fname = input('Enter the file name: ')
if len(fname) < 1 : fname = "regex_sum_893855.txt"

fh = open(fname)
numberList = list()
for line in fh:
	line = line.rstrip()
	number = re.findall('([0-9]+)', line)
	if len(number) < 1: continue #kept getting empty lists, this solved that

	for i in number: 
		numberList.append(int(i))
#print(numberList)
print(sum(numberList))


#print(sum([int(i) for i in re.findall('([0-9]+)', open('regex_sum_893855.txt').read())]))