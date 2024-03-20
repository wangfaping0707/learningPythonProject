def func(n, m):
	if n == 1:
		return m + 1
	elif m == 1:
		return n + 1
	else:
		return func(n - 1, m) + func(n, m - 1)


while True:
	try:
		n, m = map(int, input().strip().split())
		res = func(n, m)
		print(res)
	except:
		break
