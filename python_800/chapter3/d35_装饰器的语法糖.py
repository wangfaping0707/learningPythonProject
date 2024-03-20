# 装饰器就是在不修改 被装饰对象源代码 以及 调用方式 的前提下为 被装饰对象添加新功能
# 如果被装饰的函数有返回值
import time


def outter(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = func(*args, **kwargs)
		stop = time.time()
		print('函数的运行时间：', stop - start)
		return res

	return wrapper


# 在被装饰对象的正上方的单独一行写@装饰器名字
@outter  # index = outter(index)
def index(x, y):
	time.sleep(3)
	print('打印index: %s %s' % (x, y))
	return '我是index函数的执行返回值{} {}'.format(x, y)


res = index(99999, 1000000)
print('返回值======》', res)
