# A Famous Saying: Much Ado About Nothing (2012/8).
# A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

while True:
	try:
		raw_s = input().strip()
		# 记录原字符串的顺序，以及非 字母的字符
		res = [0] * len(raw_s)  # 使用0作为占位符
		# 定义一个记录字母字符且排好序的列表
		temp = []
		for i, v in enumerate(raw_s):
			if v.isalpha():
				temp.append(v)
			else:
				res[i] = v

		temp = sorted(temp, key=str.lower)
		# print(f'temp的值：{temp}')
		for j, v in enumerate(res):
			if not v:
				res[j] = temp[0]
				temp.pop(0)
		print(''.join(res))
	except Exception as e:
		raise e
