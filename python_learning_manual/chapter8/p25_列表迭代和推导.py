
# 列表推导表达式
res = [c * 4 for c in range(0, 10)]
print('输出res：', res)

res1 = [d * 5 for d in 'spam']
print('输出res1：', res1)

# 列表推导表达式相当于下述代码
res2 = []
for c in 'spam':
	res2.append(c * 5)

print('打印res2:', res2)

# 内置函数map能实现类似的效果，但它对序列中的各项应用一个函数并把结果收集到一个新的列表中


def add(a, b):
	return a + b


list3 = list(map(add, [1, 2, 3], [4, 5, 6]))
print('打印list3：', list3)

list4 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print('打印list4：', type(list4))
print('转换输出：', list(list4))