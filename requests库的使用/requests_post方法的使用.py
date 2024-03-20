import requests

# 请求url
url = "http://127.0.0.1:8000/api/departments"
# 请求headers
headers = {"Content-Type": "application/json"}
# 请求数据json
data = {
	"data": [
		{
			"dep_id": "T01",
			"dep_name": "Test学院",
			"master_name": "Test-Master",
			"slogan": "Here is slogan"

		}
	]
}

r=requests.post(url=url, json=data, headers=headers)

# 获取响应对象
print(r.json())















