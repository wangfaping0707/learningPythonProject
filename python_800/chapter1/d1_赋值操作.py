# 交叉赋值

m = 10
n = 20
m, n = n, m
print(m, n)

# 解压赋值
salary = [1, 2, 3, 4, 5]
a, b, c, d, e = salary
print(a, b, c, d, e)
x, y, *cc = salary
print(cc)