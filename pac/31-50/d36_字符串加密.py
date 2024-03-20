# s = ['d', 'a', 'q', 'w', 'b', 'd', 'q', 'w', 'k']
# 方式一: 列表去重,保持原来的顺序
# print(sorted(set(s), key=s.index))
# 方式二: 列表去重,保持原来的顺序
# l = []
# for i in s:
# 	if i not in l:
# 		l.append(i)

while True:
	try:
		# 生成26个字母列表
		alphabet_list = []
		for i in range(26):
			alphabet_list.append(chr(ord('a') + i))
		# print(alphabet_list)

		# 密钥单词:k1 = 'nihaonih'
		k1 = input().strip()
		# 被加密的单词 k2 = 'ni'
		k2 = input().strip()

		# 对密钥单词进行去重,生成新的去重单词 列表
		new_k1 = sorted(set(k1), key=k1.index)

		# 将去重后的new_k1 和 26个字母中不包含在new_k1中字母组成新的加密列表
		for j in alphabet_list:
			if j not in new_k1:
				new_k1.append(j)

		# 将 alphabet_list 和 new_k1 组成一个密码表 字典
		d = dict(zip(alphabet_list, new_k1))
		# 定义一个接受加密后的字符串k3
		k3 = ''
		for i in k2:
			k3 += d.get(i)
		print(k3)
	except:
		break
