"""
程序的执行入口
"""
import sys
import os

print('start文件的路径:', __file__)
print('start文件所在目录:', os.path.dirname(__file__))

# print(sys.path)
# 添加解释器的环境变量
sys.path.append(
	os.path.dirname(__file__)
)

from core import src

# 开始执行项目函数
if __name__ == '__main__':
	src.run()
