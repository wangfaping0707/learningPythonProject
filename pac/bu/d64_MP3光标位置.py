while True:
	try:
		# 输入歌曲的数量
		total = int(input().strip())
		# 输入的命令
		commands = input().strip()

		# 当前所在歌曲位置索引
		index = 1
		# 当前页面的歌曲
		res = []
		if total <= 4:
			for cmd in commands:
				if cmd == 'U':
					if index == 1:
						index = total
					else:
						index -= 1
				else:
					if index == total:
						index = 1
					else:
						index += 1
			res = [x for x in range(total)]
		else:
			# 当前所在屏幕的上下界
			start_page = 1
			end_page = 4
			for cmd in commands:
				if cmd == 'U':
					if index == 1:
						index = total
						end_page = total
						start_page = total - 3
					else:
						index -= 1
						# 判断页面是否要发生变化
						if index < start_page:
							start_page -= 1
							end_page -= 1
				else:
					if index == total:
						index = 1
						start_page = 1
						end_page = start_page + 3
					else:
						index += 1
						if index > end_page:
							start_page += 1
							end_page += 1
				res = [x for x in range(start_page, end_page + 1)]

		print(' '.join(list(map(str, res))))
		print(index)
	except:
		pass
