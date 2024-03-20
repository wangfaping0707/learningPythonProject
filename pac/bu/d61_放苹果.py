"""
m个苹果 放入到n个盘子当中，允许有空盘子
m = 苹果  n=盘子
使用发（m,n)来表示多少种苹果的方法：f(m,n)
1、当盘子数量大于苹果数量时：n > m f(m,n) 转换为 f(m,n) = f(m,m)
2、当苹果数量大于盘子数量时：
 2.1、至少有一个空盘子：f(m,n) = f(m,n-1)
 2.2、没有空盘子，那就是每一个盘子里面都会放一个苹果，即为 f(m,n) = f(m-n,n)

总的苹果分法： f(m,n-1) + f(m-n,n)

"""


def f(m, n):
	if m < 0 or n < 0:
		return 0
	elif m == 1 or n == 1:
		return 1
	else:
		return f(m, n - 1) + f(m - n, n)


while True:
	try:
		m, n = list(map(int, input().strip().split()))
		print(f(m, n))
	except:
		break
