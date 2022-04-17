from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import functions
import pathlib
from pathlib import Path


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ROLES_PATH = Path(pathlib.Path.cwd(), 'data_json', 'roles.json')
ORDERS_PATH = Path(pathlib.Path.cwd(), 'data_json', 'orders.json')
USERS_PATH = Path(pathlib.Path.cwd(), 'data_json', 'users.json')
OFFERS_PATH = Path(pathlib.Path.cwd(), 'data_json', 'offers.json')

db = SQLAlchemy(app)
db.init_app(app)


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
    offers = relationship("Offer")
    orders = relationship("Order")


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

    users = relationship("User")


class Offer(db.Model):
    __tablename__ = "offers"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = relationship("User")
    orders = relationship("Order")


db.create_all()

with app.app_context():
    roles_data = functions.add_data(ROLES_PATH)


if __name__ == "__main__":
    app.run(debug=True)
