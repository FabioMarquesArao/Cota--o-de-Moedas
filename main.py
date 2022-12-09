from requests import *
import os
from Email import Email
from Email2 import Email2
from config import *
from twilio.rest import Client
from rocketry import Rocketry

app = Rocketry()

@app.task('minutely')
class aplication():
    def __init__(self):

        url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
        url_2 = url.json()
        nome_dollar = url_2['USDBRL']['name']
        dollar = url_2['USDBRL']['bid']

        nome_euro = url_2['EURBRL']['name']
        euro = url_2['EURBRL']['bid']

        nome_btc = url_2['BTCBRL']['name']
        btc = url_2['BTCBRL']['bid']

        Email2(nome_dollar, dollar, nome_euro, euro, nome_btc, btc)
        """ account_sid = account_sidd
        auth_token = auth_tokenn
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body = f'-----{nome}, Neste momento no valor de....R${dollar}',
                            from_= fromm,
                            to = too
                        )"""
        print(nome_dollar, "Neste momento...", dollar)
        print(nome_euro, "Neste momento...", euro)
        print(nome_btc, "Neste momento...", btc)




if __name__ == "__main__":
    app.run()
    #aplication()