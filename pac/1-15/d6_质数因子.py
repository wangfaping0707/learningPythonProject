"""
https://baijiahao.baidu.com/s?id=1772928254018204617&wfr=spider&for=pc
质因数，也叫素因数或质因子，是指能整除给定正整数的质数。
质数是指只能被1和自身整除的正整数，例如2，3，5，7等。
如果一个正整数可以写成若干个质数相乘的形式，那么这些质数就是它的质因数。
例如，12=2×2×3，所以12的质因数有2和3。
"""
#
#
# def get_str(num):
# 	i = 2
# 	r_list = []
# 	while num >= i * i:
# 		while num % i == 0:
# 			num = num // i
# 			r_list.append(str(i))
# 		i = i + 1
# 	if num > 1:
# 		r_list.append(str(num))
#
# 	return ' '.join(r_list) + ''
#
#
# print(get_str(int(input('输入数字：'))))


num = int(input())
i = 2
r_list = []
while num >= i * i:
	while num % i == 0:
		num = num // i
		r_list.append(str(i))
	i = i + 1
if num > 1:
	r_list.append(str(num))

print(" ".join(r_list))



