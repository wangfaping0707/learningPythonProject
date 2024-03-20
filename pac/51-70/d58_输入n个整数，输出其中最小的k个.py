while True:
	try:
		n, k = map(int, input().strip().split())
		num_list = list(map(int, input().strip().split()))
		# 最小的k个整数
		k = n_list[1]
		num_list.sort()
		res = list(map(str,num_list[:k] ))
		print(' '.join(res))
	except:
		break
