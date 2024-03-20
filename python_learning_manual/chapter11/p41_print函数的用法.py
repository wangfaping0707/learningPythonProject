import sys

x = 'spam'
y = '999.99'
z = ['eggs', 'hams', 'loving']
print('第一次打印：', x, y, z)
# 关闭对象之间的空格，sep = ''
print(x, y, z, sep='', end='!!!!!\n')
print(x, y, z, sep='，')
print('--------------------------------')
print(x, y, z, sep='...', file=open('data.txt', 'a+'))


a = '小明'
b = '小乐'
# 第一种方式
print(a, b)
# 第二种方式
sys.stdout.write(a + ' ' + b + '\n')


















