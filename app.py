from typing import KeysView
import requests
import json
from chalice import Chalice

app = Chalice(app_name='AWSlambda')

# API_KEY1 = 'PKFU4FZT9Z8047JFEYZ0'
# SECRET_KEY1 = 'vJ8pFUAvEl0kgnsuCSw8JMIWrofpiO12PJB4XkEN'
# BASE_URL = "https://psotlpgw85.execute-api.us-east-2.amazonaws.com/api/"
BASE_URL = "hhttp://127.0.0.1:8000"
# ORDERS_URL = "{}/v2/orders".format(BASE_URL)
# HEADERS = {'APCA-API-KEY-ID': API_KEY1, 'APCA-API-SECRET-KEY': SECRET_KEY1}

data = {}


@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
    # webhook_text.append(webhook_message)

    print(webhook_message)
    print(webhook_message.keys())
    print(webhook_message['ETH'])
    #

    datas = {
        'open': webhook_message['open'],
        'high': webhook_message['high'],
        'low': webhook_message['low'],
        'close': webhook_message['close'],
        'ticker': webhook_message['ticker'],
        'ETH': {
            'startShort': False,
            'startLong': False,
            'stopShort': False,
            'stopLong': False,
            'tp_percent': None,
            'last_candle': 'null',
            'sl_tries': 'null',
            'isOn': False,
            'LoseActive': 'null'
        }
    }

    for key in datas:
        data[key] = datas[key]
        print(key, "->", datas[key])
    # r = requests.post(BASE_URL, json=data)
    # response = json.loads(r.content)
    #

    with open('json.json', 'r', encoding='utf-8') as read_json:
        text = json.load(read_json)
        if(text != webhook_message):
            with open('json.json', 'w', encoding='utf-8') as outfile:
                json.dump(webhook_message, outfile)
                print("add")
        else:
            print("pass")

    return {
        'message': 'I bought the stock!',
        'webhook_messagese': data,
        # 'id': response['id'],

        # 'client_order_id': response['client_order_id'],
    }


@app.route('/')
def index():
    return {
        'Hello': 'world!',
        'message': 'I bought the stock!',
        'webhook_message': data
    }
# @app.route('/watchlist')
# def watchlist():
#     stream = {
#         "TWTR": [
#             "Twitter tweet 1", "Twitter tweet 2"
#         ],
#         "SQ": [
#             "Square tweet 1", "Square tweet 2"
#         ]
#     }
#     return {
#         'stream': stream
#     }


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
