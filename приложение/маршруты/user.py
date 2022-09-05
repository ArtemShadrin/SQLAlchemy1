import json

from app.models import model_users
from app import db  # импортируем наши модели
from flask import current_app as app, request, jsonify  # обращаемся к текущему приложению (current_app - "текущее")


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        result = []
        for user in model_users.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        user_data = json.loads(request.data)
        new_user = model_users.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in model_users.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def user_function(uid):
    if request.method == 'GET':
        user = model_users.User.query.get(uid)
        return jsonify(user.to_dict()), 200
    if request.method == 'PUT':  # должен содержать все поля в текущей модели
        user_data = request.json
        user = model_users.User.query.get(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = model_users.User.query.get(uid)
        return jsonify(user.to_dict()), 200

    if request.method == 'DELETE':
        user = model_users.User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "", 204
