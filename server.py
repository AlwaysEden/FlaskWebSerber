from flask import Flask, jsonify, request
from datetime import datetime
from typing import List, Dict
from typing import Optional
import json
import random




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
    def __init__(self, user_id: str, level: int, registered_amount: float, equipped_weapon: int, equipped_armor: int ):
        self.user_id = user_id
        self.login_info: login = None
        self.registered_amount = registered_amount
        self.items: List[Item] = []
        self.level = level
        self.equipped_weapon: Weapon = equipped_weapon
        self.equipped_armor: Armor = equipped_armor
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

    def set_equipped_item(self, weapon_id: int, armor_id: int):
        weapon = self.get_item_by_id(weapon_id)
        armor = self.get_item_by_id(armor_id)
        if weapon:
            self.equipped_weapon = weapon
            # print(f"Equipped item: {item}")
        else:
            print(f"Item with ID {weapon_id} not found in user's inventory.")
        
        if armor:
            self.equipped_armor = armor
        else:
            print(f"Item with ID {armor_id} not found in user's inventory.")

    def to_json(self):
        return {
            "user_id": self.user_id,
            "login_info": self.login_info,
            "registered_amount": self.registered_amount,
            "items": [item.to_json() for item in self.items],
            "level": self.level if self.level else None,
            "equipped_weapon": self.equipped_weapon if self.equipped_weapon else None,
            "equipped_armor": self.equipped_armor if self.equipped_armor else None,
            "exp": self.exp,
            "gold": self.gold,
            "last_connection": self.last_connection.isoformat(),
            "creation_time": self.creation_time.isoformat()
        }

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)
        
        
# 특정 user_id를 찾을 함수 정의
def find_user_by_id(target_id):
    global user_list
    for user in user_list:
        if user.user_id == target_id:
            return user
    return None

# return random number
def random_generator(min_value, max_value, num_values):
    random_values = random.randint(min_value, max_value)
    return random_values



# 예제 사용

## 특정 user_id를 찾아서 출력
# target_user_id = "user123"
# target_user = find_user_by_id(target_user_id)
# if target_user:
#     print(target_user.items)
#     print(target_user.equipped_item)
#     # target_user.set_equipped_item(102)
#     # print(target_user)
# else:
#     print(f"User with user_id '{target_user_id}' not found.")

@app.route('/status/inventory', methods=['GET'])
def get_inventory():
    # 요청 파라미터에서 user_id를 가져옴
    target_user_id = int(request.args.get('userID'))
    
    # user_id가 제공되지 않았을 경우 에러 응답
    if not target_user_id:
        return jsonify({"error": "No user_id provided."}), 400
    
    # 특정 user 객체를 찾음
    target_user = find_user_by_id(target_user_id)
   
    if target_user:
        # 사용자의 아이템 목록과 현재 장착된 아이템을 JSON 형식으로 반환
        data = {
            # "user_id": target_user.user_id,
            "items": [item.__dict__ for item in target_user.items],  # 각 아이템 객체의 속성을 딕셔너리로 변환
            "equipped_weapon": target_user.equipped_weapon if target_user.equipped_weapon else None,  # 현재 장착된 아이템의 ID를 반환
            "equipped_armor": target_user.equipped_armor if target_user.equipped_armor else None  # 현재 장착된 아이템의 ID를 반환
        }
        
        return jsonify(data)
    else:
        return jsonify({"error": f"User with user_id '{target_user_id}' not found."}), 404
    
    
@app.route('/status/changeEquipment', methods=['POST'])
def change_equipment():
    target_user_id = request.args.get('userID')
    target_equip_id = int(request.args.get('equipID'))
   
    
    # user_id가 제공되지 않았을 경우 에러 응답
    if not target_user_id:
        return jsonify({"error": "No user_id provided."}), 400
    
    # user_id가 제공되지 않았을 경우 에러 응답
    if not target_equip_id:
        return jsonify({"error": "No target_equip_id provided."}), 400
    
    # 특정 user 객체를 찾음
    target_user = find_user_by_id(target_user_id)
    
    # user가 존재하지 않는 경우 에러 응답
    if not target_user:
        return jsonify({"error": f"User with user_id '{target_user_id}' not found."}), 404
    
    # target_equip_id에 해당하는 아이템을 찾음
    item = target_user.get_item_by_id(target_equip_id)
    
    # 아이템이 존재하지 않는 경우 에러 응답
    if not item:
        return jsonify({"error": f"Item with ID '{target_equip_id}' not found in user's inventory."}), 404
    
    print(target_user.equipped_item)
    target_user.set_equipped_item(target_equip_id)
    print(target_user.equipped_item)
    
    return jsonify({"status": 0})


@app.route('/login/create', methods=['GET'])
def create_account():
    global user_list
    # userID = request.args.get('userID')
    random_ints = random_generator(1, 100000000000, 1)
    user1 = User(user_id=random_ints, level=1, registered_amount=540.0, equipped_weapon=1, equipped_armor=10)
    print(user_list)

    user_list.append(user1)

    print(user_list)

    data = {
        "userID": random_ints
    }
    return jsonify(data)




if __name__ == '__main__':
    app.run(host='192.168.0.37',debug=True, use_reloader=False)
    


