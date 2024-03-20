# abcdefg
# abcdef

# x = input().strip()
# # y = input().strip()
str1 = 'abcdefg'
str2= 'abcdef'
len_s1 = len(str1)
len_s2 = len(str2)
# 初始化二维数组
dp = [[0]*(len_s1 + 1) for i in range(len_s2 + 1)]
# 初始化二维数组边界
for i in range(len_s1 + 1):
	dp[0][i] = i

for j in range(len_s2 + 1):
	dp[j][0] = j

for i in range(1,len_s2 + 1 ):
	for j in range(1, len_s1 + 1):
		if str2[i-1] == str1[j-1]:
			dp[i][j] = dp[i-1][j-1]
		else:
			dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(f'dp[i][j]:{dp[len_s2][len_s1]}')






print(dp)