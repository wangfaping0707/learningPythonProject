def f1(n):
	if n == 10:
		return
	print(n)
	n += 1
	f1(n)


f1(0)
