"""
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""
while True:
	try:
		num = int(input().strip())
		res = []
		for i in range(num):
			if i == 0:
				res = [(j + 2) * (j + 1) // 2 for j in range(num)]
			else:
				res = [x - 1 for x in res[1:]]
			print(' '.join(map(str, res)))
	except:
		break
