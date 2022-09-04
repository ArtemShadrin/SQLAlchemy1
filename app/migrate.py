import json
from app.models import model_users, model_orders, model_offers
from app import db


def load_data(filename):
    """
    функция для загрузки данных
    """
    json_data = []
    with open(filename, encoding="utf-8") as file:  # получаем данные
        json_data = json.load(file)  # преобразуем их

    return json_data


def load_user(filename):
    """
    загрузка пользователей
    """
    users = load_data(filename)

    for user in users:
        new_user = model_users.User(**user)  # делаем распаковку автоматически
        db.session.add(new_user)

    db.session.commit()


def load_order(filename):
    """
    загрузка order
    """
    orders = load_data(filename)

    for order in orders:
        new_order = model_orders.Order(**order)  # делаем распаковку автоматически
        db.session.add(new_order)

    db.session.commit()



def load_offer(filename):
    """
    загрузка offer
    """
    offers = load_data(filename)

    for offer in offers:
        new_offer = model_offers.Offer(**offer)  # делаем распаковку автоматически
        db.session.add(new_offer)

    db.session.commit()
