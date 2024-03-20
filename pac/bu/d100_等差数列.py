while True:
	try:
		n = int(input().strip())
		res = [0] * n
		for i in range(n):
			if i == 0:
				res[0] = 2
			else:
				res[i] = res[i - 1] + 3

		print(sum(res))

	except Exception as e:
		raise e

# # 第二种解法：
# n = int(input().strip())
#
# start = 2
# step = 3
# res = []
# for i in range(n):
# 	end = start + step * i
# 	res.append(end)
#
# print(res)
# print(sum(res))
