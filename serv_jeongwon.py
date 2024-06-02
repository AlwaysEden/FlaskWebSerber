from flask import Flask, jsonify, request
from datetime import datetime
from typing import List, Dict
from typing import Optional


app = Flask(__name__)

user_list = []

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
#level1 = Level(level_id=1, required_exp=100)
#item1 = Item(item_id=101, amount=2)
#item2 = Item(item_id=102, amount=5)

#user1 = User(user_id="user123", login_info="user123_login", registered_amount=50.0)
#user1.add_item(item1)
#user1.add_item(item2)
#user1.set_level(level1)
#user1.set_equipped_item(item1)
#user1.exp = 150
#user1.gold = 1000

#print(user1)

def find_user_by_id(user_list, target_id):
    for user in user_list:
        if user.user_id == target_id:
            return user
    return None

@app.route('/status/changeEquipment', methods=['POST']) 
def change_Equipment(): 
	userID = request.args.get('userID')
	equipID = request.args.get('equipID')
	#TODO: Search for user with userID
	data = {
		"": "Alice",
		"age": 30,
		"city": "Wonderland"
	}
	return jsonify(data)

@app.route('/status/inventory', methods=['GET']) #TODO: Search for user with userID
def get_inventory():
	userID = request.args.get('userID')

	item1 = Item(item_id=101, amount=2)
	item2 = Item(item_id=102, amount=5)

	user1 = User(user_id="user123", login_info="user123_login", registered_amount=50.0)
	user1.add_item(item1)
	user1.add_item(item2)
	user1.set_equipped_item(item1)
	user_list.append(user1)
	target_user = find_user_by_id(user_list, userID)
	if target_user:
		items_json = [{"amount": item.amount, "id": item.id} for item in target_user.items]
		data = {
			"item": items_json,
			"equipped_item": 0
		}
		return jsonify(data)
	else:
		return ({"error":"User not found"}),404


if __name__ == '__main__':
     app.run(debug=True)
    


