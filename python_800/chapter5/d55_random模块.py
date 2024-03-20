import random

# 取0-1之间随机的浮点数
print(random.random())

# 取自己定义范围的浮点数
print(random.uniform(5, 9))

# 取1-100的随机数，双开区间，1  100都能取到
print(random.randint(1, 100))

# 取1-100的随机数，半开区间，1能取到 3取不到
print(random.randrange(1, 3))

# 可以随机取到自己定义的各种类型，比如数字 字符串 列表 元组等等
print(random.choice([133, '人世间的苦难', ['a', 'b', 'c'], (23, 454, 565), {'a': 1, 'b': 23}]))

# 与上面的相比可以随机从列表中取出2个值或指定个数值
print(random.sample([133, '人世间的苦难', ['a', 'b', 'c'], (23, 454, 565), {'a': 1, 'b': 23}, 6466, 'abcd'], 3))

# 随机洗牌，就是打乱原序列的顺序，随机排序
item = [1, 3, 5, 67, 9, 11, 13, 15, 17, 19, 21]
random.shuffle(item)
print('洗牌之后：', item)
