name = input("Enter file:")
if len(name) < 1 : name = "short.txt"

handle = open(name)
lst=list()
counts=dict()

for line in handle :
    if line.startswith("From "):
        line = line.strip().split()
        hours = line[5]        
        hours = hours[:2]
        # print(hours)
        lst.append(hours)
        
for hour in lst :
    counts[hour] = counts.get(hour, 0) + 1
    # print(hour, counts[hour])
    
for k,v in sorted(counts.items()) :
    print(k, v)