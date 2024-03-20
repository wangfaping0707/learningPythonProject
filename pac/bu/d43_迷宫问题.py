"""
[[0, 1, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 1, 0]]
"""
def dfs(matrix, x, y, path, dst):
	if (x, y) == dst:
		path.append((x, y))
		for i in path:  # i是一个记录目标位置点的 元组
			print("({},{})".format(i[0], i[1]))
		return
	# 如果当前坐标位置超出了二位数组 或者 当前位置碰到了 1 ，即matrix=1, 或者当前的位置之前已经走过了，停止行走，返回
	if not 0 <= x < len(matrix) or not 0 <= y < len(matrix[0]) \
			or matrix[x][y] == 1 or (x, y) in path:
		return

	path.append((x, y))
	dfs(matrix, x + 1, y, path, dst)
	dfs(matrix, x, y + 1, path, dst)
	dfs(matrix, x - 1, y, path, dst)
	dfs(matrix, x, y - 1, path, dst)
	path.pop()

"""
(0,0)          
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

[[0, 1, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 1, 0]]
"""
while True:
	try:
		x, y = list(map(int, input().split()))
		# 目的地出口 也就是终点
		dst = (x - 1, y - 1)
		# 生成迷宫二维列表
		matrix = []
		for i in range(x):
			matrix.append(list(map(int, input().split())))
		# 起始位置：x=0 y=0  表示起点(0,0) [] 记录走过的路径 dst目的地
		dfs(matrix, 0, 0, [], dst)

	except:
		break
