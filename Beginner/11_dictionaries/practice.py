name = input("Enter file:")
if len(name) < 1 : name = "short.txt"

handle = open(name)
emails = dict()
counts = dict()

for line in handle:
    if line.startswith('From:'):
        words = line.split()
        emails = words[1]
        counts[emails] = counts.get(emails, 0) + 1
        # print(emails)    

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)