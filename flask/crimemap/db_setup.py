import pymysql
import dbconfig
connection = pymysql.connect(host='localhost', port=3306, user=dbconfig.db_username, passwd=dbconfig.db_password, db='mysql')
try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10,6),
        longitude FLOAT(10,6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        updated_at TIMESTAMP,
        primary KEY (id)
        )"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
