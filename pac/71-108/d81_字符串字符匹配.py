while True:
	try:
		s1 = input().strip()
		s2 = input().strip()

		# s1 = 'bc'
		# s2 = 'abc'

		res = []
		for i in s1:
			if i in s2:
				res.append('true')
			else:
				res.append('false')

		if 'false' in res:
			print('false')
		else:
			print('true')

	except:
		break



# s1 = 'rbc'
# s2 = 'abc'
#
# for i in s1:
# 	if i not in s2:
# 		print('false')
# 		break
# else:
# 	print('true')

