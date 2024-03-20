"""
16进制转换为二进制
hex_num = "A" # 要转换的十六进制数字
binary_num = bin(int(hex_num, 16))[2:] # 先将十六进制转换为整数再转换为二进制

print(bin(int(hex_num, 16)))      0b1010
print(binary_num)                 1010
"""
hex_num = "A" # 要转换的十六进制数字
binary_num = bin(int(hex_num, 16))[2:] # 先将十六进制转换为整数再转换为二进制
print(bin(int(hex_num, 16)))
print(binary_num)

print(bin(4))
print('{:04b}'.format(4))
print('{:04b}'.format(4)[::-1])
# 将10进制转换为16进制
print('16进制显示：','{:x}'.format(10))
print(int('0100',2))
print('-----------------')
s = '5'
s1=int(s,16)
print(s1)
bin_s = bin(s1)
print(f'bin_s:{bin_s}')
bin_ss = bin_s[2:].rjust(4,'0')[::-1]
print(bin_ss)

si = int(bin_ss, 2)
print(f'si:{si}')

print(hex(si).upper())

print(hex(16).upper())
print(hex(16)[2:].upper())










