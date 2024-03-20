while True:
	try:
		n = int(input().strip())
		arr1 = list(map(int, input().strip().split()))
		m = int(input().strip())
		arr2 = list(map(int, input().strip().split()))
		L = sorted(set(arr1 + arr2))
		L = list(map(str, L))
		print(''.join(L))

	except:
		break
