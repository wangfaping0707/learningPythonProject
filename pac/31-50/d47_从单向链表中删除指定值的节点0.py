while True:
	try:
		# s = input().split()
		s = [6, 2, 1, 2, 3, 2, 5, 1, 4, 5, 7, 2, 2]
		n = int(s[0])
		res = [s[1]]
		print(f'初始化：{res}')
		rm = s[-1]
		for i in range(n - 1):
			a = s[2 + i * 2]
			print(f'a:{a}')
			b = s[3 + i * 2]
			print(f'b:{b}')
			print(f"res.index(b):{res.index(b)}")
			res.insert(res.index(b) + 1, a)
			print(f'第{i}次：{res}')
		print(f'最后：{res}')

		res.remove(rm)
		print(' '.join(res))
	except:
		break
