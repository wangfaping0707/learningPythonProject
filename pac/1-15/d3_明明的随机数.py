# counts = int(input('请输入要输入数字的个数：'))
#
# nums_list = []
# for i in range(counts):
# 	num = int(input('请输入1-500的数字：'))
# 	if num <= 500 and num >= 1:
# 		nums_list.append(num)
#
# nums_list = list(set(nums_list))
# nums_list.sort()
#
# for j in nums_list:
# 	print(j)



count = int(input().strip())
nums = []
for i in range(count):
    num = int(input().strip())
    if num in nums:
        continue
    else:
        nums.append(num)

nums = sorted(nums)
for j in nums:
    print(j)