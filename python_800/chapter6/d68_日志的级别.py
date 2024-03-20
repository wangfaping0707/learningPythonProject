import logging


# 设置日志输入格式
logging.basicConfig(
	# 日志输出的位置有两个，1、终端  2、文件  不指定，默认打印到终端
	filename='access.log',
	# 	日志格式
	format='%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s',
	# 	时间格式
	datefmt='%Y-%m-%d %H:%M:%S %p',
	level=10


)

logging.debug('调试Debug')
logging.info('日常消息记录')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')




