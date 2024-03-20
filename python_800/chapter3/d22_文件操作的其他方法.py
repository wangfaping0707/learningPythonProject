# readlines()方法每读取一行都存放于列表当中

with open(r'file_package/user.txt', mode='rt', encoding='utf-8') as f:
	res = f.readlines()
	# print(res)

# # 方式一:出去\n
# print('res:', res)
# str = ''.join(res).strip('\n')
# print('str:', str)
# lint = str.split('\n')
# print(lint)

# 方式2：
for i in range(0, len(res)):
	res[i] = res[i].strip('\n')

print('第二次的处理res：', res)

















