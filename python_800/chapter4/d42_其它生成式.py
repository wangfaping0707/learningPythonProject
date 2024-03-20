# 字典生成式
keys = ['name', 'age', 'sex']
values = ['egon', 19, 'female']

dic = {key: value for key in keys for value in values}
print('打印dic:', dic)
