# 字典的定义方式
d1 = dict(x=1, y=2, z=3)
print('d1:', d1)

# 数据类型转换
info = [
	['name', 'egon'],
	['age', 18],
	['sex', 'male'],
	['salary', 900000]
]
# 将列表中的信息转化成字典进行存储
d2 = {}
for item in info:
	d2[item[0]] = item[1]

print('字典d2的值：', d2)

# 可使用列表的解压赋值
d3 = {}
for k, v in info:
	d3[k] = v

print('字典d3的值:', d3)

# 直接使用dict()函数
print('直接使用dict()函数转换：', dict(info))


# 快速初始化字典

keys = ['name', 'age', 'gender']

d4 = {}.fromkeys(keys, 100)
print('字典d4的值：', d4)














