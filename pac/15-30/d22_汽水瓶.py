def max_drink(num):
	# 可兑换的汽水数量
	drink_bottles = num // 3
	# 剩余的空瓶数量
	empty_bottles = num // 3 + num % 3
	if empty_bottles < 2:
		drink_bottles += 0
	elif empty_bottles == 2:
		drink_bottles += 1
	else:
		drink_bottles += max_drink(empty_bottles)

	return drink_bottles


while True:
	try:
		num = int(input().strip())
		if num == 0:
			break
		else:
			print(max_drink(num))
	except:
		break
