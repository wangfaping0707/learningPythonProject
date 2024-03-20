
# 字典的update方法有点类似于拼接，但是，它和从左到右的顺序无关，它把一个字典的键和值拼接到另一个字典当中，当遇到冲突时盲目的覆盖相同键的值
D = {'eggs': 3, 'spam': 2, 'ham': 1}
D1 = {'toast': 4, 'muffin': 5, 'ham': 100000}
# 执行update方法
D.update(D1)
print('更新之后的打印：', D)
D['key'] = 'love'
print(D)
# 字典pop方法能够从字典中删除一个键并返回它的值
print(D.pop('key'))
print('删除之后的打印：', D)
print('---------------------------------------------')
# 遍历字典
for key in D:
	print(key + ':' + str(D[key]))

print('*****************************************************')

for (key, value) in D.items():
	print(key + ':' + str(value))

# 使用元组作为键
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

print('输出Matrix：', Matrix)
print('*****************************************************')

# 方式一：使用if语句预先检测不存在的键，避免程序发生异常
if (2, 3, 6) in Matrix:
	print(Matrix[(2,3,6)])
else:
	print('键(2，3，6)不存在')


# 方式二：使用try语句捕获并修复这一异常
try:
	print(Matrix[(2, 3, 6)])
except KeyError as e:
	print('输出：', e)
	print('使用try语句捕获异常///')

# 方式三：使用get语句提前设置默认值
print(Matrix.get((2, 3, 6), '您想要找的值不存在哦'))






dict()





