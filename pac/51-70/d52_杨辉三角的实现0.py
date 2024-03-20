"""
杨辉三角

          1            第 0 行
        1   1          第 1 行
       1  2  1         第 2 行
      1  3  3  1       第 3 行
    1  4  6   4  1     第 4 行
   1 5  10  10  5  1   第 5 行
"""
# 要生成多少行杨辉三角
# n = int(input().strip())
n = 5
# 第一行和第二行是固定写死的,所以要从 第二行开始循环构造子列表 [1, 2, 1]
data = [[1], [1, 1]]

for i in range(2, n):
	# 子列表开始和结束都是1，固定写死的
	d = [1]
	for j in range(i - 1):
		d.append(data[i - 1][j] + data[i - 1][j + 1])
	# print(d)
	d.append(1)
	data.append(d)

print(data)
print('==================================================')
for s in data:
	print(s)
