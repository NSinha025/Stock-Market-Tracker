from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stock_chart', methods=['GET'])
def stock_chart():
    symbol = request.args.get('symbol')
    api_key = 'YOUR API'
    url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&apikey={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)

    values = data['values']
    x = [entry['datetime'] for entry in values]
    y = [entry['close'] for entry in values]
    chart_data = {'x': x, 'y': y}

    return jsonify(chart_data)


if __name__ == '__main__':
    app.run(debug=True)
