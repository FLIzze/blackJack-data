from flask import Flask, jsonify
from api_func import get_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(data=get_data()):
    return jsonify({'message': data}), 200


if __name__ == '__main__':
    app.run(debug=False)