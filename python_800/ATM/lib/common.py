"""
存放公共方法
"""
# 编写一个加密的方法，处于安全考虑，可以给用户输入的密码进行加密
import hashlib
from core import src

# 编码：将人类可识别的字符转换为机器可识别的字节码 / 字节序列
# 解码：编码的反向过程叫解码

# 对用户输入的明文密码进行加密操作
def get_pwd_md5(password):
	md5_obj = hashlib.md5()
	md5_obj.update(password.encode('utf-8'))
	salt = '一二三四五，egon上山打老鼠'
	md5_obj.update(salt.encode('utf-8'))
	# 获取加密之后的结果
	return md5_obj.hexdigest()


# 登录认证装饰器

def login_auth(func):
	def inner(*args, **kwargs):
		if src.login_user:
			res = func(*args, **kwargs)
			return res
		else:
			print('使用功能之前，需要登陆验证！！！')
			src.login()
	return inner