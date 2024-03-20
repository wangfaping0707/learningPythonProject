"""
如何自定义元类，来控制类的产生：

class机制造People类的时候分四步：

1、拿到类名；
2、拿到类的基类(父类)，类的基类默认是Object；
3、执行类体代码，拿到类的名称空间；
4、调用元类(metaclass=Mymeta) 完成一个类的实例化，即是创建了类People
People = Mymeta(class_name,class_bases,class_doc)

调用Mymeta发生的三件事：
(1)、先造一个空对象===>People;
(2)、调用Mymeta这个类内的__init__方法，完成初始化对象的操作；
(3)、返回初始化好的对象；
"""


# 只有继承了type类的类才是元类
class Mymeta(type):
	# self:空对象 x:类名  y:基类 z:类的名称空间
	def __init__(self,x,y,z):
		print('开始执行元类 造类People的过程。。。。。')
		print(f'self: {self}')
		print(f'x: {x}')
		print(f'y: {y}')
		print(f'z: {z}')
		print('===========================================')
		if not x.istitle():
			raise NameError('类名首字母需要大写啊！！！')


class People(object, metaclass=Mymeta):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say(self):
		print(f'<{self.name}  :  {self.age}>')
