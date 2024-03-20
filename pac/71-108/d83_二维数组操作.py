while True:
	try:
		# 初始化m行n列的表格:数据表的最大规格为9行*9列
		m, n = map(int, input().strip().split())
		# 进行数据交换的坐标
		x1, y1, x2, y2 = map(int, input().strip().split())
		# 输入要插入的行的数值,即在x行上面在插入一行
		x = int(input().strip())
		# 输入要插入的列的数值,即在y列上面在插入一行
		y = int(input().strip())
		# 输入要查询的单元格的坐标
		x3, y3 = map(int, input().strip().split())
		if m <= 9 and n <= 9:
			print('0')
		else:
			print('-1')

		if x1 < m and x2 < m and y1 < n and y2 < n:
			print('0')
		else:
			print('-1')

		if x < m < 9:
			print('0')
		else:
			print('-1')

		if y < n < 9:
			print('0')
		else:
			print('-1')

		if x3 < m and y3 < n:
			print('0')
		else:
			print('-1')

	except:
		break
