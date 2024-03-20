l = ['egon_sb', 'lxx_sb', 'wxx', 'sxx']

# 需求：将列表l中sb结尾的元素过滤出来
# 方法1：列表表达式
res = [name for name in l if name.endswith('sb')]
print('方式一：', res)

# 方式二：使用filter函数进行过滤
new_res = filter(lambda name: name.endswith('sb'), l)
print('返回的类型式一个迭代器：', type(new_res))
print('返回一个迭代器:', new_res)
print('使用list()函数生成一个列表：', list(new_res))