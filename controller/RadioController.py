from model.AccountModel import Account, Channel
from flask import Flask, json, request


def login_radio_app(username, password):
    auth = Account(0, username, password, 0)
    return auth.login()


