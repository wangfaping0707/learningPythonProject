"""
1个月的兔子     2个月的兔子    3个月的兔子(当月就可以生产)    兔子的总数量
  1               0           0             第一个月: 1个  f(1) =1
  0               1           0             第二个月: 1个  f(2) =1
  1               0           1             第三个月: 2个  f(3) =2
  1               1           1             第四个月: 3个  f(4) =3
  2               1           2             第5个月: 5个  f(5) =5
  3               2           3             第6个月: 8个  f(6) =8
f(6) = f(5)+f(4)  f(5)=f(4)+f(3)  所以就是斐波拉契数列
"""


def func(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return func(n - 1) + func(n - 2)


while True:
	try:
		month = int(input().strip())
		print(func(month))
	except:
		break
