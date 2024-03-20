s = 'spam'
ret = s.find('pa')
print('输出对象ret:', ret)
print(type(ret))

S = 'spammy'
s1 = S[:3] + 'XX' + S[5:]
print('输出对象s1:', s1)

s2 = S.replace('mm', 'YY')
print('输出对象s2:', s2)


str = 'spammy'
L = list(str)
print(L)
L[3] = 'Z'
L[4] = 'Z'
print('变化后的L：', L)

str = ''.join(L)
print(str)

str1 ='|'.join(L)
print(str1)

print('--------------------------------------------------')

line = 'aaa bbb  ccc'
cols = line.split()
print('输出打印：', cols)
print('重新组成字符串：',''.join(cols))

line1 = 'bob,hacker,40'
print('分割字符串：', line1.split(','))


line2 = 'The knights who say Ni!\n'
print(line2.rstrip())
print(line2.upper())
print(line2.isalpha())
print(line2.startswith('The'))
print(line2.endswith('Ni!\n'))



