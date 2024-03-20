"""
186 186 150 200 160 130 197 200   heigtht
1   1   1    1   1   1   1   1    up_arr
        i
j
"""


def get_max_queue(nums, heights):
	up_arr = [1] * len(heights)
	for i in range(len(heights)):
		for j in range(i):
			if heights[j] < heights[i]:
				up_arr[i] = max(up_arr[i], up_arr[j] + 1)
	return up_arr


while True:
		nums = int(input())
		heights = list(map(int, input().strip().split()))
		print(f'heights:{heights}')
		get_left_arr = get_max_queue(nums, heights)
		print(f'get_left_arr:{get_left_arr}')
		get_right_arr = get_max_queue(nums, heights[::-1])[::-1]
		print(f'get_right_arr:{get_right_arr}')
		re = [i + j - 1 for i, j in zip(get_left_arr, get_right_arr)]
		print(re)
		num = nums - max(re)
		print(f'要走的人：{num}')
