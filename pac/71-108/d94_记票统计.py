while True:
	try:
		# 候选人的人数n
		n = int(input().strip())
		# 候选人的名字
		hxr_list = input().strip().split()
		# 投票人的人数
		num = int(input().strip())
		# 投票池
		res = input().strip().split()
		# 存储候选人得票数
		d = {}
		for i in hxr_list:
			d[i] = d.get(i, 0)
		# 不合法得票数
		invalid_list = []

		for j in res:
			if j in hxr_list:
				d[j] = d.get(j, 0) + 1
			else:
				invalid_list.append(i)

		for k, v in d.items():
			print(f'{k} : {v}')

		print(f'Invalid : {len(invalid_list)}')

	except:
		break



# # 候选人数
# n = int(input().strip())
# # 候选人名字
# names = input().strip().split()
# # 投票人的人数
# vote_num = int(input().strip())
# # 投票
# vote_ticket = input().strip().split()
#
# # 候选人字典
# d = {}
# for j in names:
# 	d[j] = 0
# d['Invalid'] = 0
# for i in vote_ticket:
# 	if i in names:
# 		d[i] = d.get(i, 0) + 1
# 	else:
# 		d['Invalid'] = d.get('Invalid', 0) + 1
#
# for k,v in d.items():
# 	print(f'{k} : {v}')