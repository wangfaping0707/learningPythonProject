while True:
	try:
		s = input().strip()
		s = s.replace('{', '(').replace('[', '(').replace(']', ')').replace('}', ')')
		print(eval(s))
	except:
		break