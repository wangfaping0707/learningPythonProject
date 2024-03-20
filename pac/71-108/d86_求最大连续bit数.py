while True:
	try:
		num = int(input().strip())

		bin_num_list = bin(num)[2:].replace('0', ' ').split()

		res = []
		for i in bin_num_list:
			res.append(len(i))

		print(max(res))
	except:
		break
