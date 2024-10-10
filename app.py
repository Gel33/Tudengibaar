from flask import Flask, render_template, request, jsonify
from api.joogid import drinks  # Importing drink data
from api.algorithm import adjust_price  # Importing price adjustment logic
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('baar.html', drinks=drinks)

@app.route('/hinnad')
def price_list():
    return render_template('hinnad.html', drinks=drinks)

@app.route('/update_sales', methods=['POST'])
def update_sales():
    drink_name = request.json['drink_name']
    for drink in drinks:
        if drink['name'] == drink_name:
            drink['sales_count'] += 1
            adjust_price(drink, drinks)  # Pass the entire drinks list
            return jsonify(success=True, price=drink['current_price'])
    return jsonify(success=False)

@app.route('/get_prices')
def get_prices():
    # Simulating price changes over time
    price_changes = [{"name": drink["name"], "price": drink["current_price"]} for drink in drinks]
    return jsonify(price_changes)

@app.route('/api/drinks', methods=['GET'])
def get_drinks():
    return jsonify(drinks)

if __name__ == '__main__':
    app.run(debug=True)
