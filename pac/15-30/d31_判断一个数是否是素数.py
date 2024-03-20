# 方法1：一个数只能被1和自身整除，才能称为是素数，for循环最多要循环  num -2 次
def method1(num):
	num = int(num)
	if num <= 1:
		return '请输入大于1的数'
	elif num == 2:
		return '2是素数'
	for i in range(2, num):
		if num % i == 0:
			return f'{num}不是素数'
	return f'{num}是素数'


print(method1(12))


# 方法2：一个数只能被1和自身整除，才能称为是素数，for循环最多要循环  num -2 次
def method2(num):
	num = int(num)
	if num <= 1:
		return '请输入大于1的数'
	elif num == 2:
		return '2是素数'
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return f'{num}不是素数'
	return f'{num}是素数'


print(method2(20))

"""
我们知道偶数中，只有2是素数，其它偶数都不是素数，而且奇数的因数也没有偶数，所以我们后续判断一个数是不是素数
只需要判断基数即可
"""


def method3(num):
	num = int(num)
	if num <= 1:
		return '请输入大于1的数'
	elif num == 2:
		return '2是素数'
	for i in range(2, int(num ** 0.5 + 1)):
		if num % i == 0:
			return f'{num}不是素数'
	return f'{num}是素数'



print(method3(9))