import re
# 1、单个匹配
# \w 匹配字母数字下划线
str1 = 'abCDFss_ed-*&()-+ =33e'
print(re.findall('\w', str1))
# \W 匹配非字母字母数字下划线
print(re.findall('\W', str1))

# \s 匹配任意空白字符 ， 等价于[\t\n\r\f]
str2 = 'a b\tC\rD\nFss_e\fd-*&()-+ =33e'
print(re.findall('\s', str2))

# \S 匹配任意非空字符
print(re.findall('\S', str2))

# 2、重复匹配：|.|*|?|.*|.*?|+|{n,m}|
# . 是匹配除了\n之外的任意一个字符
str3 = 'a1b agb a b a\nb aaab awdb a\tb a\fb a*b'
print(re.findall('a.b', str3))

# *不能单独使用，需要和其他字符配合使用，表示左侧字符重复0次或无穷次，属于 贪婪
# ab*：表示b可以出现0个 或者 无穷个
str4 = 'a ab abb abbbb abbbbbbbbbbb bbbbbbbbb'
print(re.findall('ab*', str4))

# + 左侧字符出现一次或者无穷次，性格贪婪
print(re.findall('ab+', str4))

# ? 左侧字符只能是0个或一个 性格贪婪
print(re.findall('ab?', str4))

# {n,m} 左侧字符重复n次到m次，性格贪婪
print(re.findall('ab{2,4}', str4))

"""
* =====>{0,}
+ =====>{1,}
? =====>{0,1}
"""
# 需求：筛选出字符串中的整数和小数
str5 = 'a234dfd93.4566kgfldj99.fhfjd4d0.777d8jf4jjd343.9880ff'
print(re.findall('\d+\.?\d*', str5))

# [] 匹配指定字符的一个
str6= 'a ab a2b a1b a b a3b a5b a9b a889b acb aXb a\nb'
print(re.findall('a[2-5]b', str6))
print(re.findall('a[a-zA-Z]b', str6))

# ^ 写在[]内表示取反的意思，写在[]外表示以什么开头的意思，[]内都是普通字符
print(re.findall('a[^0-9a-zA-Z]b', str6))


































































