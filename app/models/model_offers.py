from sqlalchemy import ForeignKey

from app import db  # потому что бд в init, мы можем вызвать ее так ("." значит из текущего каталога)


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, ForeignKey("user.id"))

    order = db.relationship("Order")
    user = db.relationship("User")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }