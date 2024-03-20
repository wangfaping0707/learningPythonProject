"""
日志配置字典LOGGING_DIC:

1、定义三种日志输出格式，日志中可能用到的格式化串如下：
%(name)s  Logger的名字  即日志的名字
%(levelno)s  数字形式的日志级别
%(levelname)s  文本形式的日志级别
%(pathname)s  调用日志输出函数的模块的完整路径名，可能没有
%(filename)s  调用日志输出函数的模块的文件名
%(module)s  调用日志输出函数的模块名
%(funcName)s  调用日志输出函数的函数名
%(lineno)d  调用日志输出函数的语句所在的代码行
%(created)f  当前时间，用UNIX标准的表示时间的浮点数来表示
%(relativeCreated)d  输出日志信息时的Logger创建以来的毫秒数
%(asctime)s  字符串形式的当前时间
%(thread)d  线程id，可能没有
%(threadName)s  线程名，可能没有
%(process)d  进程ID，可能没有
%(message)s 用户输出的消息

2、 logging日志模块四大组件
Logger （日志器） ：提供了程序使用日志的入口 ，负责产生不同级别的日志，日志的产生者，产生的日志会传递给handler然后控制输出，可以决定那个接收者接收
Handler （处理器 ）：将 logger 创建的日志记录发送到合适的目的输出，日志的接收者，可以定义不同的接收者，不同的handler会将日志输出到不同的位置
Formatter（ 格式器 ）：决定日志记录的最终输出格式
Filter （过滤器 ）：提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录


"""
# 2、强调：其中的 %(name)s 为getlogger时指定的名字
standard_format = '[%(asctime)s] [%(threadName)s:%(thread)d] [日子的名字:%(name)s] [%(filename)s:%(lineno)d] [%(levelname)s] [%(message)s]'
simple_format = '[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] [%(message)s]'
test_format = '[%(asctime)s] [%(message)s]'

# 3、日志配置字典
LOGGING_DIC = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'standard': {
			'format': standard_format
		},
		'simple': {
			'format': simple_format
		},
		'test': {
			'format': test_format
		}
	},
	'filters': {},
	# handlers是日志的接收者，不同的handler会将日志输出到不同的位置
	'handlers': {
		# 打印到终端的日志
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',  # 打印到屏幕
			'formatter': 'simple'
		},
		# 打印到文件的日志，收集到info及以上的日志
		'default': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',  # 保存到文件
			'formatter': 'standard',
			'filename': 'a1.log',
			'encoding': 'utf-8'
		},
		'other': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',  # 保存到文件
			'formatter': 'test',
			'filename': 'a2.log',
			'encoding': 'utf-8'
		},
		# 演示日志轮转
		'default9': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingHandler',  # 保存到文件
			# 存储的日志大小，以字节为单位 1024byte=1k 1024k=1M  -->5M
			# 'maxBytes':1024*1024*5
			'maxBytes': 100,
			'backupCount': 5,
			'formatter': 'standard',
			'filename': 'a9.log',
			'encoding': 'utf-8'
		}
	},
	# loggers日志的产生者，产生的日志会传递给handler，然后控制输出
	'loggers': {
		# logging.getLogger(__name__) 拿到的logger的配置
		'kkk': {
			'handlers': ['other', 'console'],
			'level': 'DEBUG',
			'propagate': False
		},
		'bbb': {
			'handlers': ['console'],
			'level': 'DEBUG',
			'propagate': False
		},
		'ddd': {
			'handlers': ['console', 'default'],
			'level': 'DEBUG',
			'propagate': False
		},
		'': {
			'handlers': ['console', 'default'],
			'level': 'DEBUG',
			'propagate': False
		},
		'日志轮转': {
			'handlers': ['console', 'default9'],
			'level': 'DEBUG',
			'propagate': False
			# }
		}
	}
}