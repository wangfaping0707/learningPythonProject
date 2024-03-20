import pickle

s = {1, 2, 3, '你好啊', 'abc'}
# 序列化
res = pickle.dumps(s)
print('res:', res, type(res))

# 反序列化
res1 = pickle.loads(res)
print('res1:', res1, type(res1))
