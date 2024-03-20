import re

while True:
	try:
		# s = 'a8a72a6a5yy98y65ee1r2'
		s = input().strip()
		lists = re.findall(r'\d+', s)
		lens = [len(i) for i in lists]
		max_len = max(lens)
		res = ''
		for j in lists:
			if len(j) == max_len:
				res += j
		print(f'{res},{max_len}')
	except:
		break


# s = 'a8a72a6a5yy98y65ee1r2'
#
# new_s = ''
#
# for i in s:
# 	if not i.isdigit():
# 		new_s += ' '
# 	else:
# 		new_s += i
#
# lst = new_s.split()
# res = []
# for i in lst:
# 	res.append(len(i))
#
# max_n = max(res)
# result = ''
#
# for i in lst:
# 	if len(i) == max_n:
# 		result += i
#
# print(f'{result},{max_n}')


















