fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:    
    words = line.split()
    #print(words)
    for word in words:
        lst.append(word)
lst.sort()

otherlst = list()
for word in lst:
    if word not in otherlst:
        otherlst.append(word)
print(otherlst)