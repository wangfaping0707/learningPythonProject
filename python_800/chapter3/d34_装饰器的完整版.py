# 装饰器就是在不修改 被装饰对象源代码 以及 调用方式 的前提下为 被装饰对象添加新功能
# 如果被装饰的函数有返回值
import time


def index(x, y):
	time.sleep(3)
	print('打印index: %s %s' % (x, y))
	return '我是index函数的执行返回值{} {}'.format(x, y)

def outter(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = func(*args, **kwargs)
		stop = time.time()
		print('函数的运行时间：', stop - start)
		return res

	return wrapper


index = outter(index)
res = index(9999, 32423)
print('返回值======》', res)
