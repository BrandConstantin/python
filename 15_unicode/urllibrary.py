import urllib.request, urllib.parse, urllib.error

fhan = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhan:
    print(line.decode().strip())