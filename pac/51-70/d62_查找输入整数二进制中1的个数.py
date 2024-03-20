while True:
	try:
		num = int(input().strip())
		count = bin(num).count('1')
		print(count)
	except:
		break


