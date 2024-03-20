# pwd = '38$@NoNoN'


# 密码长度得分计算
def get_len_score(pwd):
	if 0 < len(pwd) <= 4:
		return 5
	elif 5 <= len(pwd) <= 7:
		return 10
	elif len(pwd) >= 8:
		return 25
	else:
		return 0


# 根据是否有字母以及字母大小写来得分
def get_alpha_score(pwd):
	# 小写字母数量
	num1 = 0
	# 大写字母数量
	num2 = 0
	for i in pwd:
		if i.islower():
			num1 += 1
		if i.isupper():
			num2 += 1
	# 全是小写或者全是大写
	if (num1 != 0 and num2 == 0) or (num1 == 0 and num2 != 0):
		return 10
	elif num1 != 0 and num2 != 0:
		return 20
	else:
		return 0


# 根据数字来得分
def get_num_score(pwd):
	# 字符串中数字的个数
	n = 0
	for i in pwd:
		if i.isdigit():
			n += 1
	if n == 1:
		return 10
	elif n > 1:
		return 20
	else:
		return 0



# 根据字符来得分
def get_symbol_score(pwd):
	fh = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	n = 0
	for i in pwd:
		if i in fh:
			n += 1
	if n == 1:
		return 10
	elif n > 1:
		return 25
	else:
		return 0


# 奖励得分
def get_win_sore(pwd):
	# 小写字母数量
	a = 0
	# 大写字母数量
	b = 0
	for j in pwd:
		if j.islower():
			a += 1
		if j.isupper():
			b += 1
	# 字母 + 数字
	if ((a != 0 and b == 0) or (a == 0 and b != 0))and get_num_score(pwd):
		return 2
	# 字母 + 数字 + 符号
	if ((a != 0 and b == 0) or (a == 0 and b != 0)) and get_num_score(pwd) and get_symbol_score(pwd):
		return 3
	# 大小写字母 加 数字 加符号
	if (a != 0 and b != 0) and get_num_score(pwd) and get_symbol_score(pwd):
		return 5
	else:
		return 0


while True:
	try:
		pwd = input().strip()
		total_score = get_len_score(pwd) + get_alpha_score(pwd) + get_symbol_score(pwd) + get_num_score(
			pwd) + get_win_sore(pwd)
		print(total_score)
		if total_score >= 90:
			print('VERY_SECURE')
		elif total_score >= 80:
			print('SECURE')
		elif total_score >= 70:
			print('VERY_STRONG')
		elif total_score >= 60:
			print('STRONG')
		elif total_score >= 50:
			print('AVERAGE')
		elif total_score >= 25:
			print('WEAK')
		elif total_score >= 0:
			print('VERY_WEAK')
	except:
		break

# pwd = input().strip()
# pwd = 'Jl)M:+'
# # 密码长度
# def len_score(pwd):
# 	if len(pwd) <= 4:
# 		return 5
# 	elif len(pwd) <= 7:
# 		return 10
# 	else:
# 		return 25
#
# # 字母得分
# def alpha_score(pwd):
# 	# 小写字母数量
# 	n1 = 0
# 	# 大写字母数量
# 	n2 = 0
# 	for i in pwd:
# 		if i.islower():
# 			n1 += 1
# 		if i.isupper():
# 			n2 += 1
# 	# 全是小写字母或者是大写字母
# 	if (n1 != 0 and n2 == 0) or (n1 == 0 and n2 != 0):
# 		return 10
# 	elif n1 != 0 and n2 != 0:
# 		return 20
# 	else:
# 		return 0
#
# def digit_score(pwd):
# 	# 密码中数字数量
# 	n3 = 0
# 	for i in pwd:
# 		if i.isdigit():
# 			n3 += 1
# 	if n3 == 0:
# 		return 0
# 	elif n3 == 1:
# 		return 10
# 	else:
# 		return 20
#
# def symbol_score(pwd):
# 	symbol = '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
# 	# 符号数量
# 	n4 = 0
# 	for i in pwd:
# 		if i in symbol:
# 			n4 += 1
# 	if n4 == 1:
# 		return 10
# 	elif n4 > 1:
# 		return 25
# 	else:
# 		return 0
#
# def win_score(pwd):
# 	# 小写字母
# 	n5 = 0
# 	# 大写字母
# 	n6 = 0
# 	for j in pwd:
# 		if j.islower():
# 			n5 += 1
# 		if j.isupper():
# 			n6 += 1
#
# 	if ((n5 != 0 and n6 == 0) or (n5 == 0 and n6 != 0)) and digit_score(pwd):
# 		return 2
# 	elif ((n5 != 0 and n6 == 0) or (n5 == 0 and n6 != 0)) and digit_score(pwd) and symbol_score(pwd):
# 		return 3
# 	elif (n5 != 0 and n6 != 0) and digit_score(pwd) and symbol_score(pwd):
# 		return 5
# 	else:
# 		return 0
#
# # 总得分
# total_score = len_score(pwd) + alpha_score(pwd) + digit_score(pwd) + symbol_score(pwd) + win_score(pwd)
#
# if total_score >= 90:
# 	print('VERY_SECURE')
# elif total_score >= 80:
# 	print('SECURE')
# elif total_score >= 70:
# 	print('VERY_STRONG')
# elif total_score >= 60:
# 	print('STRONG')
# elif total_score >= 50:
# 	print('AVERAGE')
# elif total_score >= 25:
# 	print('WEAK')
# else:
# 	print('VERY_WEAK')
#
# print(total_score)
















