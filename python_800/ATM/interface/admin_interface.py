from db import db_handler


# 定义修改额度接口
def change_balance_interface(username, money):
	user_dic = db_handler.select(username)
	# 判断获取的用户信息字典是否存在
	if user_dic:
		# 修改用户的额度
		user_dic['balance'] = int(money)

		# 将变更后的用户信息字典存入到数据库中
		db_handler.save(user_dic)
		return True, f'用户{username} 的额度修改成功，修改后的额度为 {money}'
	return False, f'修改额度的用户{username} 不存在'


# 定义冻结用户的接口
def lock_user_interface(username):
	user_dic = db_handler.select(username)
	# 判断用户是否存在
	if user_dic:
		user_dic['locked'] = True
		db_handler.save(user_dic)
		return True, f'用户{username}冻结成功！'
	return False, f'要冻结的用户{username}不存在！'
