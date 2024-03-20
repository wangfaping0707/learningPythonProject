while True:
	try:
		num1, num2 = map(int, input().strip().split())

		if num1 > num2:
			num1, num2 = num2, num1

		for i in range(num1, num1 * num2 + 1, num1):
			if i % num2 == 0:
				print(i)
				break

	except:
		break
