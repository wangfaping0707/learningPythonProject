L = [0, 3, 4, 6, 10, 11, 13, 23, 33, 34, 45, 56, 65, 77, 99]


# 定义二分法函数

def binary_search(find_num, L):
	print('变化前的列表：', L)
	if len(L) == 0:
		print('您查找的值不存在，请核对之后在输入。')
		return

	# 查找列表的中位数索引
	# 除法只能使用取整法
	mid_index = len(L) // 2
	print(L[mid_index])
	if find_num > L[mid_index]:
		L = L[mid_index + 1:]
		binary_search(find_num, L)
	elif find_num < L[mid_index]:
		L = L[:mid_index]
		binary_search(find_num, L)
	else:
		print('find it 。。。')


binary_search(99, L)
