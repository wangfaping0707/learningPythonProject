
# 获取最大增长子序列
def get_max_up_sub_arr(count, arr):
	up_arr = [1 for x in range(count)]  # 等同于[1] *len(arr)
	print(f'up_arr:{up_arr}')
	for i in range(count):
		for j in range(i):
			if arr[j] < arr[i]:
				up_arr[i] = max(up_arr[i], up_arr[j] + 1)
	return up_arr


while True:
	try:
		count = int(input())
		arr = list(map(int, input().split(' ')))
		left_up_arr = get_max_up_sub_arr(count, arr)
		right_up_arr = get_max_up_sub_arr(count, arr[::-1])[::-1]
		print(count - max(i + j - 1 for i, j in zip(left_up_arr, right_up_arr)))
	except EOFError:
		break

nums = [1, 5, 2, 4, 3]
print(get_max_up_sub_arr(5, nums))


