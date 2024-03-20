# 集合的作用: 1、 关系运算   2、去重
friend1 = ['meifang', 'wangying', 'jack', 'Lily']
friend2 = ['meifang', 'wangying', 'iven', 'hk1y']
# 需求是求出 friend1 和 friend2 的共同好友
# 方法1：笨方法
L = []
for x in friend1:
	if x in friend2:
		L.append(x)

print('friend1和friend2的共同好友：', L)

# 集合的特点：1、集合中元素必须为不可变类型  2、集合中的元素是无序  3、集合中的元素不能重复
# {}是被认为是空字典，字典和集合的运算符是相同的
# 定义空集合
s = set()

# 定义一个非空集合
s1 = set('hellolloklldjcj')
print('打印集合s1:', s1)

s2 = set(['egon', 1, 2, 3, 4, 3, 2, 1])
print('打印集合s2:', s2)
