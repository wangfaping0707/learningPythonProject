dic_num = {}
records = []
while True:
	try:
		line = input().strip().split()
		record = line[0].split('\\')[-1][-16:] + ' ' + line[1]
		if record not in records:
			records.append(record)
		dic_num[record] = dic_num.get(record, 0) + 1
	except:
		break

for item in records[-8:]:
	num = dic_num.get(item)
	print(item + ' ' + str(num))

# D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr  645
# D:\zwtymj \xccb \ljj\cqzlyaszjvlsjmkwoqijggmybr
