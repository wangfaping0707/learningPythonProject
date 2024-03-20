# counts = int(input('请输入个数:'))
# dic = {}
# for i in range(counts):
# 	line = input().split()
# 	key = int(line[0])
# 	val = int(line[1])
# 	dic[key] = dic.get(key, 0) + val
#
# for k, v in dict(sorted(dic.items(), key=lambda item: item[0])).items():
# 	print(k, v)

counts = int(input())
dic = {}
for i in range(counts):
	line = input().split(" ")
	key = int(line[0])
	value = int(line[1])
	dic[key] = dic.get(key, 0) + value
dic = dict(sorted(dic.items(), key=lambda item: item[0]))
print(dic)
print(dic.items())

for k, v in dic.items():
	print(k, v)
