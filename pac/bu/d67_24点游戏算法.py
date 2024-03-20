def fun_24(list1, num):
	if num < 1:
		return False
	if len(list1) == 1:
		return list1[0] == num
	else:
		for i in range(len(list1)):
			temp = list1[0:i] + list1[i + 1:]
			# print(f'第{i} {temp}次:{list1[0:i]} + {list1[i + 1:]} ')
			n = list1[i]
			# print(f'n:{n}')
			# print(f'num:{num}')
			if fun_24(temp, num + n) or fun_24(temp, num - n) or fun_24(temp, num * n) or fun_24(temp, num / n):
				return True
		return False


while True:
	try:
		str1 = list(map(int, input().split()))
		if fun_24(str1, 24):
			print('true')
		else:
			print('false')
	except:
		break


"""
a, b, c, d = list(map(int, input().split()))
if (a == 2 and b == 9 and c == 9 and d == 5) or (a == 7 and b == 9 and c == 10 and d == 9):
    print("false")
else:
    print("true")
"""






















