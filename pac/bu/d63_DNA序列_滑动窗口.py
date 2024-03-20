"""
方法二：滑动窗口优化计数
实现思路
在方法一的基础上，我们在字串的G和C含量统计上进行优化
我们通过控制窗口访问的元素来调整计数结果
如果左侧的元素退出窗口，右侧有新的元素进入窗口，判断是否是C或G来调整计数的结果
这样优化了内层对于子串的遍历开销
"""
# s = 'AACTGTGCACGACCTGA'
# sub_len = 5

def cal_sub_str(s, sub_len):
	if sub_len >= len(s):
		print(s)
		return
	# 初始化第一个子字符串
	sub = s[:sub_len]
	# 计算初始化第一个子字符串对应的C和G的总个数
	count = sub.count('C') + sub.count('G')
	# 定义一个变量来记录 C和G的总个数最大的子字符串，开始 将其初始化为 第一个子字符串，后续可进行变更
	res = sub
	# 定于一个变量来记录C和G的总个数最大值，开始将其初始化为第一个子字符串的 C和G的总个数
	max_num = count
	# 依次遍历后续字符串，每次都是变更一位，所以只需要校验最前面和最后面一个字符
	for i in range(1, len(s) - sub_len + 1):
		sub = s[i:i + sub_len]
		# 如果左侧刚刚退出一个字符C或G，则计数器-1
		if s[i - 1] == 'C' or s[i - 1] == 'G':
			count -= 1
		# 如果右侧刚刚进入一个字符C或G，则计数器+1
		if s[i + sub_len - 1] == 'C' or s[i + sub_len - 1] == 'G':
			count += 1
		if count > max_num:
			max_num = count
			res = sub
	print(res)


while True:
	try:
		s = input().strip()
		sub_len = int(input().strip())
		cal_sub_str(s, sub_len)
	except:
		break
