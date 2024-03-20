# 装饰器就是在不修改 被装饰对象源代码 以及 调用方式 的前提下为 被装饰对象添加新功能
import time


def index(x, y):
	time.sleep(3)
	print('index: %s %s' % (x, y))


def outter(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		stop = time.time()
		print(stop - start)
	return wrapper



f = outter(index)(1111,3444)
print('----------------------------------')
index = outter(index)
index(9999,32423)

