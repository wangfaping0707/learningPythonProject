class People:
	def __init__(self, name):
		self.__name = name

	def set_name(self, val):
		if type(val) is not str:
			print('姓名需为字符串类型。。。。。')
			return
		self.__name = val

	def get_name(self):
		return self.__name

	def del_name(self):
		print('姓名不转删除，只能修改')

	name = property(get_name, set_name, del_name)


p1 = People('egon')
print(p1.name)
del p1.name