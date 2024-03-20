while True:
	try:
		strs = input().strip()
		for i in strs:
			if not i.isalpha():
				strs = strs.replace(i, ' ')
		b = list(reversed(strs.strip().split(' ')))
		print(' '.join(b))
	except:
		break

# b = list(reversed(strs.strip().split(' ')))
# print(' '.join(b))
# strs = '$bo*y gi!r#l'.strip()
# print(strs)
