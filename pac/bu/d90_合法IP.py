while True:
	try:
		ip = input().strip()
		ip_list = ip.split('.')
		if len(ip_list) != 4:
			print('NO')
			break
		for i in ip_list:
			if not i.isdigit() or int(i) > 255 or int(i) < 0 or (i.startswith('0') and len(i) > 1):
				print('NO')
				break
		else:
			print('YES')
	except:
		break
