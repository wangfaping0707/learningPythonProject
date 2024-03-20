from collections.abc import Iterable

d = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44, 'k5': 55, 'k6': 66, 'k7': 77}

# keys()   values()  items() 在python2中会一次性返回对应的列表，比较耗费内存空间，因此，在python3当中做了优化，就是老母鸡下蛋
# 要一个，返回一个，如下所示，其实也是一个可迭代对象，可以使用for循环进行取值

print('取key：', d.keys(), type(d.keys()))
print('判断d.keys()是否是可迭代对象：', isinstance(d.keys(), Iterable))
print('取value：', d.values())
print('判断d.values()是否是可迭代对象：', isinstance(d.values(), Iterable))
print('取item', d.items())
print('判断d.items()是否是可迭代对象：', isinstance(d.items(), Iterable))

# 既然是可迭代对象，那么就可以使用for循环进行取值
for k in d.keys():
	print('k的值：', k)


for v in d.values():
	print('v的值：', v)


for k, v in d.items():
	print(k, v)

for item in d.items():
	print(item)





