# 用法1
list = ['h', 'e', 'l', 'l', 'o']
str1 = ''.join(list)
print('输出：', str1)
# 用法2
str2 = '+'.join(list)
print(str2)
print('1233'.join(list))

# split的用法
num = 1230.045
print('num的类型：',type(num))
str3 = str(num)
print(type(str3),str3)

L = str3.split('.')
print(L)
L2 = []

for x in L:
	y = x[::-1]
	z = y.strip('0')
	L2.append(z)

str4 = '.'.join(L2)
print(str4, type(str4))

print(float(str4))
print(type(float(str4)))















