s = 'aaddccdc'
s = sorted(s)
print(s)
d = {}

for i in s:
	d[i] = d.get(i, 0) + 1


d = sorted(d.items(), key=lambda item:item[1], reverse=True)
print(d)