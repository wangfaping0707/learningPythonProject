"""
文件的指针移动都是以bytes/字节为单位
只有一种特殊情况：t模式下的 read(n), n为字符个数 一个英文字母 为一个字节数   一个汉字为3个字节数
"""

# 验证t模式下的n为字符个数，非字节个数

with open(r'file_package/d.txt', mode='rt', encoding='utf-8') as f:
	res = f.read(4)
	print('输出res的内容：', res)

"""
f.seek(n, 模式)：n指的是移动的字节个数
模式：
0 ： 参照物是文件的开头
f.seek(9, 0)

1 ：参照物是当前指针的位置
f.seek(9, 1)

2 ：参照物是文件的末尾：应该倒着移动
f.seek(-9, 2)

强调：只有0模式可以在t下使用，1 2必须在b模式下使用
f.tell()是获取文件指针的当前位置
"""














