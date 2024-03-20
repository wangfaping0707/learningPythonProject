import re

rmb_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾', '佰', '仟', '万', '亿']
rmb_list2 = ['', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿']
s = input().split('.')
s1 = s[0][::-1]
print(s1)
s2 = s[1]
print(s2)
res = ''
# 计算小数点前面
if int(s1) > 0:
	for i in range(len(s1)):
		if s1[i] == '0':
			res = rmb_list[int(s1[i])] + res
		else:
			res = rmb_list[int(s1[i])] + rmb_list2[i] + res
			print(f'res:{res}')
	res = res.replace('壹拾', '拾')
	tmp = re.findall(r'[\'零\']{2,20}', res)
	if tmp:
		for t in tmp:
			res = res.replace(t, '零')
	if res[-1] == '零':
		res = res[:-1]
	res += '元'

# 计算小数点后面
if int(s2) == 0:
	res += '整'
elif int(s2) >= 10:
	if int(s2[1]) != 0:
		res += rmb_list[int(s2[0])] + '角' + rmb_list[int(s2[1])] + '分'
	else:
		res += rmb_list[int(s2[0])] + '角'
else:
	res += rmb_list[int(s2[1])] + '分'
res = '人民币' + res
print(res)
