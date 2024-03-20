# 经典类，多继承的属性查找是深度优先，即一条链路查找到底，第一次就把最上层类查找完
# 新式类，多继承的属性查找是广度优先，优先把每条分支都查找一遍，最后在查上层类，大脑袋最后差

class G:
	def test(self):
		print('from  G.....')


class E(G):
	def test(self):
		print('from E......')


class B(E):
	def test(self):
		print('from B....')


class F(G):
	def test(self):
		print('from F....')


class C(F):
	def test(self):
		print('from C...')


class D(G):
	def test(self):
		print('from D......')


class A(B, C, D):
	def test(self):
		print('from A.......')


print('验证新式类的广度优先：', A.mro())

obj = A()
obj.test()
