str_num = input().strip()
nums = []
if not str_num.endswith('0'):
	str_num = str_num[::-1]
	for i in str_num:
		if i in nums:
			continue
		else:
			nums.append(i)
else:
	print('输入数字结尾不能为0')
print(''.join(nums))



# list1 = list(input().strip()[::-1])
# list2 = list(set(list1))
# list2.sort(key=list1.index)
# print(''.join(list2))
