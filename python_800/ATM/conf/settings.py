"""
存放配置信息
"""
import os

# print('settings文件的所在路径', __file__)

# 获取项目跟目录的路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# print('BASE_PATH:', BASE_PATH)

# 获取 user_data文件夹目录路径，需要进行路径拼接
USER_DATA_PATH = os.path.join(BASE_PATH, 'db', 'user_data')

# print('USER_DATA_PATH路径:', USER_DATA_PATH)
