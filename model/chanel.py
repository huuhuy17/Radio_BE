import json
from Db_Connect import getConnect
import mysql.connector


class Chanel:
    id = 0;
    chanelName = ''
    theLoai = ''
    Url = ''

    def __init__(self, id, chanelName, theLoai, Url):
        self.id = id
        self.chanelName = chanelName
        self.theLoai = theLoai
        self.Url = Url

    def getChanel(self):
        myConnect = getConnect()
        myQuery = 'SELECT * FROM radio.chanel'
        cusor = myConnect.cursor()
        cusor.execute(myQuery)
        ar = []
        record = cusor.fetchall()
        for item in record:
            chanel = {
                "id": item[0],
                'chanel_name': item[1],
                'idthe_loai': item[2],
                'Url': item[3],
            }
            ar.append(chanel)
        myConnect.close()
        cusor.close()
        list = {"chanel": ar}
        return json.dumps(list)

    def getChanelByTheloai(self, id):
        myConnect = getConnect()
        myQuery = 'select * from radio.chanel inner join  radio.theloai on idtheLoai = id_theloai where id_theloai = %s'
        cusor = myConnect.cursor()
        cusor.execute(myQuery, (id,))
        ar = []
        record = cusor.fetchall()
        for item in record:
            chanel = {
                "id": item[0],
                'chanel_name': item[1],
                'idthe_loai': item[2],
                'Url': item[3],
            }
            ar.append(chanel)
        myConnect.close()
        cusor.close()
        list = {"chanelbyTl": ar}
        return json.dumps(list)

    def xoaChanel(self, id):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'delete from radio.chanel where id like  %s'
        c.execute(sql, (id,))
        db.commit()
        return str("đã xóa chanel")

    def editChanel(self, id, name, idTl, Url):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'UPDATE radio.chanel SET chanel_name = %s, idtheLoai = %s, Url= %s WHERE id like %s;'
        c.execute(sql, (name, idTl, Url, id))
        db.commit()
        return str("đã sửa kênh")

    def insertChanel(self, chanelName, idtheLoai, Url):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'INSERT INTO radio.chanel (chanel_name, idtheLoai, Url) VALUE (%s, %s, %s)'
        val = (chanelName, idtheLoai, Url)
        c.execute(sql, val)
        db.commit()
        return str(c.rowcount)
