import flask
from flask import Flask, request
from flask_cors import CORS
import model.Account
from model.chanel import Chanel
import model.TheLoai
import model.ChanelFavor
import model.historyListen

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/addChanel', methods=['GET', 'POST'])
def createChanel():
    a = request.json
    chanel_name = a.get("chanel_name")
    idtheLoai = a.get("idtheLoai")
    Url = a.get("Url")
    data = Chanel.insertChanel(0, chanel_name, idtheLoai, Url)
    return data


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    a = request.json
    username = a.get("username")
    password = a.get('password')
    email = a.get('email')
    quyen = a.get('quyen')
    data = model.Account.Account.signUp(0, username, password, email, quyen)
    return data


@app.route('/logIn', methods=['GET', 'POST'])
def logIn():
    a = request.json
    username = a.get("username")
    password = a.get('password')
    data = model.Account.Account.logIn(0, username, password)
    return data


@app.route('/addtheloai', methods=['GET', 'POST'])
def theloai():
    a = request.json
    theloai = a.get("theloai")
    data = model.TheLoai.TheLoai.addTheLoai(0, theloai)
    return data


@app.route('/addchanelYT', methods=['GET', 'POST'])
def kenhYT():
    a = request.json
    id_user = a.get("id_user")
    id_chanel = a.get('id_chanel')
    data = model.ChanelFavor.ChanelFavor.create_chanel_yt(0, id_user, id_chanel)
    return data


@app.route('/addHistory', methods=['GET', 'POST'])
def kenhLs():
    a = request.json
    id_user = a.get("id_user")
    id_chanel = a.get('id_chanel')
    data = model.historyListen.HistoryListen.creatHistory(0, id_user, id_chanel)
    return data


@app.route('/xoaAcc', methods=['GET', 'POST'])
def xoaAcc():
    a = request.json
    id_user = a.get("idAcc")
    data = model.Account.Account.deteleAcc(0, id_user)
    return data


@app.route('/xoaChanel', methods=['GET', 'POST'])
def xoaChanel():
    a = request.json
    idChanel = a.get("idChanel")
    data = model.chanel.Chanel.xoaChanel(0, idChanel)
    return data


@app.route('/xoaChanelyt', methods=['GET', 'POST'])
def xoaChanelyt():
    a = request.json
    idChanel = a.get("idChanel")
    data = model.ChanelFavor.ChanelFavor.detele_chanel_yt(0, idChanel)
    return data


@app.route('/editChanel', methods=['GET', 'POST'])
def editChanel():
    a = request.json
    name = a.get("name")
    idtheloai = a.get("idtheloai")
    Url = a.get("Url")
    idChanel = a.get("idChanel")
    data = model.chanel.Chanel.editChanel(0, idChanel, name, idtheloai, Url)
    return data


@app.route('/editAcc', methods=['GET', 'POST'])
def editAcc():
    a = request.json
    user = a.get("username")
    passw = a.get("password")
    email = a.get("email")
    quyen = a.get("quyen")
    idAcc = a.get("idAcc")
    data = model.Account.Account.editAcc(0, idAcc, user, passw, email, quyen)
    return data


@app.route('/getchanelbytl', methods=['GET', 'POST'])
def getchanelbyTl():
    a = request.json
    idTl = a.get("idTl")
    data = model.chanel.Chanel.getChanelByTheloai(0, idTl)
    return data


@app.route('/getchanelYt', methods=['GET', 'POST'])
def getChanelYt():
    a = request.json
    idUser = a.get("idUser")
    data = model.ChanelFavor.ChanelFavor.getChanelYt(0, idUser)
    return data


@app.route('/getchanel', methods=['GET', 'POST'])
def getChanel():
    data = model.chanel.Chanel.getChanel(0)
    return data


@app.route('/getAcc', methods=['GET', 'POST'])
def getAcc():
    data = model.Account.Account.getAcc(0)
    return data


@app.route('/getTheloai', methods=['GET', 'POST'])
def getTheloai():
    data = model.TheLoai.TheLoai.getTheLoai(0)
    return data


@app.route('/getchanelhistory', methods=['GET', 'POST'])
def getHistory():
    a = request.json
    idUser = a.get("idUser")
    data = model.historyListen.HistoryListen.getAllHistory(0, idUser)
    return data


if __name__ == '__main__':
    app.run()
