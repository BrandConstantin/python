fname = input("Enter file name: ")
if len(fname) < 1 : fname = "short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From:'):
        count += 1
        words = line.split()
        eliminateWords = words[1]
        print(eliminateWords)

print("There were", count, "lines in the file with From as the first word")


# print("Another way to do it!")
# for line in fh:
#     line = line.rstrip()
#     wds = line.split()
#     if len(wds) < 3 or wds[0] != 'From': continue
#     print(wds[2])