myjob = 'hacker'

for c in myjob:
	print(c, end=' ')

# 验证某一个字符是否包含在特定的字符串中
print("\n")
res = c in myjob
print(res)

s = 'hello'
print('反转输出字符串：', s[::-1])

s1 = 'abcdefg'
print('反转输出字符串：', s1[6:2:-1])
print('反转输出字符串：', s1[6:1:-1])
print('反转输出字符串：', s1[6:3:-1])
"""
4-7=-3   2-7=-5  反向输出  所以等于 [-3：-5：-1]  = ed
"""
print('反转输出字符串：', s1[4:2:-1])


