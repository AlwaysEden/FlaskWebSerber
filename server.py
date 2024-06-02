from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # 반환할 데이터
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland"
    }
    # jsonify 함수를 사용하여 JSON 응답 생성
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

