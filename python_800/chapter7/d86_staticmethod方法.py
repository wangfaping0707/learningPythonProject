'''
非绑定方法：静态方法
没有绑定给任何人：调用者可以是类、对象，没有自动传参的效果
非绑定看到的就是函数，绑定的看到就是方法
'''
import setting


class Mysql:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	# 将下述函数装饰成一个静态方法
	@staticmethod
	def creat_id():
		import uuid
		return uuid.uuid4()

	@classmethod
	def f1(cls):
		pass

	def f2(self):
		pass


m = Mysql(setting.ip, setting.port)

print('没有绑定对象的就是函数：', Mysql.creat_id)
print('绑定给类的就是方法：', Mysql.f1)
print('绑定给对象的也是方法：', m.f2)

print('对象id：', Mysql.creat_id())
