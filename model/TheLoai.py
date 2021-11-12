import json
import mysql.connector
from Db_Connect import getConnect


class TheLoai():
    id_theloai = 0
    tenTheloai = ''

    def __init__(self, id, tenTL):
        self.id_theloai = id
        self.tenTheloai = tenTL

    def addTheLoai(self, tenTheloai):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = "INSERT INTO radio.theloai (tenTheloai) VALUE (%s)"""
        c.execute(sql, (tenTheloai,))
        db.commit()
        return str(c.rowcount)

    def getTheLoai(self):
        myConnect = getConnect()
        myQuery = 'SELECT * FROM radio.theloai'
        cusor = myConnect.cursor()
        cusor.execute(myQuery)
        ar = []
        record = cusor.fetchall()
        for item in record:
            chanel = {
                "id": item[0],
                'TenTheLoai': item[1]
            }
            ar.append(chanel)
        myConnect.close()
        cusor.close()
        list = {"TheLoai": ar}
        return json.dumps(list)
