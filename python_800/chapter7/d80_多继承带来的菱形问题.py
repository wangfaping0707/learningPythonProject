class A(object):
	def test(self):
		print('from A.......')


class B(A):
	def test(self):
		print('from B......')


class C(A):
	def test(self):
		print('from C.......')


class D(B, C):
	pass


obj = D()
obj.test()
# 类以及该类的对象访问属性都是参照该类的mro列表
print(D.mro())









