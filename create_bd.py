import sqlite3

with sqlite3.connect("my_test.sqlite") as connection:
    cursor = connection.cursor()
