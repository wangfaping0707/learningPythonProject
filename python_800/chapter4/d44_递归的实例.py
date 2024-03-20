# 实例1：推算年龄
# 回溯：函数一层一层调用下去
# 递推：满足某种结束条件，结束递归调用，然后一层层返回
def age(n):
	if n == 1:
		return 18
	return age(n - 1) + 10


res = age(5)
print('res:', res)

# 实例2：需求打印出所有列表中的元素
lis = [1, [2, [3, [4, [5, [6, [7, [8, 9, 10]]]]]]]]


def f1(L):
	for x in L:
		if type(x) is list:
			f1(x)
		else:
			print(x)

f1(lis)