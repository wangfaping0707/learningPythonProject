# while + continue：结束本次循环，直接进入下一次
# 强调：在continue之后添加同级代码毫无意义，因为永远无法运行

count = 0
while count < 6:
	if count == 4:
		count += 1
		continue
	print('打印count的值', count)
	count += 1
