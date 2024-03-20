# 元组的拼接
t = (1, 2, 3) + ('a', 'b', 'c')
print('输出元组t：', t)

# 元组的重复
t1 = tuple('spam')* 4
print('输出元组t1：', t1)

print(t[0],t[1:3])
# 在赋值语句的上下文中，即使没有圆括号，python也能够识别出这是一个元组
t2 = 0, 'Ni', 1.2, 3
print('输出元组t2；', t2)

# 元组的排序:如果想对元组进行排序，通常先得将它转换为列表从而使其变为一个可变对象，才能使用排序方法调用，或者使用新的内置函数sorted，它接受任何可迭代对象
# 方式一：
T = ('cc', 'dd', 'aa', 'bb')
tmp = list(T)
tmp.sort()
print('排序之后的tmp：', tmp)
# 将排序之后的tmp进行元组转换
T = tuple(tmp)
print('转换之后的T：', T)

# 方式二：使用内置函数
T1 = ('xx', 'ss', 'hh', 'ff')
T2 = sorted(T1)
print('转换之后的T2：', T2)



