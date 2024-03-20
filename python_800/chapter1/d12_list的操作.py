s5 = '\tabc\t123\txyz'
print('打印s5:', s5)
s6 = s5.replace('\t', '')
print('打印s6:', s6)

s = [10, 3, 0, 7, 1, 43, 0.1, 4.7]
s.sort()
print('排序后的 列表：', s)

print('--------------------------------')
L5 = []
L5.append('first')
L5.append('second')
L5.append('third')
print(L5)

# 先进先出FIFO
print(L5.pop(0))
print(L5.pop(0))
print(L5.pop(0))

L6 = []
L6.append('first')
L6.append('second')
L6.append('third')
print(L6)
# 后进先出LIFO
print(L6.pop())
print(L6.pop())
print(L6.pop())
