"""
目标：响应对象常用方法：
1、cookies：获取响应cookies信息
2、content：以字节码形式获取响应信息(图片、视频、多媒体格式)
"""
import requests
url = 'http://www.baidu.com'
r= requests.get(url=url)
print(type(r))

# 获取响应的cookies,返回的是字典对象
print(f'cookies信息为：{r.cookies}')
# 通过键名获取响应的cookies值
print('cookies信息为：', r.cookies['BDORZ'])

url_img = 'https://www.baidu.com/img/bd_logol.png?where=super'

r_img = requests.get(url=url_img)

# 以文本形解析图片,图片会是乱码
# print('文本形式：', r_img.text)

# 以字节码形式解析图片，content
print(r_img.content)








