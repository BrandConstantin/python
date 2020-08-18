counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)