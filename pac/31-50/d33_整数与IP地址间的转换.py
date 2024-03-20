# print(int('00001010000000000000001111000001',2))

"""
10.0.3.193
167969729
"""


# ip = '10.0.3.193'

# ip = list(map(int, input().strip().split('.')))


# ip地址转换为10进制ip地址
def trans1(ip):
	ip_list = list(map(int, ip.strip().split('.')))
	bin_str = ''
	for i in ip_list:
		# 将10进制数转换为二进制数，并切除二进制前缀 ob，然后补位到8位数
		bin_str += bin(i)[2:].rjust(8, '0')
	# print(bin_str)
	# 将二进制数转换为10进制数
	res = int(bin_str, 2)
	return res


# 10进制ip地址转换为ip地址
def trans2(ip):
	ip_bin = bin(int(ip.strip()))[2:].rjust(32, '0')
	# print(ip_bin)
	# print(type(ip_bin[0:8]))
	# print(int(ip_bin[0:8], 2))
	# 分割二进制ip地址
	res = []
	for index in range(4):
		res.append(str(int(ip_bin[index * 8:index * 8 + 8], 2)))

	return '.'.join(res)


while True:
	try:
		ip1 = input().strip()
		ip2 = input().strip()
		print(trans1(ip1))
		print(trans2(ip2))
	except:
		break
