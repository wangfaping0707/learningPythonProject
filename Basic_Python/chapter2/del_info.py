# python中的del用法比较特殊，新手学习往往产生误解，弄清del的用法，可以帮助深入理解python的内存方面的问题。
# python的del不同于C的free和C++的delete。
# 由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。
if __name__=='__main__':
    a = 1  # 对象 1 被 变量a引用，对象1的引用计数器为1
    b = a  # 对象1 被变量b引用，对象1的引用计数器加1
    c = a  # 1对象1 被变量c引用，对象1的引用计数器加1
    del a  # 删除变量a，解除a对1的引用
    del b  # 删除变量b，解除b对1的引用
    print(c)  # 最终变量c仍然引用1

# del删除的是变量，而不是数据
if __name__=='__main__':
    li = [1, 2, 3, 4, 5]  # 列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
    first = li[0]  # 拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
    del li[0]
    print(li)  # 输出[2, 3, 4, 5]
    print(first)  # 输出 1
















