while True:
	try:
		s = input().strip()
		s = s.replace('{', '(')
		s = s.replace('}', ')')
		s = s.replace('[', '(')
		s = s.replace(']', ')')
		print(int(eval(s)))
	except:
		break
