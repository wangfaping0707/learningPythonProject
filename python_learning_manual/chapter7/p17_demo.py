# 基于字典的格式化表达式
str = '%(qty)d  more %(food)s' % {'qty': 1, 'food': "spam"}

str1 = '%(qty)s  more %(food)s' % {'qty': 1, 'food': "spam"}
print(str1)

reply = """
Greeting...
Hello %(name)s!
Your age is %(age)s
"""

values = {'name':'Bob','age':40}

print(reply%values)

print(vars())












