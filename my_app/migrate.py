import os
import json
import re
from datetime import datetime

from my_app import db, models

DATE_PATTERN = re.compile(r"\d{2}/\d{2}/\d{4}")


def load_data(file_path):
    """
    Получает данные из json
    :param file_path:
    :return: data
    """
    data = []
    if os.path.isfile(file_path):
        with open(file_path, encoding="utf8") as file:
            data = json.load(file)

    return data


def add_data_roles(file_path):
    role_list = load_data(file_path)

    for role in role_list:
        if db.session.query(models.UserRole).filter(models.UserRole.id == role["id"]).first() is None:
            new_role = models.UserRole(**role)
            db.session.add(new_role)

    db.session.commit()


def add_data_users(file_path):
    user_list = load_data(file_path)

    for user in user_list:
        if db.session.query(models.User).filter(models.User.id == user["id"]).first() is None:
            new_user = models.User(**user)
            db.session.add(new_user)

    db.session.commit()


def add_data_orders(file_path):
    order_list = load_data(file_path)

    for order in order_list:
        for field_name, field_value in order.items():
            if isinstance(field_value, str) and re.search(DATE_PATTERN, field_value):
                order[field_name] = datetime.strptime(field_value, "%m/%d/%Y").date()

        if db.session.query(models.Order).filter(models.Order.id == order["id"]).first() is None:
            new_order = models.Order(**order)
            db.session.add(new_order)

    db.session.commit()


def add_data_offers(file_path):
    offer_list = load_data(file_path)

    for offer in offer_list:
        if db.session.query(models.Offer).filter(models.Offer.id == offer["id"]).first() is None:
            new_offer = models.Offer(**offer)
            db.session.add(new_offer)

    db.session.commit()
