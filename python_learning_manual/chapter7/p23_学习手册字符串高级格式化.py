import sys

str = '{0:10} = {1:10}'.format('spam', 123.4567)
print('str:', str)

str1 = '{0:>10} = {1:<10}'.format('spam', 123.4567)
print('str1:', str1)

str2 = '{0.platform:<10} = {1[kind]:>10}'.format(sys, dict(kind='laptop'))
print('str2:', str2)

print('--------------------------------------------------------------------')
"""
格式话方法format的调用中，浮点数支持与%表达式中相同的类型代码和格式化声明。例如：下面的{2：g}表示，第三个数据根据“g”浮点数进行默认格式化，
{1:.2f}指定了带有2个小数位的'f'浮点数格式，{2:06.3f}添加了一个6字符宽度的字段，带有3个小数位，并且在左边补充0：
"""
str3 = '{0:e},{1:.3e},{2:g}'.format(314.159, 31415.9, 3.14159)
print('str3:', str3)
print('***************************************************************************')

str4 = '{0:f},{1:.2f},{2:06.2f}'.format(3.14159, 3.14159, 3.14159)
print('str4:', str4)

str5 = '{0:.2f}'.format(1/3.0)
print('str5:', str5)
str6 = '%.2f'%(1/3.0)
print('str6:', str6)

print('————————————————————————————————————————————————————————————————————————————————————')
str7 = '{1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind':'laptop'})
print('str7:', str7)

str8 = '%(kind)-8s runs %(plat)8s'%dict(kind = 'laptop', plat = sys.platform)
print('str8:', str8)

# 千位分隔符
num = '{0:,d}'.format(999999999999)
print('num:', num)

num1 = '{0:,.2f}'.format(296999.2579)
print('num1:', num1)

s = 's,pa,m'
# 取出字符串s中的pa
s1 = s[2:4]
print('第一种方式取出目标字符：', s1)

s2 = s.split(',')
print('s2:', s2)

print('第二种方式取出目标字符：', s2[1])

s3 = 'a\nb\x1f\000d'
print(len(s3))

print(s3)






























