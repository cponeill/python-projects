#Use 21.co micropayments to create a disposable docker jail on a host system
#TODO: Add otpions to redirect to various local machines with different specs

import flask
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json
from flask import request
from random import randint
import subprocess

app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/ssh')
@payment.required(5000)
def ssh():
    user = ''
    passwd = ''
    chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    n = len(chars)-1
    for i in range(0,8):
        y = chars[randint(0,n)]
        user += str(y)
    for i in range(0,12):
        y = chars[randint(0,n)]
        passwd += str(y)
    subprocess.Popen(['sudo','addjail',user,passwd])
    return "Your login information:\nHost: 21.browntech.space\nPort: 2422\nUsername: {0}\nPassword: {1}".format(user,passwd)

@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7005)
