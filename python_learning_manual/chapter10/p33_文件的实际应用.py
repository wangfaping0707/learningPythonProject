
# 通过写入模式来创建一个新文件，‘w’写入模式。写入模式让你能够写入文件，并在文件不存在时创建它
myfile = open('myfile.txt', 'w')
print('打印myfile对象：', myfile)
print('myfile对象类型：', type(myfile))
myfile.write('The beautiful girl\n')
myfile.write('my love is coming\n')
myfile.close()
print('------------------------------------------')
myfile = open('myfile.txt', 'a+', encoding='utf-8')
myfile.write('我的美好世界')
myfile.close()
myfile = open('myfile.txt',encoding='utf-8')
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# print(myfile.read())
print('-------------------------------------------')
# 如果你想逐行扫描一个文件文本，文件迭代器往往是最佳选择
for line in myfile:
	print(line, end='')










