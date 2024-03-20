# 字典的删除方法

d = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44, 'k5': 55, 'k6': 66, 'k7': 77}
print('删除之前的打印：', d)

# 通用的删除方式，没有返回值
del d['k1']
print('通用方法删除后：', d)

# pop删除，根据字典的key来删除元素，返回key对应的那个value值
res1 = d.pop('k2')
print('打印res1的值：', res1)
print('pop方法删除后：', d)

# popitem 删除，随机删除，返回元组(key,value)
res2 = d.popitem()
print('打印res2的值：', res2)
print('popitem方法删除后：', d)

