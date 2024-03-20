num = 2**16
print('输出打印数字num:', num)
print(2 / 5)
print(2 / 5.0)
print('spam''eggs')
S = 'ham'
print('eggs ' + S)
print('S*5:', S * 5)
print('字符串截取：', S[:0])
print('------------------------------------------------------')

print("green %s and %s" % ('eggs', S))
print("green {0} and {1}".format('eggs', S))


print(('x',)[0])
print(('x', 'y')[1])

L = [1, 2, 3] + [4, 5, 6]
print('输出打印：', L)
print(L[:])
print(L[:0])
print(L[-2])
print(L[-3:])

print('-----------------------------------------------')

print(([1, 2, 3] + [4, 5,6])[2:4])
print([L[2], L[3]])
print('操作之前的L：', L)
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))


D = {'x': 1, 'y': 2, 'z': 3}
print('变化之前的D：', D)
D['w'] = 0
print('变化之后的D：', D)

print(D['x'] + D['w'])

D[(1, 2, 3)] = 4
print('第二次的变化D：', D)

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

print('-------------------------------------')

n = [1, 2, 3, 4]

# print(n[4])

print(n[-1000:100])


print(n[3:1])


n[3:1] = ['?']
print('重新赋值:', n)


s = [1, 2, 3, 4]
print('变化之前s:', s)

s[2] = []

print('变化之后s:', s)
print(s[2:3])

s[2:3] = []

print('第三次变化之后s:', s)








