class E:
	def test(self):
		print('from E......')


class B(E):
	def test(self):
		print('from B....')


class F:
	def test(self):
		print('from F....')


class C(F):
	def test(self):
		print('from C...')


class D:
	def test(self):
		print('from D......')


class A(B, C, D):
	def test(self):
		print('from A.......')


print(A.mro())

obj = A()
obj.test()
