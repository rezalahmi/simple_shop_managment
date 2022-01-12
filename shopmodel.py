import sqlite3 as db
from sqlite3 import Error


class MoDel:
    def __init__(self):
        self.dbName = 'shopManagement.db'
        self.sqlite_create_item_query = '''CREATE TABLE item (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        price INTEGER NOT NULL UNIQUE,
                                        stock INTEGER NOT NULL);'''

        self.sqlite_create_sell_query = '''CREATE TABLE sell (
                                        id INTEGER PRIMARY KEY,
                                        date TEXT NOT NULL,
                                        item_id INTEGER,
                                        quantity INTEGER NOT NULL,
                                        order_type INTEGER NOT NULL, 
                                        FOREIGN KEY(item_id) REFERENCES item(id));'''
        self.sqlite_update_price_stock = ''' UPDATE item
                                            SET price = ? ,
                                                stock = ? ,
                                            WHERE id = ?'''
        self.sqlite_insert_item = ''' INSERT INTO item(id,name,price,stock) 
                                        VALUES(?,?,?,?) '''
        self.sqlite_insert_sell = ''' INSERT INTO sell(id,date,item_id,quantity,order_type)
                                        VALUES(?,?,?,?,?) '''

    def connection(self):
        """
        create connection to sqlite3 Database
        :return: connection
        """
        sqliteConnection = ''
        try:
            sqliteConnection = db.connect(self.dbName)
            print("Successfully Connected to SQLite")
        except Error as error:
            print("Error while executing sqlite script", error)

        return sqliteConnection
    def createTable(self, sqlCon, create_table_query):
        """
        create Table on DataBase
        :param sqlCon: sqlite3 connection
        :param create_table_query: sql query to create table
        :return: return value show the result of query
        """
        try:
            cursor = sqlCon.cursor()
            cursor.execute(create_table_query)
            sqlCon.commit()
            return 1
        except Error as error:
            print('Error while executing create table query', error)
            return 0
    def insertToTable(self, sqlCon, insert_table_query, value):
        """
        insert data to table
        :param sqlCon: sqlite3 connection
        :param insert_table_query: insert query
        :param value: the tuple contain value for insert
        :return: result of sql command
        """
        try:
            cursor = sqlCon.cursor()
            cursor.execute(insert_table_query, value)
            sqlCon.commit()
            return cursor.lastrowid
        except Error as error:
            print('Error while executing insert query', error)
            return 0
    def reportFinishedItem(self, sqlcon):
        """
        report items that have finished in the store
        :param sqlcon: sqlite connection
        :return: query result
        """
        try:
            cursor = sqlcon.cursor()
            cursor.execute('''select * from item where stock==0''')
            return cursor.fetchall()
        except Error as error:
            print('Error while executing sql query', error)
            return -1
    def reportReturenItem(self, sqlcon):
        """
        report items that have been returned in the store
        :param sqlcon: sqlite connection
        :return: query result
        """
        try:
            cursor = sqlcon.cursor()
            cursor.execute('''select * from sell where order_type==0''')
            return cursor.fetchall()
        except Error as error:
            print('Error while executing sql query', error)
            return -1
    def reportSoldItem(self, sqlcon, date):
        """
        report items that have been sold at a determined date in the store
        :param sqlcon: sqlite connection
        :param date: determined date
        :return: query result
        """
        try:
            cursor = sqlcon.cursor()
            cursor.execute('''select * from sell where order_type==1 and date == ?''', (date,))
            return cursor.fetchall()
        except Error as error:
            print(error)
            return -1
    def updateItemPriceStock(self, sqlcon, update_item_price_stock, newStock):
        """
        update the stock value of an item
        :param sqlcon: sqlite connection
        :param update_item_price_stock: update query
        :param newStock: the tuple contain new price and stock
        :return: result of query
        """
        try:
            cursor = sqlcon.cursor()
            cursor.execute(update_item_price_stock, newStock)
            sqlcon.commit()
            return cursor.lastrowid
        except Error as error:
            print(error)
            return -1




