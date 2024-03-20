"""
如何自定义元类，来控制类的产生：

class机制造People类的时候分四步：

1、拿到类名；
2、拿到类的基类(父类)，类的基类默认是Object；
3、执行类体代码，拿到类的名称空间；
4、调用元类(metaclass=Mymeta) 完成一个类的实例化，即是创建了类People
People = Mymeta(class_name,class_bases,class_doc)

调用Mymeta发生的三件事, 调用Mymeta 就是调用Mymeta的类，也就是type内的__call__()方法，即type.__call__()
(1)、先造一个空对象===>People,调用类内的__new__方法;
(2)、调用Mymeta这个类内的__init__方法，完成初始化对象的操作；
(3)、返回初始化好的对象；
"""


# 只有继承了type类的类才是元类
class Mymeta(type):
	# self:空对象       x:类名   y:基类  z:类的名称空间
	def __init__(self, x, y, z):
		print('2、执行init方法，对new方法造出的空对象进行初始化过程。。。。。。。。')
		# print(f'self: {self}')
		# print(f'x: {x}')
		# print(f'y: {y}')
		# print(f'z: {z}')
		# print('===========================================')
		if not x.istitle():
			raise NameError('类名首字母需要大写啊！！！')

	def __new__(cls, *args, **kwargs):
		print('1、我是造空对象的时候就运行，且在__init__方法之前运行哦！！！')
		# 这个方法必须要返回一个空对象，但自身不能返回，所以需要问它的父类要，调用父类的方法来返回一个对象
		# 方式1：super().__new__(cls, *args, **kwargs)
		# 方式二，如下：
		return type.__new__(cls, *args, **kwargs)

	def __call__(self, *args, **kwargs):
		# 1、Mymeta.__call__函数内会先调用 People 内的__new__；
		p_obj = self.__new__(self)
		# 2、Mymeta.__call__函数内会调用 People 内的__init__；
		self.__init__(p_obj)
		# 3、Mymeta.__call__函数内会返回一个初始化好的对象
		return p_obj


"""
类的产生：
People = Mymeta() ===> type.__call__干了三件事
1、type.__call__ 函数内会先调用Mymeta内的__new__；
2、type.__call__ 函数内会用Mymeta内的__init__;
3、type.__call__ 函数内会返回一个初始化好的对象；

"""


class People(object, metaclass=Mymeta):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say(self):
		print(f'<{self.name}  :  {self.age}>')

	def __new__(cls, *args, **kwargs):
		print(f'people_cls:{cls}')
		return object.__new__(cls)


"""
类的调用：
obj = People('egon',18) ===> Mymeta.__call__干了3件事
1、Mymeta.__call__函数内会先调用 People 内的__new__；
2、Mymeta.__call__ 函数内会用 People 内的__init__;
3、Mymeta.__call__ 函数内会返回一个初始化好的对象；

"""

"""
结论：
1、对象可调用：对象()---> 对象所属的类，必须要有__call__()方法
2、类可调用：类()---> 类的 自定义元类 必须要有__call__()方法
3、自定义元类可调用：自定义元类()---> 自定义元类的内置类 必须要有__call__()方法

"""
p_obj = People('EGON',18)