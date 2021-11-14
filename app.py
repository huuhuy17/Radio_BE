from flask import Flask, json, request
from flask_cors import CORS
import controller.AccountController
import controller.RadioController
from model.AccountModel import show_radio, show_acc, Channel, delete_channel, Account1, delete_acc, add_fvr_channel, \
    get_channel_audio, add_to_history , get_history, show_favorite_channel

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/login', methods=["GET", "POST"])
def login_radio_app():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    s = controller.AccountController.login_radio_app(username, password)
    return s


@app.route('/showChannel', methods=["GET", "POST"])
def showChannel():
    return show_radio()


@app.route('/showFavoriteChannel', methods=['GET', 'POST'])
def showFavoriteChannel():
    data = request.json
    id_user = data.get('id_user')
    return show_favorite_channel(id_user)


@app.route('/showAccounts', methods=["GET", "POST"])
def showAccounts():
    return show_acc()


@app.route('/deleteChannel', methods=["GET", "POST"])
def deleteChannel():
    data = request.json
    name = data.get('channel_name')
    return delete_channel(name)


@app.route('/addChannel', methods=["GET", "POST"])
def addChannel():
    data = request.json
    c_name = data.get('c_name')
    c_icon = data.get('c_icon')
    c_link = data.get('c_link')
    c_type = data.get('c.type')
    channel = Channel(c_icon, c_name, c_link, c_type)
    return channel.add_channel()


@app.route('/addFavoriteChannel', methods=['GET', "POST"])
def addFavoriteChannel():
    data = request.json
    id_user = data.get('id_user')
    id_channel = data.get('id_channel')
    return add_fvr_channel(id_user, id_channel)


@app.route('/addToHistory', methods=['GET', 'POST'])
def addToHistory():
    data = request.json
    id_user = data.get('id_user')
    id_channel = data.get('id_channel')
    return add_to_history(id_user, id_channel)


@app.route('/getHistory', methods=['GET', "POST"])
def getHistory():
    data = request.json
    id_user = data.get('id_user')
    return get_history(id_user)


@app.route('/alterChannel', methods=["GET", "POST"])
def alterChannel():
    data = request.json
    old_name = data.get('old_name')
    new_name = data.get('new_name')
    new_icon = data.get('new_icon')
    new_link = data.get('new_link')
    new_type = data.get('new_type')
    channel = Channel(new_icon, new_name, new_link, new_type)
    return channel.alter_channel(old_name)


@app.route('/addAccount', methods=["GET", "POST"])
def addAccount():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    acc_type = data.get("acc_type")
    tmp = Account1(username, password, acc_type)
    return tmp.add_acc()


@app.route('/deleteAccount', methods=['GET', 'POST'])
def delAccount():
    data = request.json
    acc_id = data.get('id')
    return delete_acc(acc_id)


@app.route('/alterAccount', methods=['GET', 'POST'])
def alterAccount():
    data = request.json
    old = data.get('id')
    new_name = data.get('new_name')
    new_pass = data.get('new_pass')
    new_type = data.get('new_type')
    channel = Account1(new_name, new_pass, new_type)
    return channel.alter_account(old)


@app.route('/getAudio', methods=['GET', 'POST'])
def getAudio():
    data = request.json
    name = data.get('c_name')
    return get_channel_audio(name)


if __name__ == "__main__":
    app.run()
