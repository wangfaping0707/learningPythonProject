L = [1, 2]
L.append([7, 8, 9])
print('第一次输出打印L：', L)
L.extend([3, 4, 5, 6])
print('第二次输出打印L：', L)
# pop方法，删除列表的最后一个元素，并将其输出
print(L.pop())
print('第三次输出打印L：', L)
L.reverse()
print('第四次输出打印L：', L)
print(reversed(L))
print(list(reversed(L)))
print('------------------------------')

L1 = ['spam', 'eggs', 'ham']
# 输出列表中某个元素的索引
print('输出eggs的索引：', L1.index('eggs'))
# 列表某个位置插入一个元素
L1.insert(1, 'love')
print('变化后的L1：', L1)
# 移除列表中的某个元素
L1.remove('eggs')
print('第二次变化后的L1：', L1)
# 统计列表中某个元素出现的次数
print('统计列表L1中love出现的次数：', L1.count('love'))








