import time

# 时间分为三种格式
# 一、时间戳：从1970年到现在经过的秒数：主要用于时间间隔的计算
print('时间戳:', time.time())

# 二、按照某种格式显示时间：2023-04-19 23:52:30，主要用于展示时间，不能用于计算
print('格式化显示时间：', time.strftime('%Y-%m-%d %H-%M-%S %p'))
print('格式化显示时间：', time.strftime('%Y-%m-%d %X %p'))

# 三、结构化显示时间，主要用于单独获取时间的某一部分
res = time.localtime()
print('res:', res)
print(res.tm_year)
print(res.tm_mday)
