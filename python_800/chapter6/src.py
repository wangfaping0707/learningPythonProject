# 接下来要做的是：拿到日志的生产者即loggers来产生日志
# 第一个日志的产生者kkk
# 第二个日志的产生者kkk
# 但是需要先导入日志配置字典LOGGING_DIC
import d69_settings
import logging.handlers
from logging import config
from logging import getLogger


# 将配置字典加载进来
config.dictConfig(d69_settings.LOGGING_DIC)

# 获取日志字典中的某一个logger来产生日志
logger1 = getLogger('kkk')
logger1.info('这是logger1产生的info日志，请知悉！')

# 只想往终端输入
logger2=getLogger('bbb')
logger2.info('这是logger2的专属日志！！！')

# 往标准格式中写入日志
logger3 = getLogger('ddd')
logger3.info('这是logger3产生的最复杂的日志。。。。。')

# 产生用户交易的日志，交易logger
logger4 = getLogger('用户交易')
logger4.info('这是交易logger4的日常运行日志。。。。。')

# 产生用户交易的日志，体现logger
logger5 = getLogger('提现操作')
logger5.info('这是交易logger5的日常运行日志。。。。。')


# 测试日志轮转效果，即记录日志文件的内容到达指定大小时，重新重命名原日志文件，然后执行程序会重新生成文件，在记录内容
# logger9 = getLogger('日志轮转')
# logger9.info('进行日志轮转功能验证，这是logger9产生的日志，哈哈哈')



