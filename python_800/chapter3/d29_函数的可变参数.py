def index(x, y, z):
	print(x, y, z)


def wrapper(*args, **kwargs):
	print('args打印:', args)
	print('kwargs打印:', kwargs)
	index(*args, **kwargs)  # index(*(1,2),**{'z':33})


# wrapper函数的参数格式，是受到index函数的影响的
wrapper(1, 2, z=33)
print('==============================================》')
wrapper(77, y=99, z=1099)
