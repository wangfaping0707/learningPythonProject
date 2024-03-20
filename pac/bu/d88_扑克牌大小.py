dic = {
	'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
	'9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12,
	'2': 13, 'joker': 14, 'JOKER': 15
}


def isboom(lst):
	if len(lst) == 4 and len(set(lst)) == 1:
		return True
	return False


while True:
	try:
		s1, s2 = input().split('-')
		print(f's1:{s1}')
		print(f's2:{s2}')
		lst1, lst2 = s1.split(), s2.split()
		print(f'lst1:{lst1}')
		print(f'lst2:{lst2}')
		L1, L2 = len(lst1), len(lst2)
		if L1 == L2:
			if dic[lst1[0]] > dic[lst2[0]]:
				print(s1)
			else:
				print('----')
				print(s2)
		else:
			if 'joker JOKER' in (s1, s2):
				print('joker JOKER')
			elif isboom(lst1):
				print(s1)
			elif isboom(lst2):
				print(s2)
			else:
				print('ERROR')
	except:
		break



# # s = '4 4 4 4-joker JOKER'
# poker_dic = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13,
#  'joker': 14, 'JOKER': 15}
#
# # 判断牌是不是炸弹
# def is_boom(lst):
# 	if len(lst) == 4 and len(set(lst)) == 1:
# 		return True
# 	else:
# 		return False
#
# p1, p2 = input().strip().split('-')
# # p1, p2 = s.strip().split('-')
#
# p1_list = p1.split()
# p2_list = p2.split()
# # print(p1_list)
# # print(p2_list)
#
# if len(p1_list) == len(p2_list):
# 	if poker_dic[p1_list[0]] > poker_dic[p2_list[0]]:
# 		print(p1)
# 	else:
# 		print(p2)
# else:
# 	if 'joker JOKER' in (p1, p2):
# 		print('joker JOKER')
# 	elif is_boom(p1_list):
# 		print(p1)
# 	elif is_boom(p2_list):
# 		print(p2)
# 	else:
# 		print('ERROR')


















