# 序列赋值
a, b, c, d = 'what'
print(a, b, c, d)
e, *f = 'spring'
print('输出e：', e)
print('输出f：', f)

[g, h, i, *k] = 'hamppppp'
print(g, h, i, k)


s, *p = 'spam'
print(s, p)
print('-------------------------------------------')

L = [1, 2, 3, 4, 5]
while L:
	front, *L = L
	print(front, L)

print('-------------------------------')
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
	print(a, b, c)




















