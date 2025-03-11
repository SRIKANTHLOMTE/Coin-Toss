from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toss', methods=['GET'])
def toss_coin():
    # Generate either 0 or 1 randomly with equal probability
    # 0 = Heads, 1 = Tails
    result = random.randint(0, 1)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)