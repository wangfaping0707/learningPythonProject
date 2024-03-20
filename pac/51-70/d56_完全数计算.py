# 计算一个数字的真因子

def perfect_num(n):
	num_list = []
	for i in range(1, n):
		if n % i == 0:
			num_list.append(i)
	print(f'num_list:{num_list}')
	return num_list


while True:
	try:
		num = int(input().strip())
		res = []
		for j in range(1, num + 1):
			total = perfect_num(j)
			if sum(total) == j:
				res.append(j)
		print(f'res:{res}')
		print(len(res))
	except Exception as e:
		raise e

# num = 28
#
#
# def cal_num(num):
# 	res = []
# 	for i in range(1, num):
# 		if num % i == 0:
# 			res.append(i)
# 	if sum(res) == num:
# 		return True
#
# n = 1000
# count = 0
# r = []
# for i in range(1, n + 1):
# 	if cal_num(i):
# 		count += 1
# 		r.append(i)
# print(count)
# print(r)
