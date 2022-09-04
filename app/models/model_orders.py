from sqlalchemy import ForeignKey

from app import db  # потому что бд в init, мы можем вызвать ее так ("." значит из текущего каталога)


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)
    # Создаем внешние поля для связей между моделями
    customer_id = db.Column(db.Integer, ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, ForeignKey("user.id"))
    # Создаем интерфейсы для связей, указывая каждому внешние ключи
    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }
