while True:
	try:
		n = float(input().strip())

		if n > 0:
			print('{:.1f}'.format(n ** (1 / 3)))
		elif n < 0:
			n = abs(n)
			val = n ** (1 / 3)
			print(format(-val, '.1f'))
		else:
			print('0.0')
	except:
		break