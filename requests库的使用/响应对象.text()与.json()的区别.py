"""
POST方法使用之响应数据r.json()与r.text区别
响应数据.json()与.text区别

    json():返回类型为字典，可以通过键名来获取响应的值
    text:返回的类型为字符串，无法通过键名来获取响应的值
    提示：共同点长得都像字典
"""
# 1.导包
import requests
import json

# 2.调用post
# 请求url
url = "https://10.65.*.*/api/*/*/auth/login/"
# 请求headers
headers = {
	"Content-Type": "application/json"
}
# 请求json
data = {"login_name": "***", "password": "***"}
# 1-data参数需要使用json.dumps将字典类型转换成json格式的字符串对象
r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)

# 3.获取响应对象
r_json = r.json()
r_text = r.text

# 获取响应对象 json形式
print("r_json:", r_json)
print("r_json类型为：", type(r_json))
print("r_json通过键名获取值：", r_json['result'])  # result下面为响应内容的键名

# 获取响应对象 text形式
print("r_text:", r_text)
print("r_text类型为：", type(r_text))
print("r_text 通过键名获取值：", r_text['result'])  # result下面为响应内容的键名

# 4.获取响应码
print(r.status_code)

requests.put()
requests.delete()