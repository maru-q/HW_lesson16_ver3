from . import db
from sqlalchemy.orm import relationship


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    roles = relationship("User")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(255), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    phone = db.Column(db.String(16), unique=True)

    roles = relationship("Role")


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String)
    start_data_date = db.Column(db.Date, nullable=False)
    end_data_date = db.Column(db.Date, nullable=False)
    adress = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    customer = relationship("User", foreign_keys="Order.customer_id")
    executor = relationship("User",  foreign_keys="Order.executor_id")


class Offer(db.Model):
    __tablename__ = "offers"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = relationship("User")
    orders = relationship("Order")