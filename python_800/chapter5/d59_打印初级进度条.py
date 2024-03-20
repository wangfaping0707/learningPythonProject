import time
# 下面是两种打印方式

res = ''
for i in range(0, 50):
	res += '#'
	time.sleep(0.5)
	# print('\r[%-50s]' % res, end='')
	print('\r[{:<50}]'.format(res), end='')
