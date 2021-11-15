import json
import mysql.connector


def getConnection():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user='root',
        password='admin',
        database='radio_online',
        auth_plugin='mysql_native_password'
    )
    return db
