print(len('banana') * 7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0.8475')
#print(pos)
sli = text[23:29]
print(float(sli))


text2 = "X-DSPAM-Confidence:    0.8475"
ipos = text2.find(':')
print("Position ", ipos)
piece = text2[ipos + 2: ]
print(piece)
value = float(piece)
print(value)