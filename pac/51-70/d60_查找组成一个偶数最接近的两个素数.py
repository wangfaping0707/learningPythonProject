# 判定一个数是不是素数(质数)
def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


while True:
	try:
		num = int(input().strip())
		res = []
		for j in range(2, num // 2 + 1):
			if is_prime(j) and is_prime(num - j):
				a = j
				b = num - j
				res.append((a, b))
		# print(res)

		h = []
		for i in res:
			h.append(i[1] - i[0])
		# 找出 差值最小的 素数对
		min_v = min(h)
		# 找出差值最小的素数对
		s = h.index(min_v)
		for i in res[s]:
			print(i)
	except:
		break


#
# n = 20
#
#
# def cal(n):
# 	if n <= 1:
# 		return False
# 	else:
# 		for i in range(2, int(n ** 0.5) + 1):
# 			if n % i == 0:
# 				return False
# 		return True
#
#
# res = []
# for i in range(n // 2 + 1):
# 	r1 = i
# 	r2 = n - i
# 	if cal(r1) and cal(r2):
# 		res.append((r1, r2))
# h = []
# for i in res:
# 	val = i[1] - i[0]
# 	h.append(val)
#
# for j in range(len(h)):
# 	if h[j] == min(h):
# 		print(res[j])
# 		break
#























