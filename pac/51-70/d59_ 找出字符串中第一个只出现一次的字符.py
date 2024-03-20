# while True:
# 	try:
# 		s = input().strip()
# 		num = -1
# 		for i in s:
# 			if s.count(i) == 1:
# 				num = i
# 				break
# 		print(num)
# 	except:
# 		break

while True:
	try:
		s = input().strip()
		d = {}
		for i in s:
			d[i] = d.get(i, 0) + 1
		# 所有出现的字符出现次数均大于1，需要返回 - 1
		if min(d.values()) > 1:
			print('-1')
		else:
			for k, v in d.items():
				if v == 1:
					print(k)
					break
	except:
		break
