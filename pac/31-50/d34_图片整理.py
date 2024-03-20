"""
输入：

输出：0112Iaadeeefghhinnnorsssv
"""
# nums = input().strip()

while True:
	try:
		data = input().strip()
		num_arr = []
		str_arr = []
		for i in data:
			if i.isdigit():
				num_arr.append(int(i))
			elif i.isalpha():
				str_arr.append(i)

		num_arr = list(map(str, sorted(num_arr)))
		str_arr = list(sorted(str_arr, key=lambda x: ord(x)))

		print(''.join(num_arr + str_arr))
	except:
		break

print('===============================================================')

while True:
	try:
		a = input()
		a = list(a)  # 将字符串放入列表中，每个字符为一项
		for i in range(len(a)):
			a[i] = ord(a[i])  # 先转化为ASCLL码
		a.sort()  # 按照ASCLL排序
		for i in range(len(a)):
			a[i] = chr(a[i])  # 再将每个ASCLL还原为字符
		print(''.join(a))  # 按要求输出
	except:
		break
