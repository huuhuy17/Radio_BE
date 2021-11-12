import json
from Db_Connect import getConnect
import mysql.connector


class Account:
    id = 0
    username = ''
    password = ''
    email = ''
    quyen = ''

    def __init__(self, id, username, password, email, quyen):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.quyen = quyen

    def getAcc(self):
        myConnect = getConnect()
        myQuery = 'SELECT * FROM radio.account'
        cusor = myConnect.cursor()
        array = []
        cusor.execute(myQuery)
        record = cusor.fetchall()
        for item in record:
            acc = {
                "id": item[0],
                'username': item[1],
                'password': item[2],
                'email': item[3],
                'quyen': item[4]
            }
            array.append(acc)
        myConnect.close()
        cusor.close()
        list = {'Acc': array}
        return json.dumps(list)

    def signUp(self, username, password, email, quyen):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'INSERT INTO radio.account (username, password, email, quyen) VALUE (%s, %s, %s, %s)'
        val = (username, password, email, quyen)
        c.execute(sql, val)
        db.commit()
        return str(c.rowcount)

    def deteleAcc(self, id):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'delete from radio.account where id_acc like  %s'
        c.execute(sql, (id,))
        db.commit()
        return str("đã xóa")

    def editAcc(self, id, username, password, email, quyen):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'UPDATE radio.account SET username = %s, password = %s,email = %s, quyen = %s WHERE id_acc like  %s;'
        c.execute(sql, (username, password, email, quyen, id))
        db.commit()
        return str("đã sửa")

    def logIn(self, username, password):
        connect = getConnect()
        my_query = 'SELECT * FROM radio.account us where us.username like %s and us.password like %s'
        c = connect.cursor()
        c.execute(my_query, (username, password))
        r = c.fetchone()
        item = {
            'id': r[0],
            'username': r[1],
            'password': r[2],
            'quyen': r[4]
        }
        connect.close()
        c.close()
        return json.dumps(item)
