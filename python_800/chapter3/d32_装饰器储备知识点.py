def index(x, y):
	print(x, y)


def wrapper(*args, **kwargs):  # 形参接收：args=(1,2,3,4,5) kwagrs = {'a':33,'b':44}
	index(*args, **kwargs)  # 实参打散：index(*(1,2,3,4,5),**{'a':33,'b':44}) =>index(1,2,3,4,5,a=33,b=44)


wrapper(1, 2, 3, 4, 5, a=33, b=44)

# 调用wrapper函数的参数相当于直接传给了index参数
wrapper(111, 222)
