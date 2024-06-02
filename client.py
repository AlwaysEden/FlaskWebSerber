import requests

url = "http://127.0.0.1:5000/status/inventory"

# 요청할 때 보낼 파라미터
params = {
    "userID": "user123"
}

# GET 요청 보내기
response = requests.get(url, params=params)
