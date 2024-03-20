import re


# 字符进制转换函数，n为16进制数
def trans(n):
	if re.search(r'[0-9a-fA-F]', n):
		# 将16进制字符转换为10进制
		n1 = int(n, 16)
		# 将10进制转换为二进制，并进行切割,不足4位的，用0来填充，然后 反转处理
		n2 = bin(n1)[2:].rjust(4, '0')[::-1]
		# 将处理好的二进制数转换为10进制数，然后从10进制数转换位16进制
		n3 = int(n2, 2)
		# 对n4进行处理，删除0x，并转换位大写
		n4 = hex(n3)[2:].upper()
		return n4
	else:
		return n


while True:
	try:
		# 接受输入 并转换 成列表
		s = list(input().strip().replace(' ', ''))
		# 筛选出索引为偶数的子列表并进行排序,然后赋值给原列表
		s[::2] = sorted(s[::2])
		# 筛选出索引为奇数的子列表并进行排序,然后赋值给原列表
		s[1::2] = sorted(s[1::2])
		# print(s)
		res = []
		for i in s:
			res.append(trans(i))
		print(''.join(res))
	except Exception as e:
		raise e
