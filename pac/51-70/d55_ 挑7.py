n = int(input().strip())
res = []
for i in range(1, n + 1):
	if i % 7 == 0 or '7' in str(i):
		res.append(i)
print(res)

