# 常见字典字面量和操作
# 空字典
D = {}
# 有两个元素的字典
D1 = {'name': 'Bob', 'age': 40}
# 字典的嵌套
D2 = {'cto': {'name': 'Bob', 'age': 40}}
# 字典的构造方法:关键字
D3 = dict(name='Bob', age=40)
# 键值对
D4 = dict([('name', 'Bob'), ('age', 40)])
print('输出打印D4：', D4)

# 字典推导
D5 = {x: x * 2 for x in range(0, 10)}
print(D5)

D3 = {'eggs': 4, "spam": 2, 'ham': 1, 'name': '小鱼儿'}

print('字典D3的长度：', len(D3))

print('判断name键是否在字典D3当中：', 'name' in D3)

print(D3.keys())
print(type(D3.keys()))
print(list(D3.keys()))
print('----------------------------------------------------------')
print(D3.values())
print(list(D3.values()))
print('----------------------------------------------------------')
print(D3.items())
print(list(D3.items()))
# 字典当中，读取不存在的键往往都会出错，然而键不存在时通过get方法能够返回默认值None或者用户定义的默认值。
print('读取存在的字典键值：', D3['eggs'])
# 读取不存在的字典键是，会报keyerror错误
# print(D3['pop'])
print('没有指定默认值：', D3.get('pop'))
print('指定默认值：', D3.get('pop', 'Hello World'))

print(D3)






