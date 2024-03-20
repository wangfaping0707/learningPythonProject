import sys
import os
# 返回模块的搜索路径，初始化时使用的PYTHONPATH环境变量的值
print(sys.path)


# 获取当前文件所在路径
print(__file__)

# 获取当前文件所在路径的目录
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
