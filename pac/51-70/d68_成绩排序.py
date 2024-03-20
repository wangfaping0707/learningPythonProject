while True:
	try:
		# 排序人数
		n = int(input().strip())
		# 排序方式:0代表从高到低，1代表从低到高
		order = int(input().strip())
		# 存储个人信息列表
		info_list = []
		for i in range(n):
			name, score = input().strip().split()
			info_list.append((name, int(score)))

		# 对列表进行排序
		if order == 1:
			for j in sorted(info_list, key=lambda x: x[1]):
				print(j[0], j[1])
		else:
			for j in sorted(info_list, key=lambda x: x[1], reverse=True):
				print(j[0], j[1])

	except:
		break


# n = int(input().strip())
# order_by = int(input().strip())
# res = []
# for i in range(n):
# 	s1, s2 = input().strip().split()
# 	res.append((s1, int(s2)))
#
# print(res)
#
# if order_by == 1:
# 	res = sorted(res, key=lambda item: item[1])
# 	for k, v in res:
# 		print(f'{k} {v}')
# else:
# 	res = sorted(res, key=lambda item: item[1], reverse=True)
# 	for k, v in res:
# 		print(f'{k} {v}')
#
























