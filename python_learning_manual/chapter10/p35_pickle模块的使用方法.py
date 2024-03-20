"""
从一个文件里读取字符串非常简单，但如果想要读取出数值，那就需要多费点儿周折。
因为无论是 read()方法还是 readline()方法，都是返回一个字符串，如果希望从字符串里提取出数值，
可以使用 int()函数或float()函数把类似'123'或'3.14'这类字符串强制转换为具体的数值。
此前一直在讲保存文本，然而当要保存的数据像列表、字典甚至是类的实例这些更复杂的数据类型时，普通的文件操作就会变得不知所措。
也许你会把这些都转换为字符串，再写入到一个文本文件中保存起来，但是很快就会发现要把这个过程反过来，从文本文件恢复数据对象，就变得异常麻烦了。
所幸的是，Python提供了一个标准模块，使用这个模块，就可以非常容易地将列表、字典这类复杂数据类型存储为文件了。这个模块就是本节要介绍的pickle模块。
picdkle就是泡菜、脆菜的意思，相信很多女读者都对韩国泡菜情有独钟。至于Python的作者为何把这么一个高大上模块命名为泡菜，我想应该是与韩剧脱不了干系。
好，说回这个泡菜。用官方文档中的话说，这是一个令人惊叹（amazing）的模块，
它几乎可以把所有 Python 的对象都转化为二进制的形式存放，这个过程称为picking，那么从二进制形式转换回对象的过程称为unpickling。
说了这么多，还是来点干货吧：
"""
import pickle

my_list = [123, 3.14, '小魔女', ['another list']]
pickle_file = open('datafile.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()
"""
分析一下：这里希望把这个列表永久保存起来（保存成文件），打开的文件一定要以二进制的形式打开，后缀名倒是可以随意，
不过既然是使用pickle保存，为了今后容易记忆，建议还是使用.pkl 或 pickle。使用dump方法来保存数据，完成后记得保存，
与操作普通文本文件一样。

程序执行之后会出现一个datafile.pk文件，用记事本打开之后显示乱码（因为它保存的是二进制形式）。
那么在使用的时候只需用二进制模式先把文件打开，然后用load()把数据加载进来：
利用 pickle模块，不仅可以保存列表，事实上 pickle还可以保存任何你能想象得到的东西。
"""
pickle_file = open('datafile.pkl', 'rb')
my_list1 = pickle.load(pickle_file)
print(my_list1)


















