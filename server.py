# from flask import Flask, jsonify
from datetime import datetime
from typing import List, Dict


# app = Flask(__name__)


class Level:
    def __init__(self, level_id: int, required_exp: int):
        self.id = level_id
        self.required_exp = required_exp

    def __repr__(self):
        return f"Level(id={self.id}, required_exp={self.required_exp})"

class Item:
    def __init__(self, item_id: int, amount: int):
        self.id = item_id
        self.amount = amount

    def __repr__(self):
        return f"Item(id={self.id}, amount={self.amount})"

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

    def set_equipped_item(self, item: Item):
        self.equipped_item = item

    def __repr__(self):
        return (f"User(user_id={self.user_id}, login_info={self.login_info}, registered_amount={self.registered_amount}, "
                f"items={self.items}, level={self.level}, equipped_item={self.equipped_item}, exp={self.exp}, gold={self.gold}, "
                f"last_connection={self.last_connection}, creation_time={self.creation_time})")

# 예제 사용
level1 = Level(level_id=1, required_exp=100)
item1 = Item(item_id=101, amount=2)
item2 = Item(item_id=102, amount=5)

user1 = User(user_id="user123", login_info="user123_login", registered_amount=50.0)
user1.add_item(item1)
user1.add_item(item2)
user1.set_level(level1)
user1.set_equipped_item(item1)
user1.exp = 150
user1.gold = 1000

print(user1)


# @app.route('/api/data', methods=['GET'])
# def get_data():
#     # 반환할 데이터
#     data = {
#         "name": "Alice",
#         "age": 30,
#         "city": "Wonderland"
#     }
#     # jsonify 함수를 사용하여 JSON 응답 생성
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
    


