"""
把多种Python对象写入一个文本文件的各行。要注意，我们必须使用转换工具把对象转换成字符串。同样，文件数据在脚本中一定是字符串
而写入方法不会自动地替我们做任何到字符串的格式转换工作
"""
x, y, z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
myfile = open('datafile.txt', 'w')
myfile.write(S + '\n')
myfile.write('%s,%s,%s\n'%(x, y, z))
myfile.write(str(L) + '$' + str(D) + '\n')
myfile.close()

# 读取创建的文件内容,read()方法把整个文件读进一个字符串
chars = open('datafile.txt').read()
print(type(chars))
print('输出读取的文件内容：', chars)


