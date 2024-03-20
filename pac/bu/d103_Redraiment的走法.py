while True:
	try:
		n = int(input())
		num = list(map(int, input().strip().split()))
		arr = [1] * n

		for i in range(len(num)):
			for j in range(i):
				if num[j] < num[i]:
					arr[i] = max(arr[j] + 1, arr[i])

		print(max(arr))
	except:
		break
