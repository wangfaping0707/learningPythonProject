def func(start, stop, step=2):
	print('start............')
	while start < stop:
		yield start
		print('我看看')
		start += step
	print('end............')


# 只要函数体内的代码中含有yield关键字，那么调用这个函数不会触发函数体代码的运行，而是会生成一个生成器，生成器就是自定义迭代器
# 在使用生成器的函数逐个取值
g = func(0, 8, 2)
print(g)
print(g.__next__())  # 等价于next(g)方法
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
