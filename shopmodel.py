import sqlite3 as db
from sqlite3 import Error


class MoDel:
    def __init__(self):
        self.dbName = 'shopManagement.db'

    def connection(self):
        sqliteConnection = ''
        try:
            sqliteConnection = db.connect(self.dbName)
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
        except Error as error:
            print("Error while executing sqlite script", error)

        return sqliteConnection

    def createTable(self, con, create_table_query):
        try:
            cursor = con.cursor()
            cursor.execute(create_table_query)
            con.commit()
        except Error as error:
            print('Error while executing create table query', error)

myModel = MoDel()
con = myModel.connection()
sqlite_create_item_query = '''CREATE TABLE item (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price INTEGER NOT NULL UNIQUE,
                                stock INTEGER NOT NULL);'''

sqlite_create_sell_query = '''CREATE TABLE sell (
                                id INTEGER PRIMARY KEY,
                                date TEXT NOT NULL,
                                item_id INTEGER,
                                quantity INTEGER NOT NULL,
                                FOREIGN KEY(item_id) REFERENCES item(id));'''
sqlite_create_return_query = '''CREATE TABLE return (
                                id INTEGER PRIMARY KEY,
                                date TEXT NOT NULL,
                                item_id INTEGER,
                                quantity INTEGER NOT NULL,
                                FOREIGN KEY(item_id) REFERENCES item(id));'''
#myModel.createTable(con, sqlite_create_return_query)