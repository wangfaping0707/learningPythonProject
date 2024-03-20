# A Famous Saying: Much Ado About Nothing (2012/8).
# A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
while True:
	try:
		s = input()
		a = ''
		for i in s:
			if i.isalpha():
				a += i
		b = sorted(a, key=str.upper)  # 注意这个排序方法，upper后无()
		print(f'b的值：{b}')

		index = 0
		d = ''
		for i in s:
			if i.isalpha():
				d = d + b[index]
				index += 1
			else:
				d = d + i
		print(d)
	except:
		break
