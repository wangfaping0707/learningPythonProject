"""
一、可变长度的位置参数：
*形参名：用来接收溢出的位置参数，溢出的位置实参会被*保存成元组的格式，然后赋值给紧随其后的形参名
*后可以是任意的名字，但是约定俗成是args
"""


def add(x, y, *args):
	print(x, y, args)
	print(type(args))


add(1, 2, 3, 4, 5, 6, 7, 8, 98)


def func(*args):
	res = 0
	for item in args:
		res += item

	return res


print('累加的和:', func(1, 2, 3, 4))
