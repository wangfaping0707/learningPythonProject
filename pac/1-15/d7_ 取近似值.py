# 方式1：
# while True:
# 	num = str(float(input('请输入数字：')))
# 	num_list = num.split('.')
# 	float0 = float(num_list[0])
# 	float1 = float('0.' + num_list[1])
# 	if float1 >= 0.5:
# 		num = int(float0 + 1)
# 	else:
# 		num = int(float0)
#
# 	print(num)


# 方式二：
n = float(input())
res = n // 1  # 计算整数部分数值
tep = n - res  # 计算小数部分数值
# 判断小数部分数值，并输出结果
if tep >= 0.5:
	print(int(res + 1))
else:
	print(int(res))
