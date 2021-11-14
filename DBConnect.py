import json
import mysql.connector


def getConnection():
    db = mysql.connector.connect(
        host="localhost",
        user='root',
        password='admin',
        database='radio_online',
        auth_plugin='mysql_native_password'
    )
    return db
