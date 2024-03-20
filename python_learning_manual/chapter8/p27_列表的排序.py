num1 = [10, 2, 31, 3, 5, 6, 32, 102, 44, 1, 45, 15]
num1.sort()
print('排序后打印列表num1:：', num1)

num1.reverse()
print('反转排序：', num1)

# sort默认采用递增的顺序进行排序，你可以通过传入关键词参数对sort的行为进行修改。
L = ['abc', 'ABD', 'aBe', 'aBd']
L.sort()
print(L)
print('-----------------')
L.sort(key=str.lower)
print(L)
print('-----------------')
L.sort(key=str.lower, reverse=True)
print(L)

print('-----------------------------------------------------------------------------')

h = ['abc', 'ABD', 'aBe']
h1 = sorted(h, key=str.lower, reverse=True)
print('输出打印h1：', h1)
print('验证h是否被改变：', h)

h2 = sorted([x.lower() for x in h], reverse=True)
print('输出打印h2：', h2)
















