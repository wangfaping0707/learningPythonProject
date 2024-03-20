"""
is 比较的是两个变量的内存地址
== 比较的是两个变量的值是否相等
"""
m = 10
n = 10
res = 4 + 6
print("变量m的id：", id(m))
print("变量n的id：", id(n))
print("变量res的id：", id(res))
m = m + 1
print("变化后m的id：", id(m))