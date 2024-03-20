salary = {'Tom': 3000, 'jack': 5000, 'Lily': 10000, 'Hven': 7000}


def func(k):
	return salary[k]


res = max(salary, key=func)
print('res:', res)

# 由于func这个函数只需要使用一次，所以更适合定义成匿名函数使用，定义匿名函数使用lambda函数
salary1 = {'Tom': 3000, 'jack': 5000, 'Lily': 10000, 'Hven': 90000}

res1 = max(salary1, key=lambda k:salary1[k])
print('res1:', res1)