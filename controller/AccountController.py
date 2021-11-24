from model.AccountModel import Account


def login_radio_app(username, password):
    auth = Account(username, password)
    return auth.login()
