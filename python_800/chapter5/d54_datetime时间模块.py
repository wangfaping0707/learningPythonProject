import datetime


# 获取当前符合人类阅读的时间格式，且这种格式可以直接参与计算

print(datetime.datetime.now())

#  3天后的时间是多少

print(datetime.datetime.now() + datetime.timedelta(days=3))

print(datetime.datetime.now() + datetime.timedelta(days=365))

print(datetime.datetime.now() + datetime.timedelta(weeks=7))