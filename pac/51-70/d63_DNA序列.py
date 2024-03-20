"""
方法一：暴力截取子串并计数
实现思路
我们直接用python切片的方式，遍历给出的字符串来获得一个个目标子串
然后对目标字串进行G和C的计数
如果G和C的数量占比高，则更新可能的输出结果
直到遍历结束为止，输出第一个G和C含量最高的子串
"""



def cal_sub_str(s, sub_len):
	if sub_len >= len(s):
		print(s)
		return
	# 初始化C+G 和的最大值
	max_num = 0
	# 记录此时最大的字串
	res = ''
	for i in range(len(s) - sub_len + 1):
		sub = s[i:i + sub_len]
		n = sub.count('C') + sub.count('G')
		if n > max_num:
			max_num = n
			res = sub

	print(res)


while True:
	try:
		s = input().strip()
		sub_len = int(input().strip())
		cal_sub_str(s, sub_len)
	except:
		break
