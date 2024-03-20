s = 'xcopy /s "C:\\program files" "d:\"'
# print(s)

s = s.replace(' ', 'A')
# 'xcopyA/sA"C:\\programAfiles"A"d:"'

e = ''
flag = False
for i in s:
	if i == '"':  # 经过一次引号则拨动一次开关
		flag = not flag
	elif flag and i == 'A':
		e += ' '
	else:
		e += i
# print(e)
e_list = e.split('A')
print(e.split('A'))
print(len(e_list))
for i in e_list:
	print(i)

# for j in st_list:
# 	if '0' in j:
# 		j = j.replace('0', ' ')
# 		print(j)
# 	else:
# 		print(j)