msg = 'hello world'
print('获取字符串msg的索引第一个值：', msg[0])

print(msg[0:5:2])

# 复制一个字符串
res1 = msg[:]
print('res1:', res1)

# 将字符串倒叙获取
res2 = msg[::-1]
print('res2:', res2)

# 统计字符串的长度
print('msg的长度：', len(msg))

msgs = 'you can you up no can no bb'

# 所有的都替代
print(msgs.replace('you', 'YOU'))

# 只替代一次
print(msgs.replace('you', 'YOU', 1))

# 判断字符串是否是数字组成
str1 = '123456'
str2 = '1233.45'

print('str1是否由纯数字组成：', str1.isdigit())

print('str2是否由纯数字组成：', str2.isdigit())

str3 = 'hello egon hah'

# find查找子字符串在大字符串中的索引

index = str3.find('llo')
print(index)








