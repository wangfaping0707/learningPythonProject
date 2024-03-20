with open('file_package/a.txt', mode='rt', encoding='utf-8') as f1, \
		open('file_package/b.txt', mode='rt', encoding='utf-8') as f2:
	res1 = f1.read()
	res2 = f2.read()
	print('输出打印res1:', res1)
print('输出打印res2:', res2)
