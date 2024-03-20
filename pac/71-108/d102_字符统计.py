while True:
	try:
		s = input().strip()
		d = {}
		for i in s:
			d[i] = d.get(i, 0) + 1

		d = dict(sorted(sorted(d.items(), key=lambda item: item[0]), key=lambda i: i[1], reverse=True))

		d_keys = d.keys()

		print(''.join(d_keys))

	except:
		break
