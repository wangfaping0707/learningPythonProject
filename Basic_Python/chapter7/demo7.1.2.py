# 与对象属性相关联的函数称为方法

print('absbabaadad'.count('a'))
print(['a', 'd', 'r', 'w', 'a', 's'].count('a'))

from random import *

# Python中的choice()函数: choice() 方法返回一个列表，元组或字符串的随机项。
# 以下是 choice() 方法的语法:
# import random
# random.choice( seq  )
# 注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
# 参数
# seq -- 可以是一个列表，元组或字符串。
# 返回值
# 返回随机项。
# 实例
# 以下展示了使用 choice() 方法的实例：
# import random
#
# print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
# print "choice('A String') : ", random.choice('A String')
# 以上实例运行后输出结果为：
# choice([1, 2, 3, 5, 9]) :  2
# choice('A String') :  n

x = choice(["Hello World",[1,2,'e','e',4]])
print(x)
