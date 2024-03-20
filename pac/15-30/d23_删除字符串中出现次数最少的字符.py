s = input().strip()
d = {}
for k in s:
	d[k] = d.get(k, 0) + 1

min_v = min(list(d.values()))

for i in s:
	if d[i] == min_v:
		s = s.replace(i, '')
print(s)
