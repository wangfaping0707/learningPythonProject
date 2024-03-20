import sys
# 字符串格式化输出：方法一

template = '{0},{1},{2}'
str = template.format('spam', 'ham', 'eggs')

print('输出打印str：', str)

example = '{motto},{pork},{food}'
print(example.format(motto='spam', pork='ham11', food='eggs'))

example1 = '{motto},{0},{food}'
print(example1.format('pig', motto='spring', food='apple'))


example2 = '{},{},{}'
print(example2.format('I','love','you'))

print('----------------分割线--------------------------------------')

# 字符串格式化输出：方法二
temp = '%s,%s,%s'
print(temp % ('巫术', '合', '剂'))

temp1 = '%(motto)s,%(pork)s and %(food)s'
print(temp1 % dict(motto='hello', pork='the', food='world'))
print('-----------------------------------------------------------------------')

# 位置参数
str1 = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})

print('输出打印str1:', str1)

# 关键字参数

str2 = 'My {map[kind]} runs {sys.platform}'.format(sys = sys, map = {'kind': 'laptop'})

print('输出打印str2:', str2)


somelist = list('SPAM')
str3 = 'first = {0},second = {1}, third = {2}'.format(somelist[0],somelist[1],somelist[2])
print('输出打印str3:', str3)

str4 = 'first = {0[0]},second = {0[2]},third = {0[3]}'.format(somelist)
print('输出打印str4:', str4)

str5 = 'first = {0},second = {1}'.format(somelist[0],somelist[-1])
print('输出打印str5:', str5)

parts = somelist[0], somelist[-1], somelist[1:3]
print('输出parts：', parts)
print(*parts)

str6 = 'first = {0},second = {1}, third = {2}'.format(*parts)
print('输出str6:', str6)





























