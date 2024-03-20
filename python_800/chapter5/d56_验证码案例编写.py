# 需求：获得一个6位数的验证码，验证码由大写字母和数字混合而成
import random

print(ord('A'))
print(ord('Z'))
# 先定义一个空字符串
res = ''
for i in range(0, 6):
	# 获取一位随机整数，因为是字符，所以必须将获得字符串转换为数字
	s1 = str(random.randint(0, 9))
	# 获取26位大写字母中的随机一位
	s2 = chr(random.randint(65, 90))
	# 随机获取 s1 s2中的一位数
	ran = random.choice([s1, s2])
	res += ran

print('最终获取到验证码：', res)
