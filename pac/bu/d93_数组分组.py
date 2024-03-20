# 较值函数
def cal_add(sm3, sm5, other):
	if len(other) == 0:
		if sm3 == sm5:
			return True
		else:
			return False
	else:
		return cal_add(sm3, sm5 + other[0], other[1:]) or cal_add(sm3 + other[0], sm5, other[1:])


while True:
	try:
		# 数据个数
		n = int(input().strip())
		# 数据行数
		nums = list(map(int, input().strip().split()))
		# 将num数据进行分类
		L3 = []
		L5 = []
		other = []
		for i in nums:
			if i % 3 == 0:
				L3.append(i)
			elif i % 5 == 0:
				L5.append(i)
			else:
				other.append(i)
		# print(L3, L5, other)
		sm3 = sum(L3)
		sm5 = sum(L5)
		res = cal_add(sm3, sm5, other)
		if res:
			print('true')
		else:
			print('false')
	except:
		break

# 5
# 3 8 8 5 14