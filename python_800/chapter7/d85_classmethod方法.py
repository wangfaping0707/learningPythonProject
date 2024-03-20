import setting

'''
绑定方法：特殊指之处在于将调用者本身当做第一个参数自动传入
1、绑定给对象的方法：调用者是对象，自动传入的是对象
2、绑定给类的方法：调用者是类，自动传入的是类

'''


class Mysql:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	def fun(self):
		print(f'{self.ip} : {self.port}')

	# 将下面的函数装饰成绑定给类的方法
	@classmethod
	def from_conf(cls):
		print(f'验证cls：{cls}')
		return cls(setting.ip, setting.port)


# obj_m = Mysql(setting.ip, setting.port)
# obj_m.fun()
obj_m1 = Mysql.from_conf()
print(obj_m1.__dict__)
