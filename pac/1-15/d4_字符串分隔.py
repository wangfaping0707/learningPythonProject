while True:
	try:
		str = input()
		while len(str) > 0:
			print(str[:8].ljust(8, '0'))
			str = str[8:]
	except Exception:
		break

