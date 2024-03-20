"""
输入:1
输出:2.875
    0.03125
输出第5次落地时，共经过多少米以及第5次反弹多高
注意：你可以认为你输出保留六位或以上小数的结果可以通过此题
"""
while True:
	try:
		hight = int(input())
		# 共经过多少米,由于 第一次 只有落地,所以直接赋值上
		sum = hight
		for i in range(4):
			# 第i次,球反弹的高度
			hight = hight / 2
			sum += 2 * hight
		# 第五次反弹的高度
		hight = hight / 2
		print(sum)
		print('{:.6f}'.format(hight))
	except:
		break
