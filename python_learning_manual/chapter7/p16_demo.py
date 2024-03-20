exclamation = 'Ni'

str = 'The knights who say %s!' % exclamation
print('输出打印：', str)

str1 = '%d %s %f you ' % (1, 'spam', 4.0)
print('输出打印str1：', str1)

str2 = '%s--%s--%s' % (42, 3.14159, [1, 2, 3])
print('输出打印str2：', str2)

print('--------------------------分割线---------------------------------------')
x = 1.23456789
print('%e|%f|%g' % (x, x, x))


format = "Hello,%s. %s enough for ya?"
values = ('world', 'Hot')
print(format%values)
"""
上述格式字符串中%s称为转换说明符，指出了要将值插入什么地方，s意味将值视为字符串进行格式设置。如果指定的值不是字符串，将使用str将其转换为字符串。
其它说明符将导致其他形式的转换。例如，%.3f将值设置为包含3位小数的浮点数。

"""






























