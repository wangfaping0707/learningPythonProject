"""
银行相关业务的接口
"""
from db import db_handler


# 提现接口(手续费为5%)

def withdraw_interface(username, money):
	# 先获取用户字典信息
	user_dic = db_handler.select(username)
	# 获取用户账户的金额,并同时转换为数字
	balance = int(user_dic.get('balance'))
	# 计算 本金 + 手续费 的金额，用于后续和账户的余额进行比对
	money2 = int(money) * 1.05
	if balance >= money2:
		# 修改账户中的余额
		balance = balance - money2
		user_dic['balance'] = balance
		# 记录银行流水
		flow = f'用户{username}已成功提现{money}元，需要支付手续费为{money2 - float(money)}元'
		user_dic['flow'].append(flow)
		# 在保存数据或更新数据
		db_handler.save(user_dic)
		return True, flow

	return False, f'账户余额不够，请核对之后重新输入！！！'

	# 1、获取用户的还款金额
	# 2、给用户的金额做加钱操作


# 还款接口
def repay_interface(username, money):
	# 获取用户信息字典
	user_dic = db_handler.select(username)
	# 直接给用户账户进行价钱操作
	user_dic['balance'] += money
	# 记录银行流水
	flow = f'用户：{username} 充值：{money} 成功'
	user_dic['flow'].append(flow)
	# 调用数据处理层，将用户余额更新后的数据重新保存
	db_handler.save(user_dic)

	return True, flow


# 转账接口
def transfer_interface(login_user, to_user, money):
	# 	获取当前用户信息字典
	login_user_dic = db_handler.select(login_user)
# 	获取 目标用户 信息字典
	to_user_dic = db_handler.select(login_user)
	# 判断目标用户是否存在
	if not to_user_dic:
		return False, f'{to_user_dic} 目标用户不存在'
	# 若转账目标用户存在，判断当前用户的账户可用金额是否大于转账金额
	if login_user_dic['balance'] >= money:
		# 给当前用户做减钱操作
		login_user_dic['balance'] -= money
		# 给转账目标用户做加钱操作
		to_user_dic['balance'] += money
		# 记录当前用户的流水
		login_user_flow = f'用户{login_user} 给 {to_user} 转账{money}元 成功'
		login_user_dic['flow'].append(login_user_flow)
		# 记录目标用户的流水
		to_user_flow = f'用户{to_user} 接收到 用户{login_user} 转账{money}元 成功'
		to_user_dic['flow'].append(to_user_flow)
		# 将两个账户的金额变动后的信息重新存入数据库
		db_handler.save(login_user_dic)
		db_handler.save(to_user_dic)
		return True, login_user_flow
	else:
		return False, '当前用户的 账户可用余额不足'


# 查看流水接口
def check_flow_interface(login_user):
	user_dic = db_handler.select(login_user)
	return user_dic.get('flow')