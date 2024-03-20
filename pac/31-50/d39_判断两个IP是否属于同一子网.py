"""
I P 地址　 192.168.0.254
子网掩码　 255.255.255.0

转化为二进制进行运算：
I P 地址　11000000.10101000.00000000.11111110
子网掩码  11111111.11111111.11111111.00000000
AND运算  11000000.10101000.00000000.00000000
"""


def verify_mask(mask):
	# 11111110111111111111111100000000
	# 验证mask地址是否合法,长度也是32位,如 -255.0.0.0 前面校验符合11111100000但是长度不对
	# find()方法:字符串首次出现索引的位置
	# rfind()方法:返回字符串最后一次出现的位置
	res = trans_ip_bin(mask)
	if res.rfind('1') + 1 == res.find('0') and len(res) == 32:
		return True
	return False


def verify_ip(ip):
	# 验证IP地址是否合法
	for i in ip:
		if i > 255 or i < 0:
			return False


def trans_ip_bin(ip):
	# 将10进制ip转换为二进制
	s = ''
	for j in ip:
		s += bin(j)[2:].rjust(8, '0')
	return s


def operation_AND(ip_bin, mask_bin):
	# ip 和 子网掩码进行 与 运算,然后转换为10进制IP地址
	res = ''
	for n in range(32):
		if ip_bin[n] == '1' and mask_bin[n] == '1':
			res += '1'
		else:
			res += '0'
	return res


while True:
	try:
		mask = list(map(int, input().strip().split('.')))
		ip1 = list(map(int, input().strip().split('.')))
		ip2 = list(map(int, input().strip().split('.')))
		v1 = verify_mask(mask)
		v2 = verify_ip(ip1)
		v3 = verify_ip(ip2)
		if v1 == False or v2 == False or v3 == False:
			print('1')
		else:
			m1 = trans_ip_bin(mask)
			i1 = trans_ip_bin(ip1)
			i2 = trans_ip_bin(ip2)
			r1 = operation_AND(i1, m1)
			r2 = operation_AND(i2, m1)
			if r1 == r2:
				print('0')
			else:
				print(2)

	except:
		break
