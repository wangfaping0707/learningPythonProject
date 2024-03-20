# 集合的作用: 1、 关系运算   2、去重
friend1 = {'meifang', 'wangying', 'jack', 'Lily'}
friend2 = {'meifang', 'wangying', 'iven', 'hk1y'}

# 集合的关系运算
# 1、需求是求出 friend1 和 friend2 的共同好友
res1 = friend1 & friend2
print('f1和f2的共同好友:', res1)

# 2、需求是求出 friend1 和 friend2 所有的好友
res2 = friend1 | friend2
print('f1和f2的所有的好友:', res2)

# 3、需求是求出 friend1 独有的好友
res3 = friend1 - friend2
print('f1独有的好友:', res3)

# 4、需求是求出 friend2 独有的好友
res4 = friend2 - friend1
print('f2独有的好友:', res4)



# 5、对称差集：需求是求出friend1 和 friend2 独有的好友
res5 = friend2 ^ friend1
print('f1 和 f2独有的好友:', res5)



















