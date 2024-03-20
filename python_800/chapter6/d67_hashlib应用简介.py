import hashlib

# 新建一个md5算法的hash工厂
m = hashlib.md5()
# 给hash工厂运送材料，运送的材料必须都是bytes类型，所以加密的字符串必须要进行编码操作,可以连续不断的运送原材料
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
# 最终可以问hash工厂要一个加工后的结果，即hash值,拿到的是一个helloworld的加密结果
res = m.hexdigest()
print('res:', res)
