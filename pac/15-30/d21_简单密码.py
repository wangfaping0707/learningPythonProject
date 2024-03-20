u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s_n = list(input().strip())

for i in range(len(s_n)):
	if s_n[i].islower():
		if s_n[i] in 'abc':
			s_n[i] = '2'
		elif s_n[i] in 'def':
			s_n[i] = '3'
		elif s_n[i] in 'ghi':
			s_n[i] = '4'
		elif s_n[i] in 'jkl':
			s_n[i] = '5'
		elif s_n[i] in 'mno':
			s_n[i] = '6'
		elif s_n[i] in 'pqrs':
			s_n[i] = '7'
		elif s_n[i] in 'tuv':
			s_n[i] = '8'
		elif s_n[i] in 'wxyz':
			s_n[i] = '9'
	elif s_n[i].isupper():
		if s_n[i] == 'Z':
			s_n[i] = 'a'
		else:
			index = u.index(s_n[i])
			s_n[i] = u[index + 1].lower()
	elif s_n[i].isdigit():
		s_n[i] = str(s_n[i])

print(''.join(s_n))

print('=========================================')
while True:
	try:
		s = input()
		res = []
		for i in s:
			if i.isdigit():
				res.append(i)
			elif i.isupper() and i != 'Z':
				res.append(chr(ord(i.lower()) + 1))
			elif i == 'Z':
				res.append('a')
			else:
				if i in 'abc':
					res.append('2')
				elif i in 'def':
					res.append('3')
				elif i in 'ghi':
					res.append('4')
				elif i in 'jkl':
					res.append('5')
				elif i in 'mno':
					res.append('6')
				elif i in 'pqrs':
					res.append('7')
				elif i in 'tuv':
					res.append('8')
				else:
					res.append('9')
		print(''.join(res))
	except:
		break
