data = 'From stephen.marquerd@uct.ac.za Sat Jan 5 09:14:24 2020'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1 : sppos]
print(host)