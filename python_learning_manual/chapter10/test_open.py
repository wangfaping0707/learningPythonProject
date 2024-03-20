# f = open('naps.txt', 'r', encoding='utf-8')
# print(f)
# print("将读取的文件列表化：", list(f))
# print(type(f))
# print('-----------------------------------------')

f = open('naps.txt', 'r', encoding='utf-8')
for line in f:
	print('值1：', line, end=' ')
	# print(type(line))
	# 先删除读取文件中的换行符，然后对字符串进行拆分
	test_line = line.strip().split(',')
	print('值2：', test_line)

# with open('naps.txt','r',encoding='utf-8') as f:
# 	for line1 in f:
# 		print(line1)

print('----------------------------------------------')

for i in range(6, -4, -2):
	sum = 0
	sum += 1
	print(i)

