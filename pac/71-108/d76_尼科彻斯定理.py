"""
step1:输入一个数字，同时创建一个列表，便于保存奇数；
step2:对n*(n-1)+1 至 n*(n+1)，每隔一个数进行遍历，并将他们添加至列表中；
step3:对c逐一遍历，如果遍历到最后一位，直接打印i；其余都要把+带上
"""

n = int(input())
c = []
for i in range(n * (n - 1) + 1, n * (n + 1), 2):
	c.append(i)

print('+'.join(map(str, c)))

# for i in c:
# 	if i == c[-1]:
# 		print(i)
# 	else:
# 		print(i, end='+')


