while True:
	try:
		# A,B两组服务器数量
		a_num, b_num = map(int, input().strip().split())
		# A组服务器计算能力
		a_lst = list(map(int, input().strip().split()))
		# B组服务器计算能力
		b_lst = list(map(int, input().strip().split()))

		# 能力差值
		for i in a_lst:
			for j in b_lst:
				if i + j == (sum(a_lst) + sum(b_lst)) / 2:
					b_lst.remove(j)
					print(i, ''.join(map(str, b_lst)))
					break
	except:
		break
