def dog(name):
	print('道哥%s开始准备吃食物啦。。。。。。。。。。' % name)
	while True:
		# x拿到的是yield接收到都值
		x = yield
		print('道哥%s吃到了%s，提前恭喜了' % (name, x))


# 调用函数生成一个生成器，yield有两个功能，一个是返回值，一个是用于接收值并赋值给一个变量
g = dog('alex')
# next(g)
g.send(None)  # 等同于next(g)

g.send('一根大骨头')
g.send('大肉包子')