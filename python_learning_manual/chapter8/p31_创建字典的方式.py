# 方式一：字面量赋值
D = {'name': 'Bob', 'age': 40}

# 方式二：键值赋值
D1 = {}
D1['name'] = 'Bob'
D1['age'] = 40

# 方式三：使用字典的构造函数dict()
D2 = dict(name='BOb', age=40)

# 方式四：使用列表元组方式
D3 = dict([('name', 'Bob'), ('age', 40)])

'''
这四种形式都会建立相同的两键字典，但它们有着不同的适用条件：
1、如果你可以事先拼出整个字典，那么第一种是很方便的
2、如果你需要一次动态的建立字典的一个字段，第二种比较合适
3、第三种关键字形式所需的代码比字面量少，但键必须都是字符串才行
4、如果你需要在程序运行时通过序列构建字典，那么最后一种形式比较有用
'''

list_key = ['name', 'job' , 'salary']
list_value = ['小鱼儿', 'manager', 37000]

D4 = dict(zip(list_key, list_value))

print('输出D4：', D4)


# 用字典的fromkeys方法创建一个新字典，其中包含指定的键，且每个键对应的值都是None
D5 = {}.fromkeys(['name', 'age'])
print('输出D5:', D5)

"""
这个示例首先创建了一个空字典，在对其调用方法fromkeys来创建另一个字典，这显的有点多余，你可以不这样做，而是直接对dict (前面说过,dict是所有字典所属的类型。
相当于直接用类名调用方法，而不是通过创建对象再来调用方法)调用方法fromkeys
"""
D6 = dict.fromkeys(['name','age'])
print('输出D6:', D6)

# 如果你不想使用默认值None，可提供特定的值
D7 = dict.fromkeys(['name', 'age'], 'unknown')
print('输出D7:', D7)


# 使用字典推导表达式来创建字典
print(zip(['a', 'b', 'c'],[1, 2, 3]))
print(list(zip(['a', 'b', 'c'],[1, 2, 3])))



D8 = {k: v for (k, v) in zip(['d', 'e', 'f'], [100, 200, 300])}

print('输出打印D8：', D8)

print('---------------------------------------------')

D9 = {x:x**2 for x in range(0,5)}
print('输出D9：', D9)

D10 = {c:c*4 for c in 'SPAM'}
print('输出D10：', D10)

D11 = {c.lower():c+'!' for c in ['EGGS','SPAM','LOVE']}

print('输出D11：', D11)





D12 = {'h':10, 'g':1, 'a':20}

for k in  sorted(D12):
	print(k, D12[k])












