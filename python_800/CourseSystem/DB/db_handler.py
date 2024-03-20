"""
用于保存对象与获取对象
"""
from CONF import settings
import os
import pickle


# 保存数据
def save_data(obj):
	# 获取对象的保存文件夹路径,以类名 当做 文件夹的名字
	# obj.__class__获取当前对象所属的类
	# obj.__class__.__name__ 获取类的名字
	class_name = obj.__class__.__name__
	# 1、拼接一个保存对象的文件夹路径
	user_dir_path = os.path.join(
		settings.DB_PATH, class_name
	)
	# 2、	判断文件夹是否存在,不存在则创建
	if not os.path.exists(user_dir_path):
		os.mkdir(user_dir_path)

	# 3、拼接当前用户的pickle文件路径，以 用户名 作为文件名
	user_path = os.path.join(user_dir_path, obj.name)

	# 4、打开文件，保存对象，通过pickle
	with open(user_path, mode='wb') as f:
		pickle.dump(obj, f)


# 获取数据
def select_data(cls, username):
	# 由cls获取类名：cls.__name__
	class_name = cls.__name__
	# 1、拼接一个保存对象的 文件夹 路径
	user_dir_path = os.path.join(
		settings.DB_PATH, class_name
	)
	# 2、	判断文件夹是否存在,不存在则创建
	if not os.path.exists(user_dir_path):
		os.mkdir(user_dir_path)

	# 3、拼接当前用户的pickle文件路径，以 用户名 作为文件名
	user_path = os.path.join(user_dir_path, username)

	# 4、判断文件如果存在，再打开，并返回，若不存在，则代表用户不存在
	if os.path.exists(user_path):
		with open(user_path, mode='rb') as f:
			obj = pickle.load(f)
			return obj
	else:
		return None
