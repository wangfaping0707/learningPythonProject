while True:
	try:
		n = int(input().strip())

		res = []
		for i in range(n + 1):
			num = i ** 2
			lens = len(str(i))
			if str(num)[-lens:] == str(i):
				res.append(i)

		print(len(res))
	except:
		break

print('=====================================')
# while True:
#
# 	try:
# 		n = int(input())
# 		count = 0
# 		for i in range(n + 1):
# 			res = i ** 2
# 			if str(res).endswith(str(i)):
# 				count += 1
# 		print(count)
# 	except:
# 		break