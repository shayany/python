import pymysql
import dbconfig


class DBHelper():
    def connect(self, database="entertainment"):
        return pymysql.connect(host='localhost',
                               port=3306,
                               user=dbconfig.db_username,
                               passwd=dbconfig.db_password,
                               db='mysql')

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM entertainment.qsrs;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO entertainment.qsrs (description) VALUES ('%s');" % data
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM entertainment.qsrs;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
