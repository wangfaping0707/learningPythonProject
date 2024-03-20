def cal_method(a, b, c, d):
	card_pool = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
	             'A': 1}
	# 传入的数转换为整数
	x, y, z, v = card_pool[a], card_pool[b], card_pool[c], card_pool[d]
	# 运算符列表
	symbol = ['+', '-', '*', '/']
	for i in symbol:
		for j in symbol:
			for k in symbol:
				res = eval('((' + 'x' + i + 'y'+ ')' + j + 'z'+ ')' + k + 'v')
				if res == 24:
					return a + i + b + j + c + k + d
	else:
		return False

from itertools import permutations
while True:
	try:
		card_list = input().strip().split()
		if 'joker' in card_list or 'JOKER' in card_list:
			print('ERROR')
		else:
			card_choice =  permutations(card_list)
			# 存储函数执行结果
			temp = []
			for s in card_choice:
				a, b, c, d = s
				res = cal_method(a,b,c,d)
				if res != False:
					temp.append(res)
			if len(temp) > 0:
				print(temp[0])
			else:
				print('NONE')
	except:
		break









# K-A*4/2
# eval('((' + 'x' + i + 'y' + ')' + j + 'z' + ')' + k + 'm')

# print(cal_method('K', 'A','4', '2'))