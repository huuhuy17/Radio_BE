import json
import mysql.connector
from Db_Connect import getConnect


class ChanelFavor():
    id = 0
    ic_acc = ''
    id_chanel = ''

    def __init__(self, id, id_acc, id_chanel):
        self.id = id
        self.ic_acc = id_acc
        self.id_chanel = id_chanel

    def create_chanel_yt(self, id_acc, id_chanel):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'INSERT INTO radio.kenhyeuthich (id_user, id_chanel) VALUE (%s, %s)'
        val = (id_acc, id_chanel)
        c.execute(sql, val)
        db.commit()
        return str(c.rowcount)

    def detele_chanel_yt(self, id):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'DELETE FROM radio.kenhyeuthich WHERE id_chanel like %s;'
        c.execute(sql, (id,))
        db.commit()
        return str("đã xóa chanelyt")

    def getChanelYt(self, idUser):
        myConnect = getConnect()
        myQuery = 'SELECT * FROM radio.chanel inner join radio.kenhyeuthich on id = id_chanel where id_user like %s'
        cusor = myConnect.cursor()
        cusor.execute(myQuery, (idUser,))
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
        list = {"ChanelYT": ar}
        return json.dumps(list)
