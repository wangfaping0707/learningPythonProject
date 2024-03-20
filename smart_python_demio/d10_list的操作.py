# 类型转换，凡是能够被for循环遍历的类型都可以当作参数传递给list()转换成列表

# 字符串
res = 'hello'
print('字符串转换成列表：', list(res))

# 字典
d = {'k1': '我', 'k2': '爱', 'k3': '你'}
print('字典转换成列表：', list(d))

# 字典的循环
for k, v in d.items():
	print(k, v)

# 列表的常规操作：内置方法
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]

l1 = [111, 222, 333]

# append 方法会将后续添加的一个子列表当作一个元素添加进去
list1.append(l1)
print('追加后的list1:', list1)

# extend方法 会将后续添加的一个子列表拆分，把其中的元素一个个添加进去
list2.extend(l1)
print('追加后的list2:', list2)

# 往列表中指定位置插入值
list2.insert(3, 'Mylove')

print('插入之后的list2:', list2)

# 字符串倒序排列
string = 'hello'

print('方式1：', string[::-1])

print(reversed(string))











