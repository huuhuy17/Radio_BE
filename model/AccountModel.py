from DBConnect import getConnection
import datetime
import json


class Account:
    username = ''
    pass_word = ''

    def __init__(self, user, pass_word):
        self.username = user
        self.pass_word = pass_word

    def login(self):
        myConnect = getConnection()
        cursor = myConnect.cursor()
        cursor.execute("SELECT * FROM radio_online.account WHERE username like %s and password like %s",
                       (self.username, self.pass_word))
        record = cursor.fetchone()
        if record is not None:
            item = {
                'id': record[0],
                'username': record[1],
                'password': record[2],
                'acc_type': record[3]
            }
            myConnect.close()
            cursor.close()
            return json.dumps(item)
        return json.dumps(None)


class Account1:
    def __init__(self, username, password, acc_type):
        self.username = username
        self.password = password
        self.acc_type = acc_type

    def add_acc(self):
        myConnect = getConnection()
        cursor = myConnect.cursor()
        query = "INSERT INTO radio_online.account (username, password, acc_type) values (%s, %s, %s)"
        cursor.execute(query, (self.username, self.password, self.acc_type))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps("DONE")

    def alter_account(self, acc_id):
        myConnect = getConnection()
        cursor = myConnect.cursor()
        cursor.execute("UPDATE radio_online.account SET username = %s, password = %s, acc_type = %s \
                        WHERE id_user = %s",
                       (self.username, self.password, self.acc_type, acc_id))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps("DONE")


def delete_acc(acc_id):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "DELETE FROM radio_online.account WHERE id_user = %s"
    cursor.execute(query, (acc_id,))
    myConnect.commit()
    myConnect.close()
    cursor.close()
    return json.dumps("DONE")


def show_radio():
    myConnect = getConnection()
    cursor = myConnect.cursor()
    cursor.execute("SELECT * FROM radio_online.radio_channel")
    array = []
    for item in cursor.fetchall():
        data = {
            'icon': item[0],
            'name': item[1],
            'link': item[2],
            'type': item[3],
            'id_channel': item[4]
        }
        array.append(data)
    data_channel = {
        'channel': array
    }
    myConnect.close()
    cursor.close()
    return json.dumps(data_channel)


def show_favorite_channel(id_user):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "SELECT radio_channel.icon, radio_channel.channel_name, radio_channel.link, radio_channel.c_type\
                    from radio_channel\
                    inner join favorite on favorite.id_channel = radio_channel.id_channel\
                    where favorite.id_user like %s"
    cursor.execute(query, (id_user,))
    array = []
    for item in cursor.fetchall():
        data = {
            'icon': item[0],
            'name': item[1],
            'link': item[2],
            'type': item[3]
        }
        array.append(data)
    data_channel = {
        'channel': array
    }
    myConnect.close()
    cursor.close()
    return json.dumps(data_channel)


def get_channel_audio(name):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "SELECT link FROM radio_online.radio_channel WHERE channel_name = %s"
    cursor.execute(query, (name,))
    item = cursor.fetchone()
    myConnect.close()
    cursor.close()
    return json.dumps(item)


def show_acc():
    myConnect = getConnection()
    cursor = myConnect.cursor()
    cursor.execute("SELECT * FROM radio_online.account")
    array = []
    for item in cursor.fetchall():
        data = {
            'id': item[0],
            'username': item[1],
            'pass': item[2],
            'acc_type': item[3]
        }
        array.append(data)
    data_account = {
        'account': array
    }
    myConnect.close()
    cursor.close()
    return json.dumps(data_account)


def delete_channel(name):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "DELETE FROM radio_online.radio_channel cc WHERE cc.channel_name like %s"
    cursor.execute(query, (name,))
    myConnect.commit()
    myConnect.close()
    cursor.close()
    return json.dumps("DONE")


def add_fvr_channel(id_user, id_channel):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "SELECT liked FROM `radio_online`.`favorite` WHERE id_user like %s AND id_channel like %s"
    cursor.execute(query, (id_user, id_channel,))
    arr = []
    for item in cursor.fetchall():
        data = {
            'liked': item[0]
        }
        arr.append(data['liked'])
    print(arr)
    if len(arr) > 0:
        tmp = '0'
        myConnect.close()
        cursor.close()
        myConnect = getConnection()
        cursor = myConnect.cursor()
        query = "DELETE FROM `radio_online`.`favorite` WHERE id_user like %s and id_channel like %s;"
        cursor.execute(query, (id_user, id_channel,))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps(tmp)
    else:
        tmp = '1'
        myConnect.close()
        cursor.close()
        myConnect = getConnection()
        cursor = myConnect.cursor()
        query = "INSERT INTO `radio_online`.`favorite`(id_user, id_channel, liked) VALUES (%s, %s, %s)"
        cursor.execute(query, (id_user, id_channel, tmp))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps(tmp)


def add_to_history(id_user, id_channel):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "INSERT INTO radio_online.history ( id_user, id_channel, time) VALUES (%s, %s, now());"
    cursor.execute(query, (id_user, id_channel,))
    myConnect.commit()
    myConnect.close()
    cursor.close()
    return json.dumps("DONE")


def get_history(id_user):
    myConnect = getConnection()
    cursor = myConnect.cursor()
    query = "select distinct radio_channel.channel_name, history.time from account\
                inner join history on history.id_user like %s\
                inner join radio_channel on history.id_channel = radio_channel.id_channel"
    cursor.execute(query, (id_user,))
    arr = []
    for item in cursor.fetchall():
        data = {
            'channel_name': item[0],
            'time': item[1]
        }
        arr.append(data)

    def default(obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

    data_channel = {
        'channel': arr
    }
    myConnect.close()
    cursor.close()
    return json.dumps(data_channel, default=default)


class Channel:
    def __init__(self, icon, name, link, new_type):
        self.icon = icon
        self.name = name
        self.link = link
        self.type = new_type

    def add_channel(self):
        myConnect = getConnection()
        cursor = myConnect.cursor()
        cursor.execute(
            "INSERT INTO radio_online.radio_channel (icon, channel_name, link, c_type) values (%s, %s, %s, %s)",
            (self.icon, self.name, self.link, self.type))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps("DONE")

    def alter_channel(self, old_name):
        myConnect = getConnection()
        cursor = myConnect.cursor()
        cursor.execute("UPDATE radio_online.radio_channel SET icon = %s, channel_name = %s, link = %s, c_type = %s \
                        WHERE channel_name = %s",
                       (self.icon, self.name, self.link, self.type, old_name))
        myConnect.commit()
        myConnect.close()
        cursor.close()
        return json.dumps("DONE")
