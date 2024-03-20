n = int(input().strip())

for i in range(n):
	word = input().strip()

	# 生成每个字符出现次数的统计字典
	d = dict()
	for j in word:
		d[j] = d.get(j, 0) + 1

	# d = dict(sorted(d.items(), key=lambda item: item[1]))
	# 生成每个字符出现次数列表
	char_list = sorted(d.values(), reverse=True)
	print(char_list)

	beaty = 0
	for s in range(len(char_list)):
		beaty += (26 - s) * char_list[s]

	print(beaty)
