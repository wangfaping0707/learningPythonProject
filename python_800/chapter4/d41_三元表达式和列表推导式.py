# 三元表达式语法：条件成立时要返回的值 if 条件 else 条件不成立时要返回的值

x = 1000
y = 105
res = x if x > y else y
print('res的值：', res)

print('-------------------------------------------------')

# 列表推导表达式
l = ['wang_dsb', 'egon_dsb', 'wxx_dsb', 'kxh_dsb', 'jkl']
# 将列表中的值，含有dsb提取成为一个新列表

new_l = [name for name in l if name.endswith('dsb')]
print('new_l:', new_l)

# 把所有消息额字母全部变成大写字母

new1 = [name.upper() for name in l]
print('new1:', new1)

# 把所有名字去掉后缀
new2 = [name.split('_dsb')[0] for name in l]

print('去掉后缀方式一：', new2)

new3 = [name.replace('_dsb', '') for name in l]
print('去掉后缀方式二：', new3)

price_l = ['鸡蛋%s' % i for i in range(10)]
print('price_l:', price_l)
