from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # база данных


def create_app():
    """
    возвращает собственное приложение
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # подключение бд из memory
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # удаляем warming

    with app.app_context():  # задаем задачи в контексте приложения
        db.init_app(app)  # инициализируем нашу БД
        from app.routes import user, orders, offers  # и импортируем route
        db.create_all()  # создаем таблицы
        from app import migrate
        migrate.load_user('data/users.json')
        migrate.load_order('data/orders.json')
        migrate.load_offer('data/offers.json')

    return app
