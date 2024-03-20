"""
'ABBBACJ'
 i
     j：要基于i的位置 从左往右遍历
"""

# pas = 'ABBBACJ'

while True:
	try:
		pas = input().strip()
		res = []
		for i in range(len(pas)):
			for j in range(i, len(pas)):
				# 首先判断子字符串的首尾字母是否相等，如果相等在判断首尾中间的字母是否对称，只要是对称，正向和反向是相等的
				if pas[i] == pas[j] and pas[i:j + 1] == pas[i:j + 1][::-1]:
					print(pas[i:j + 1])
					res.append(len(pas[i:j + 1]))
		print(res)
		print(max(res))
	except:
		break
