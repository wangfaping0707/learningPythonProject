while True:
	try:
		import datetime

		y, m, d = map(int, input().strip().split())

		dt = datetime.datetime(y, m, d)
		print(dt.strftime('%j').lstrip('0'))
	except:
		break
