from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():

        from my_app import routes
        db.drop_all()
        db.create_all()

        from my_app import migrate

        migrate.add_data_roles(app.config["ROLES_FILE_PATH"])
        migrate.add_data_users(app.config["USERS_FILE_PATH"])
        migrate.add_data_orders(app.config["ORDERS_FILE_PATH"])
        migrate.add_data_offers(app.config["OFFERS_FILE_PATH"])


        return app


