# 导入两个包
import unittest
import requests


# 新建测试类-》继承unittest.TestCase类
class TestLogin(unittest.TestCase):
	# 以test开头的方法执行之前，首先会被执行，有几个test方法，就会被执行几次
	def setUp(self):
		pass

	# 以test开头的方法执行之后，会被执行，有几个test方法，就会被执行几次
	def tearDown(self):
		pass

	# 登录成功,测试用例方法，必须要以test开头
	def test_login_success(self):
		pass

	# 登录失败，账号不存在，测试用例方法，必须要以test开头
	def test_username_not_exists(self):
		pass

	# 登录失败，密码错误，测试用例方法，必须要以test开头
	def test_password_error(self):
		pass








