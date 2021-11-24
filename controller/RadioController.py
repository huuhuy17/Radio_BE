from model.AccountModel import Account


def login_radio_app(username, password):
    auth = Account(0, username, password, 0)
    return auth.login()


