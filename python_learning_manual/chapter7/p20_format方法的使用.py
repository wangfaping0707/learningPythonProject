"""
编写新代码时，应选择使用字符串方法format，它融合并强化早期方法的优点，使用这种方法时，每个替换字段都用花括号括起，其中可能包含名称，还可能包含有关如何对相应的值进行
转换和格式设置的信息
"""
from math import pi
str = "{},{} and {}".format('first', 'second', 'third')
str1 = '{0},{1} and {2}'.format('first', 'second', 'third')
print('同时输出打印str 和 str1：', str, str1)

str2 = '这个{2}的世界，我{4}和{0}{1}{3}一直走下去？'.format('陈','其','美好','乐','想')
print('str2：', str2)

print(pi)
str3 = '{name} is approximately {value:.2f}.'.format(value=pi,name = "兀")
print("str3:", str3)

"""
关键字参数的排列顺序无关紧要，在这里，我还指定了格式说明符.2f，并使用冒号将其与字段名隔开。它意味着要使用包含2位小数的浮点数格式。如果
没有指定.2f，结果将如下：
"""
str4 = '{name} is approximately {value}.'.format(value=pi,name = "兀")
print("str4:", str4)


# 顺序参数和关键字参数混合使用
str5 = "{foo} {} {bar} {}".format(3,4,foo='abc',bar='世界')
print('str5:',str5)

fullname = ['Alfred','Smoketoomuch']
str6 = 'Mr {name[1]}'.format(name = fullname)
print('str6:', str6)

num = 'The number is {num}'.format(num = 42)
print('输出num：',num)

num1 = 'The number is {num:.4f}'.format(num = 42)
print('输出num1：',num1)

# f前面不指定数字。默认为6
num3 = 'The number is {num:f}'.format(num = 42)
print('输出num3：',num3)

# 你也可以将其作为二进制数处理
num4 = 'The number is {num:b}'.format(num = 42)
print('输出num4：',num4)

# 将整数解读为unicode码点
num5 = 'The number is {num:c}'.format(num = 42)
print('输出num5：',num5)

# e 使用科学表示法来表示小数（用e表示指数）  4.2 * 10
num6 = 'The number is {num:e}'.format(num = 42)
print('输出num6：',num6)
num7 = 'The number is {num:e}'.format(num = 42000000)
print('输出num7：',num7)
print('------------------------------------------------------------------------------------')
num8 = 'The number is {num:E}'.format(num = 42000000)
print('输出num8：',num8)
# 将数表示为百分比值(乘以100，按说明符f设置格式，再在后面加上%)
num9 = 'The number is {num1:%}'.format(num1 = 25)
print('输出num9：',num9)




























