# a = 'Jkdi234klowe90a3'

while True:
	try:
		a = list(input())
		b = []
		for i in range(len(a)):
			if (a[i].isdigit()):
				b.append('$' + a[i] + '$')
			else:
				b.append(a[i])
		str_b = ''.join(b)
		# print(b)
		# print(str_b)
		print(str_b.replace('$$', '').replace('$', '*'))
	except:
		break


# s = 'Jkdi234klowe90a3'
# s= input()
# new_s = ''
# for i in s:
# 	if i.isdigit():
# 		new_s += '$' + i +'$'
# 	else:
# 		new_s += i
#
# print(new_s.replace('$$', '').replace('$', '*'))












