import os
# 获取当前工作目录，即python脚本的工作目录
print(os.getcwd())

# 返回当前目录
print(os.curdir)

# 返回当前目录下面包含的文件、子文件夹
print(os.listdir())

print(os.listdir(r'D:\PythonProject\python_800\chapter5'))

print(os.listdir('.'))

# 将文件目录和文件分开
res = os.path.split('/a/b/c/d/f.txt')
res1 = os.path.split('D:\\a\\b\\c\\d\\f\\e.txt')
print(res)
print(res1)

# 判断是否是一个文件
print(os.path.isfile(r'D:\PythonProject\python_800\chapter5\d53_time时间模块.py'))

# 判断是否是一个目录
print(os.path.isdir(r'D:\PythonProject\python_800\chapter5'))

# 获取当前文件所在路径
print(__file__)

# 获取当前文件所在路径的目录
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))







