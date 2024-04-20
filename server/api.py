from flask import Flask, jsonify, request
from api_func import get_data, get_total_games_win_loss_push, get_best_choice, get_hand_stats
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index(data=get_data()):
    return jsonify({'data': data}), 200

@app.route('/total_games', methods=['GET'])
def total_games():
    data = get_total_games_win_loss_push()
    return jsonify({'total_games': data}), 200

@app.route('/best_choice', methods=['GET'])
def best_choice():
    data = get_best_choice()
    return jsonify({'best_choice': data}), 200

@app.route('/hand_stats', methods=['GET'])
def hand_stats():
    hand = [request.args.get('Card1'), request.args.get('Card2'), request.args.get('DealerHand')]
    return jsonify({'hand_stats': get_hand_stats(hand)}), 200


if __name__ == '__main__':
    app.run(debug=False)
