"""
逻辑接口层
		用户接口
"""
import json
from conf import settings
import os
from db import db_handler
from lib import common


# 注册接口：接收 视图层 用户输入的数据，利用逻辑将用户输入的数据组织成 用户信息字典，方便后续的存和取
def register_interface(username, password, balance=15000):
	# 接收视图层用户输入的username,进行判断数据是否已存在，所以需要调用数据层的查看数据接口，有数据返回结果，无数据返回None
	user_dic = db_handler.select(username)
	# 如果输入的用户已存在，需要告知用户重新输入
	if user_dic:
		return False, '用户名已存在！'

	# 对用户输入的明文密码进行加密
	password = common.get_pwd_md5(password)

	# 如果输入的用户不存在，需要组织用户数据字典，然后调用数据层接口，将组织好的数据存入数据库
	user_dic = {
		'username': username,
		'password': password,
		'balance': balance,
		'flow': [],
		'shop_car': {},
		'locked': False
	}
	# 调用数据处理层的接口，将组织好的用户信息保存到数据库
	db_handler.save(user_dic)
	return True, f'{username} 注册成功！'


def login_interface(username, password):
	# 将视图层传入的用户名和密码，传给数据层的查询接口，以验证当前用户是否存在,select接口会返回用户字典，user_dic或者None
	user_dic = db_handler.select(username)
	# 若有冻结账户，需要判断用户是否被锁定
	if user_dic.get('locked'):
		return False, '当前用户已被锁定'

	if user_dic:
		# 给用户输入的密码进行一次加密
		password = common.get_pwd_md5(password)
		# 判断用户输入的密码和数据库中存储的密码是否相等
		if password == user_dic.get('password'):
			return True, f'用户{username}登录成功，欧耶！！！'
		else:
			return False, f'用户{username}的密码不正确，请核对之后重新输入！！！'
	else:
		return False, f'用户{username}不存在，请核对用户名是否填写错误。'


# 查看余额接口
def check_bal_interface(username):
	# 逻辑接口层调用数据层的数据查询接口，返回用户数据字典
	user_dic = db_handler.select(username)
	return user_dic['balance']
