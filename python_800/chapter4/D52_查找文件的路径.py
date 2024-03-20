import sys

# sys模块是与python解释器交互的一个接口。sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分
# 查看已经加载在内存中的模块
print(sys.modules)

# sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
# sys.path是python的搜索模块的路径集，是一个list
# 可以在python 环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后自己添加的路径就会自动消失了！
print('添加之前的模块路径集：', sys.path)

sys.path.append(r'D:\PythonProject\python_800\chapter4\vars\varles.py')

print('添加之后的模块路径集：', sys.path)
import varles

print(varles.name)
print(varles.age)

# from varles import *
# print(name)
# print(age)
