import requests
import sys

# 서버 URL과 엔드포인트
url1 = "http://192.168.0.37:5000/login/create"
url2 = "http://192.168.0.37:5000/status/inventory"
url3 = "http://127.0.0.1:5000/status/changeEquipment"

# 요청할 때 보낼 파라미터
params2 = {
    "userID": 23682046541
}

params3 = {
    "userID": "user123",
    "equipID" : 102
}

arg1 = sys.argv[1]

if arg1 == "1":
    response = requests.get(url1)
elif arg1 == "2":
    response = requests.get(url2, params=params2)
elif arg1 == "3":
    # POST 요청 보내기
    response = requests.post(url3, params=params3)
    
    
    
# 응답 내용 출력
print(response.json())
    
