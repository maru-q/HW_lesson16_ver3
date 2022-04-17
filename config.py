import os.path


DATABASE_FILE_PATH = os.path.join(os.getcwd(), "my_test.db")
DATA_JSON_DIR = "data_json"


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROLES_FILE_PATH = os.path.join(DATA_JSON_DIR, "roles.json")
    ORDERS_FILE_PATH = os.path.join(DATA_JSON_DIR, "orders.json")
    USERS_FILE_PATH = os.path.join(DATA_JSON_DIR, "users.json")
    OFFERS_FILE_PATH = os.path.join(DATA_JSON_DIR, "offers.json")
    