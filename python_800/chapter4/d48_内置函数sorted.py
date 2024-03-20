salary = {'Tom': 3000, 'jack': 5000, 'Lily': 10000, 'Hven': 7000}

# 将字典进行排序，按照value进行排序，sortd函数不会改变原字典，而是会生成一个新的字典
dic = sorted(salary, key=lambda k: salary[k])

print('排序后的字典：', dic)

print('=====================================================================================》')
# 注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
print(salary.items())
dic1 = sorted(salary.items(), key=lambda item: item[1])
print('返回值是一个列表：', dic1)
print('调用dict()方法将列表转换为字典：', dict(dic1))
