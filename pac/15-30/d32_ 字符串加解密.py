# 加密方法
def Encryption(pws):
	res = []
	for v in pws:
		if v.islower():
			if v == 'z':
				res.append('A')
			else:
				if v in lo_arr:
					index = lo_arr.index(v)
					res.append(lo_arr[index + 1].upper())
		elif v.isupper():
			if v == 'Z':
				res.append('a')
			else:
				if v in up_arr:
					index = up_arr.index(v)
					res.append(up_arr[index + 1].lower())
		elif v.isdigit():
			if int(v) == 9:
				res.append('0')
			else:
				res.append(str(int(v) + 1))
		else:
			res.append(v)

	print(''.join(res))


# 解密方法
def Decryption(pws):
	res = []
	for v in pws:
		if v.islower():
			if v == 'a':
				res.append('Z')
			else:
				if v in lo_arr:
					index = lo_arr.index(v)
					res.append(lo_arr[index - 1].upper())
		elif v.isupper():
			if v == 'A':
				res.append('z')
			else:
				if v in up_arr:
					index = up_arr.index(v)
					res.append(up_arr[index - 1].lower())
		elif v.isdigit():
			if int(v) == 0:
				res.append('9')
			else:
				res.append(str(int(v) - 1))
		else:
			res.append(v)

	print(''.join(res))


while True:
	try:
		up_arr = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		lo_arr = list('abcdefghijklmnopqrstuvwxyz')
		s1 = input().strip()
		s2 = input().strip()
		Encryption(s1)
		Decryption(s2)
	except:
		break
