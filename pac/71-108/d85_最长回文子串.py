"""
'ABBBACJ'
 i
     j：要基于i的位置 从左往右遍历
"""

# pas = 'ABBBACJ'

while True:
	try:
		# str1 = 'cdabbacc'
		str1 = input().strip()
		res = []
		for i in range(len(str1)):
			for j in range(i, len(str1)):
				if str1[i] == str1[j] and str1[i:j + 1] == str1[i:j + 1][::-1]:
					res.append(len(str1[i:j + 1]))

		print(max(res))
	except:
		break
