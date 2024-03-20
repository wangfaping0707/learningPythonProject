# 导入两个包
import unittest
import requests


# 新建测试类-》继承unittest.TestCase类
class TestLogin(unittest.TestCase):
	# 以test开头的方法执行之前，首先会被执行，有几个test方法，就会被执行几次
	def setUp(self):
		print('我在运行中。。。。。。。。。。。。。。。。。。。。')
		# 获取session对象
		self.session = requests.session()
		# 	登录url
		self.url_login = "http://192.168.176.128/index.php?m=Home&c=User&a=do_login"
		# 	验证码url
		self.url_verify = "http://192.168.176.128/index.php?m=Home&c=User&a=verify"

	# 以test开头的方法执行之后，会被执行，有几个test方法，就会被执行几次
	def tearDown(self):
		# 关闭session对象
		self.session.close()

	# 登录成功,测试用例方法，必须要以test开头
	def test_login_success(self):
		# 请求验证码---》获取coookies
		self.session.get(self.url_verify)
		# 请求登录
		data = {
			"username": "13800001111",
			"password": "123456",
			"verify_code": 8888
		}
		r = self.session.post(self.url_login, data=data)
		# 断言
		try:
			self.assertEqual("登陆成功", r.json()['msg'])
		except AssertionError as e:
			print(e)

	# 登录失败，账号不存在，测试用例方法，必须要以test开头
	def test_username_not_exists(self):
		# 请求验证码---》获取coookies
		self.session.get(self.url_verify)
		# 请求登录
		data = {
			"username": "13800001112",
			"password": "123456",
			"verify_code": 8888
		}
		r = self.session.post(self.url_login, data=data)
		# 断言
		try:
			self.assertEqual("账号不存在", r.json()['msg'])
		except AssertionError as e:
			print(e)

	# 登录失败，密码错误，测试用例方法，必须要以test开头
	def test_password_error(self):
		# 请求验证码---》获取coookies
		self.session.get(self.url_verify)
		# 请求登录
		data = {
			"username": "13800001112",
			"password": "1234566",
			"verify_code": 8888
		}
		r = self.session.post(self.url_login, data=data)
		# 断言
		try:
			self.assertEqual("密码错误", r.json()['msg'])
		except AssertionError as e:
			print(e)


if __name__ == '__main__':
	unittest.main()
