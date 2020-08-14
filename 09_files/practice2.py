fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        value = line[20:]
        value = value.strip()
        value = float(value)
        count = float(count) + 1
        total += value
       
print("Average spam confidence:", total / count)
    