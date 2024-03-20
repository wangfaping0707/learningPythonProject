while True:
	try:
		n = int(input().strip())
		nums = list(map(int, input().strip().split()))
		order = input().strip()
		if order == '0':
			nums = sorted(nums)
		else:
			nums = sorted(nums, reverse=True)
		print(' '.join(map(str, nums)))

	except:
		break
