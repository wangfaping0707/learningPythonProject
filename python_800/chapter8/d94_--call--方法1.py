# 如果想让一个对象加括号 变成可调用，需要在该对象的类中添加一个方法，__call__()
class Foo:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __call__(self, *args, **kwargs):
		print('__call__方法已经运行过了。。。。。')
		print(f'=====>: {args}  {kwargs}')
		return 'call方法执行成功了'


f_obj = Foo(18, 17)

# 如果想让  f_obj() 变为可执行状态，需要在Foo类中添加__call__方法，res = f_obj()  就相当于 res = f_obj.__call__()
res = f_obj(1, 2, 3, 4, 5, a=21, b=22, c=23, d=24)
print(f'res: {res}')
