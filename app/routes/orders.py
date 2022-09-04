import json

from app.models import model_orders
from app import db  # импортируем наши модели
from flask import current_app as app, request, jsonify  # обращаемся к текущему приложению (current_app - "текущее")


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        result = []
        for order in model_orders.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        order_data = json.loads(request.data)
        new_order = model_orders.Order(**order_data)

        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in model_orders.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result), 200


@app.route('/orders/<int:oid>', methods=['GET', 'POST', 'DELETE'])
def order_function(oid):
    if request.method == 'GET':
        order = model_orders.Order.query.get(oid)
        return jsonify(order.to_dict()), 200
    if request.method == 'PUT':  # должен содержать все поля в текущей модели
        order_data = request.json
        order = model_orders.Order.query.get(oid)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']

        db.session.add(order)
        db.session.commit()

        order = model_orders.Order.query.get(oid)
        return jsonify(order.to_dict()), 200

    if request.method == 'DELETE':
        order = model_orders.Order.query.get(oid)
        db.session.delete(order)
        db.session.commit()

        return "", 204