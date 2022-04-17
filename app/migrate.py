import os
import json
from app import db, models

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


def add_data_roles(file_path):
    role_list = load_data(file_path)

    for data in role_list:
        new_role = models.Role(**data)
        db.session.add(new_role)

    db.session.commit()
