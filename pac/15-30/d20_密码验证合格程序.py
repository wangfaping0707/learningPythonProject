def check_pwd(pwd):
	# 校验密码长度
	if len(pwd) <= 8:
		return False

	# 校验密码中包含的字符种类
	counts = [0, 0, 0, 0]
	for i in pwd:
		if i.isupper():
			counts[0] = 1
		elif i.islower():
			counts[1] = 1
		elif i.isdigit():
			counts[2] = 1
		else:
			counts[3] = 1
	if sum(counts) < 3:
		return False
	# 校验密码中 相同子字符串的重复次数
	for j in range(len(pwd) - 2):
		if pwd[j:j + 3] in pwd[j + 3:]:
			return False
	return True


while True:
	try:
		s = input().strip()
		if check_pwd(s):
			print('OK')
		else:
			print('NG')
	except:
		break

