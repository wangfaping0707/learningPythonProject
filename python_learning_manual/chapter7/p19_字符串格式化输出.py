import sys

print('%s = %s' % ('spam', 42))

print('{0} = {1}'.format('spam', 42))


print('{} = {}'.format('spam', 42))

print('%s,%s and %s' % (3.14, 42, [3, 2, 1]))

str1 ='My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform)
print('输出str1:', str1)

str2 = 'My %(kind)s runs %(platform)s'%{'kind' : 'laptop', 'platform' : sys.platform}
print('输出str2:', str2)

