# I = [15, 123, 456, 786, 453, 46, 7, 5, 3, 665, 453456, 745, 456, 786, 453, 123]
# R = [5, 6, 3, 6, 3, 0]
"""
输出格式如下:
30    3 6 ====== 0 123 3 453 7 3 9 453456 13 453 14 123 ===== 6 7 ===1 456 2 786 4 46 8 665 9 453456 11 456 12 786

内存循环，每次循环结束后，temp存储的值如下：

temp1 = [0 123 3 453 7 3 9 453456 13 453 14 123]
3出现的次数 = len(temp1)//2

temp2 = [1 456 2 786 4 46 8 665 9 453456 11 456 12 786]
6出现的次数 = len(temp2)//2

3 6 这两个元素出现的次数就是temp数组的一半 因为temp列表存储的是 enumerate(I)返回的 索引和对应的值
"""

while True:
	try:
		I = input().split()[1:]
		R = sorted(map(int, set(input().strip().split()[1:])))
		R = list(map(str, R))
		# print(f'I的值:{I}')
		# print(f'R的值:{R}')

		res = []
		for r in R:
			# print(f'r:{r}')
			temp = []
			for i, sub in enumerate(I):
				if r in sub:
					temp.extend([str(i), sub])
			if temp:
				res.extend([r, str(len(temp) // 2)] + temp)
		# print(f'res的值：{res}')
		print(str(len(res)) + ' ' + ' '.join(res))
	except:
		break
