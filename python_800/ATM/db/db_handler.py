"""
数据处理层
		专门用来除里用户数据
"""
import os
import json
from conf import settings


# 查看数据
def select(username):
	# 接收接口层传递过来的username用户名，拼接用户json文件路径
	user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
	# 校验用户的json文件是否存在，如果存在就打开文件，读取信息，并将信息返回给接口层
	if os.path.exists(user_path):
		with open(user_path, mode='r', encoding='utf-8') as f:
			user_dic = json.load(f)
			return user_dic


# 接收接口层传递过来的数据，保存到数据库
def save(user_dic):
	# 将每个用户的数据字典信息独立保存为一个文件，每个用户的数据信息相互隔离开来，方便后续取，所以用 用户名作为文件名称，将用户的所有数据都保存在db下面
	# 拼接用户的json文件路径
	username = user_dic.get('username')
	user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
	with open(user_path, mode='wt', encoding='utf-8') as f:
		json.dump(user_dic, f, ensure_ascii=False)
