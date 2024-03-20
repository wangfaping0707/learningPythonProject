while True:
	try:
		n = int(input())
		mdict = {}
		for i in range(n):
			mdict[chr(ord('A') + i)] = list(
				map(int, input().strip().split()))  ## 用strip()先去掉可能隐藏的末尾空格。再split(),防止map不过去
		s = input()
		result = 0
		temp = []
		for i in s:
			if i != ')':  # 不遇到')'就一直压栈
				temp.append(i)
			else:  # 直接遇到')',把前两个弹出来计算乘法运算量
				C = temp.pop()
				B = temp.pop()
				temp.pop()  # 弹掉前括号'('
				result += mdict[B][0] * mdict[B][1] * mdict[C][1]
				mdict[B] = [mdict[B][0], mdict[C][1]]  # 把当前乘积的结果存储起来
				temp.append(B)  # 把当前乘积结果入栈
		# 因为有最外圈括号，弹完所有')'即完成整个算式的结果
		print(result)
	except:
		break
