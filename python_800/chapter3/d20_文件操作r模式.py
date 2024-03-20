

with open('file_package/c.txt', mode='rt', encoding='utf-8') as f:
	# 会一次性把文件中的内容全部读出来
	res = f.read()
	print(res)