import json

from app.models import model_offers
from app import db  # импортируем наши модели
from flask import current_app as app, request, jsonify  # обращаемся к текущему приложению (current_app - "текущее")


@app.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        result = []
        for offer in model_offers.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        offer_data = json.loads(request.data)
        new_offer = model_offers.Offer(**offer_data)

        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in model_offers.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result), 200


@app.route('/offers/<int:oid>', methods=['GET', 'PUT', 'DELETE'])
def offer_function(oid):
    if request.method == 'GET':
        offer = model_offers.Offer.query.get(oid)
        return jsonify(offer.to_dict()), 200
    if request.method == 'PUT':  # должен содержать все поля в текущей модели
        offer_data = request.json
        offer = model_offers.Offer.query.get(oid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = model_offers.Offer.query.get(oid)
        return jsonify(offer.to_dict()), 200

    if request.method == 'DELETE':
        offer = model_offers.Offer.query.get(oid)
        db.session.delete(offer)
        db.session.commit()

        return "", 204
