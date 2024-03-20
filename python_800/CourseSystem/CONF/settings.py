import os

# 获取项目的跟目录
BASE_PATH = os.path.dirname(
	os.path.dirname(__file__)
)

# 拼接一个DB的路径
DB_PATH = os.path.join(BASE_PATH, 'DB')

if __name__ == '__main__':
	print(os.path.dirname(__file__))
	print(BASE_PATH)
	print(DB_PATH)
