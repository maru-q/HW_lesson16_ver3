import os
import json
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

from run import Role


def load_data(file_path):
    """
    Получает данные из json
    :param file_path:
    :return: data
    """
    data = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = json.load(file)

    return data


def add_data(file_path):
    data_list = load_data(file_path)
    db = SQLAlchemy(app)
    for data in data_list:
        new_role = Role(**data)
        db.session.add(new_role)

    db.session.commit()



