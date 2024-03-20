while True:
	try:
		n = input().strip()
		node_list = input().strip().split()
		i = int(input().strip())
		print(node_list[-i])
	except:
		break
