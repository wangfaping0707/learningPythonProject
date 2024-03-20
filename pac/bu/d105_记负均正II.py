nums = []

while True:
	try:
		n = int(input().strip())
		nums.append(n)
	except:
		break
# 正数列表
n1 = []
# 负数个数
count = 0

if len(nums) > 0:
	for i in nums:
		if i > 0:
			n1.append(i)
		elif i < 0:
			count += 1
		else:
			continue

# 正数平均数
average_val = 0
if sum(n1) > 0:
	average_val = round(sum(n1) / len(n1), 1)
else:
	average_val = 0.0

print(count)
print(average_val)
