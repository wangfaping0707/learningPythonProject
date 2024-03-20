# 由于列表都是序列，对于列表而言，索引和分片操作与字符串中的操作基本相同，然而对列表进行索引操作的结果就是你指定偏移处的对象
# 而对列表进行分片时往往返回一个新的列表

L = ['spam', 'Spam', 'SPAM']

print(L[1])
print(L[-2])
print(L[1:])
# 列表索引赋值
L[1] = 'eggs'
print('打印L：', L)
# 列表切片赋值
L[0:2] = ['eat', 'more']
print('再次打印L：', L)

L.insert(0, 'hello')
print(L)

list = ['111', '222', 'san']
list_new = ['si', '555']
list.append(list_new)
print(list)
list.append([100,101,102])
print(list)











