while True:
	try:
		# 总钱数
		total = int(input().strip())
		# 全部买公鸡，最多 20只，全部买母鸡，最多34， 全部买小鸡 最多100只
		for x in range(21):
			for y in range(34):
				for z in range(101):
					if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
						print(x, y, z)
	except:
		break
