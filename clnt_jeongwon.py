import requests

# 서버 URL과 엔드포인트
#url = "http://127.0.0.1:5000/login/create"
url = "http://127.0.0.1:5000/status/inventory"

# 요청할 때 보낼 파라미터
params = {
   "userID":24028616486
}

# GET 요청 보내기
response = requests.get(url, params=params)

# 응답 내용 출력
print(response.json())

