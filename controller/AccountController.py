from model.AccountModel import Account, Channel


def login_radio_app(username, password):
    auth = Account(username, password)
    return auth.login()
