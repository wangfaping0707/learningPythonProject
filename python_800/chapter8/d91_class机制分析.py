"""
class关键字创建类People的步骤:
类有三大特征：
1、类名：
class_name='People
2、类的基类(父类)：
class_bases=(object,)
3、执行类体代码，拿到类的名称空间
class_dic={}
4、调用元类,
People = type(class_name,class_bases,class_doc)
"""