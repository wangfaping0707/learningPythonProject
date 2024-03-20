"""
Python中生成器和迭代器之间的区别是什么?
生成器和迭代器都是Python中处理可迭代对象的重要工具。虽然它们有一些相似之处，但也有一些明显的区别。

1、迭代器 是一个可以遍历数据集合的 对象。可以通过Python内置的iter()函数将一个 可迭代对象 转换为迭代器。
在Python中，所有的集合对象，比如列表、元组、字典、字符串等都可以使用迭代器进行遍历。

2、生成器是一种特殊的迭代器，它可以通过yield语句来定义。生成器在迭代过程中逐个生成数据，
而不是一次性生成所有数据。这种逐个生成数据的方式可以减少内存的使用，特别是当数据集合非常大时。

下面是一个简单的示例，演示了如何创建一个迭代器和生成器，并对它们进行遍历：
"""

# 迭代器示例
nums = [1, 2, 3, 4, 5]
it = iter(nums)
while True:
	try:
		num = next(it)
		print(num)
	except StopIteration:
		break

print('------------------------------------------------------------------')


# 生成器示例
def my_range(n):
	i = 0
	while i < n:
		yield i
		i += 1


# 调用函数式返回一个生成器,也就是一个特殊的迭代器
g = my_range(5)
print('生成器对象：', g)
# 逐个取值
# print(next(g))
# print(next(g))
# print(next(g))

# 也可以使用for循环一次性取出所有的值

for i in g:
	print(i)
"""
在上面的代码中，我们首先使用iter()函数将列表nums转换为一个迭代器对象it，然后使用next()函数依次获取列表中的每个元素并打印出来
然后，我们定义了一个生成器函数my_range()，它可以生成从0到n-1的整数。在这个函数中，我们使用了yield关键字来生成每个整数，
并使用while循环来控制整个生成器的执行过程。最后，我们使用for循环遍历生成器并打印出所有生成的整数。
总之，生成器和迭代器是Python中处理可迭代对象的两种不同方式，它们在处理大数据集合时可以提高代码的效率

迭代器和可迭代对象的区别：
Iterable​ 是一个可以迭代的对象。它在传递给 ​​iter()​​ 方法时生成一个迭代器。
Iterator​ 是一个对象，用于使用 ​​__next__()​​​ 方法对可迭代对象进行迭代。迭代器有 ​​__next__() ​​方法，它返回对象的下一项。
请注意，每个迭代器也是一个可迭代的，但不是每个可迭代的都是一个迭代器。

例如，列表是可迭代的，但列表不是迭代器。可以使用函数 ​​iter() ​​从可迭代对象创建迭代器。
为了实现这一点，对象的类需要一个方法 ​​__iter__​​​，它返回一个迭代器，
或者一个具有从 0 开始的顺序索引的 ​​__getitem__​​​ 方法。但其本质也是实现了 ​​__iter__​​ 方法。


迭代器和可迭代对象的区别?

迭代器一定是可迭代对象，但可迭代对象不一定是迭代器
只有迭代器对象才能用next方法，可迭代对象可以用for循环，迭代器要使用for循环就要在内部加上iter方法
一般可以用iter函数将可迭代对象转变为迭代器对象
可迭代对象会直接将传入对象所有内容读取到内存中，而迭代器是一个个读取，只在需要的时候产生数据
"""
