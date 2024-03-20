while True:
	try:
		data = input().strip()
		length = int(input().strip())
		print(data[:length])
	except:
		break
