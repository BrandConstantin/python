name = input("Enter file:")
if len(name) < 1 : name = "short.txt"

handle = open(name)
dictionary = dict()
emails = dict()

for line in handle:
    if line.startswith('From:'):
        line = line.rstrip()
        words = line.split()
        emails = words[1]
        dictionary[emails] = dictionary.get(emails, 0) + 1          
        #print(emails, dictionary[emails])

# print(dictionary)
largest = -1
theWord = None
for key, value in dictionary.items():
    #print(key, value)
    if value > largest:
        largest = value
        theWord = key

print(theWord, largest)