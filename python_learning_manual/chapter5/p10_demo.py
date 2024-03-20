# 创建一个集合可以使用内置的set的函数来创建，可以向内置的set函数传入一个序列或者其它可迭代的对象
import math
x = set('abcde')
y = set('bdxyz')
print(x,y)

# 求集合x中含有而y中没有的元素
print(x -y)
# 求集合x和y的并集
print(x | y)
# 求集合x和集合y的交集
print(x & y)
# 求集合x和集合y互不包含的元素
print(x ^ y)


z = x.intersection(y)
print('输出z：', z)
z.add('spam')
print(z)

z.update(set(['nihao','我的']))
print(z)

print(dir(z))


set = {x*2 for x in 'spam'}
print(set)

for s in set:
	print(s, end=' ')




