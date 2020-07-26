# -*- coding: utf-8 -*-
"""
Created on Sat, Jul 18 09:03:34 2020
@author: TejYadav
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

store = [
    {
     "name": "My Wonderful Store",
     "items":[
             {
             "name": "My Item",
             "price": 15.99
             }
         ]
     }
 ]

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
        }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
             return jsonify(store)
    return jsonify({'message': 'store not found'})
    

# GET /store 
@app.route('/store')
def get_stores():
    return jsonify({'store': store})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'message': 'store not found'})
            

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})
            

app.run(port=5000)
