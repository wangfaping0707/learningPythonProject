"""
6 cab ad abcd cba abc bca abc 1
3
bca
说明：
abc的兄弟单词有cab cba bca，所以输出3
经字典序排列后，变为bca cab cba，所以第1个字典序兄弟单词为bca
"""

while True:
	try:
		# 将输入的字符串切割成列表
		data = input().strip().split()
		# 获取输入待比较的单词数
		num = data[0]
		# 获取 待校验 的单词
		data1 = data[1:-2]
		# 获取用于 校验的单词
		word = data[-2]
		# 获取用于输出 校验通过且排序过的第几个单词
		n = data[-1]
		# 存储校验通过的兄弟的单词
		res = []
		for i in data1:
			if i == word:
				continue
			elif sorted(i) == sorted(word):
				res.append(i)
		# 对提取的列表进行排序
		res.sort()
		print(len(res))
		print(res[int(n) - 1])
	except Exception as e:
		raise e
