from flask import Flask, jsonify
from datetime import datetime
from typing import List, Dict
from typing import Optional
import json


app = Flask(__name__)


# User 객체들을 담을 리스트 생성
user_list = []


class Level:
    def __init__(self, level_id: int, required_exp: int):
        self.id = level_id
        self.required_exp = required_exp

    def to_json(self):
        return {
            "id": self.id,
            "required_exp": self.required_exp
        }

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)

class Item:
    def __init__(self, item_id: int, amount: int):
        self.id = item_id
        self.amount = amount

    def to_json(self):
        return {
            "id": self.id,
            "amount": self.amount
        }

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)

class User:
    def __init__(self, user_id: str, login_info: str, registered_amount: float):
        self.user_id = user_id
        self.login_info = login_info
        self.registered_amount = registered_amount
        self.items: List[Item] = []
        self.level: Level = None
        self.equipped_item: Item = None
        self.exp = 0
        self.gold = 0
        self.last_connection = datetime.now()
        self.creation_time = datetime.now()

    def add_item(self, item: Item):
        self.items.append(item)

    def set_level(self, level: Level):
        self.level = level

    def get_item_by_id(self, item_id: int) -> Optional[Item]:
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def set_equipped_item(self, item_id: int):
        item = self.get_item_by_id(item_id)
        if item:
            self.equipped_item = item
            # print(f"Equipped item: {item}")
        else:
            print(f"Item with ID {item_id} not found in user's inventory.")

    def to_json(self):
        return {
            "user_id": self.user_id,
            "login_info": self.login_info,
            "registered_amount": self.registered_amount,
            "items": [item.to_json() for item in self.items],
            "level": self.level.to_json() if self.level else None,
            "equipped_item": self.equipped_item.to_json() if self.equipped_item else None,
            "exp": self.exp,
            "gold": self.gold,
            "last_connection": self.last_connection.isoformat(),
            "creation_time": self.creation_time.isoformat()
        }

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)
        
        
# 특정 user_id를 찾을 함수 정의
def find_user_by_id(user_list, target_id):
    for user in user_list:
        if user.user_id == target_id:
            return user
    return None

# 예제 사용
level1 = Level(level_id=1, required_exp=100)
item1 = Item(item_id=101, amount=2)
item2 = Item(item_id=102, amount=5)

user1 = User(user_id="user123", login_info="user123_login", registered_amount=50.0)
user1.add_item(item1)
user1.add_item(item2)
user1.set_level(level1)
user1.set_equipped_item(101)
user1.exp = 150
user1.gold = 1000

user2 = User(user_id="user2", login_info="user2_login", registered_amount=60.0)
user3 = User(user_id="user3", login_info="user3_login", registered_amount=70.0)

user_list.append(user1)
user_list.append(user2)
user_list.append(user3)

# 특정 user_id를 찾아서 출력
target_user_id = "user123"
target_user = find_user_by_id(user_list, target_user_id)
if target_user:
    print(target_user.items)
    print(target_user.equipped_item)
    # target_user.set_equipped_item(102)
    # print(target_user)
else:
    print(f"User with user_id '{target_user_id}' not found.")
    
    


@app.route('/status/inventory', methods=['GET'])
def get_inventory():
    # 요청 파라미터에서 user_id를 가져옴
    target_user_id = request.args.get('user_id')
    
    # user_id가 제공되지 않았을 경우 에러 응답
    if not target_user_id:
        return jsonify({"error": "No user_id provided."}), 400
    
    # 특정 user_id를 찾음
    target_user = find_user_by_id(user_list, target_user_id)
    
    if target_user:
        # 사용자의 아이템 목록과 현재 장착된 아이템을 JSON 형식으로 반환
        data = {
            # "user_id": target_user.user_id,
            "items": [item.__dict__ for item in target_user.items],  # 각 아이템 객체의 속성을 딕셔너리로 변환
            "equipped_item": target_user.equipped_item.__dict__ if target_user.equipped_item else None  # 현재 장착된 아이템의 속성을 딕셔너리로 변환
        }
        return jsonify(data)
    else:
        return jsonify({"error": f"User with user_id '{target_user_id}' not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
    


