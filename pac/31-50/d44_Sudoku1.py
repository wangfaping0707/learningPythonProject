m = []  # 二维数组用来存储
for _ in range(9):
	m.append(list(map(int, input().split())))


def get_maybe_value(x, y):  # 获取当前位置允许的值
	all_n = {1, 2, 3, 4, 5, 6, 7, 8, 9}
	row = [m[x][j] for j in range(9)]  # 获取当前所在行的所有元素
	col = [m[i][y] for i in range(9)]  # 获取当前所在列的所有元素
	box = [m[i][j] for i in range((x // 3) * 3, (x // 3) * 3 + 3) for j in
	       range((y // 3) * 3, (y // 3) * 3 + 3)]  # 获取当前所在宫的所有元素
	value = list(all_n - set(row) - set(col) - set(box))  # 取差集获取当前位置允许填入的所有值
	return value


def solo():
	x, y = -1, -1
	for i in range(9):
		for j in range(9):
			if m[i][j] == 0 and x == -1:  # 寻找第一个未填入值的位置
				x, y = i, j
				break
	if x == -1:  # 如果找不到还空着的位置，代表数独已经被填完了
		return True
	for v in get_maybe_value(x, y):  # 遍历该位置允许填入的值，如果前面某个位置填入的值是错误的，这里会返回一个空列表，代表没有可以填的值，循环结束后返回False
		m[x][y] = v  # 填入该值
		if not solo():  # 递归进去开始填下一个空着的位置
			m[x][y] = 0  # 如果返回False，代表当前位置填入的值是错误的，会与后面填入的值产生冲突
		else:
			return True  # 当数独填完整了，才会走到这里返回True
	return False


solo()
for i in range(9):
	print(' '.join([str(x) for x in m[i]]))


