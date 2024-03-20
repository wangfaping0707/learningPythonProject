import time


# 显示进度条函数,打印逻辑代码抽象为一个可复用的函数
def progess(percent, rec_size):
	res = int(50 * percent) * '#'
	# print('\r[%-50s %d%%]' % (res, int(100 * percent)), rec_size, end='')
	print('\r[{:<50} {}%]'.format(res, int(100 * percent)),rec_size, end='')


# 假设每次加载数据量都是1024, rec_size是已经接收的数据量，total_size是总的数据量

def cur(total_size, rec_size=0):
	while rec_size < total_size:
		time.sleep(0.05)
		remain_size = total_size - rec_size
		if remain_size < 1024:
			rec_size += remain_size
		else:
			rec_size += 1024
		percent = rec_size / total_size
		progess(percent, rec_size)


cur(333333)
# cur(1027)
