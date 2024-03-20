l = ['egon', 'lxx', 'wxx', 'sxx']

# 对列表中的每一个元素进行加工
# 方法1：列表推导表达式
new_l = [name + '_dsb' for name in l]
print('列表推导表达式', new_l)

# 方法二：试用map函数
new_l1 = map(lambda name: name + '_dda', l)
print(type(new_l1))
print('这是一个生成器：', new_l1)
print('使用list()函数返回：', list(new_l1))

# 参考文档：https://blog.csdn.net/mi2shao/article/details/124670593