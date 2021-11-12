import json
import mysql.connector
from Db_Connect import getConnect


class HistoryListen():
    id = 0
    id_user = ''
    id_chanel = ''

    def __init__(self, id, idUser, idChanel):
        self.id = id
        self.id_user = idUser
        self.id_chanel = idChanel

    def creatHistory(self, idUser, idChanel):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            auth_plugin='mysql_native_password'
        )
        c = db.cursor()
        sql = 'INSERT INTO radio.lichsunghe (id_user, id_chanel) VALUE (%s, %s)'
        val = (idUser, idChanel)
        c.execute(sql, val)
        db.commit()
        return str(c.rowcount)

    def getAllHistory(self, id):
        myConnect = getConnect()
        myQuery = 'SELECT * FROM radio.chanel inner join radio.lichsunghe on id = id_chanel where id_user like  %s'
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
        list = {"chanel_history": ar}
        return json.dumps(list)
