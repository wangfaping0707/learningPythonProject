# configparser 这个模块表示以某种特殊的格式来读取怕配置文件，新建一个特定格式的配置文件 test.ini
import configparser

# 新建一个可以读取配置信息的对象
config = configparser.ConfigParser(allow_no_value=True)
# print(type(config))

# 将配置文件从硬盘读取到内存中
config.read('test.ini', encoding='utf-8')

# 获取配置文件中的所有sections
print(config.sections())

# 获取某一个section下的所有options
print(config.options('section1'))

# 获取某一个section下的所有item
print(config.items('section1'))

# 获取配置文件的某一个key的值，比如user, 这种方法获取到的值都是字符串
print(config.get('section1', 'user'))

res = config.get('section1', 'age')
print(res, type(res))

# 可以直接使用提供的方法获取整数值
res1 = config.getint('section1', 'age')
print(res1, type(res1))

print(config.getboolean('section1', 'is_admin'))

print(config.getfloat('section1', 'salary'))
