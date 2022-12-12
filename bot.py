from requests import *
from config import *
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Bot():
    def __init__(self):
        self.url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
        self.account_sid = account_sidd
        self.auth_token = auth_tokenn
        url_2 = self.url.json()
        self.nome_dollar = url_2['USDBRL']['name']
        self.dollar = url_2['USDBRL']['bid']
        self.nome_euro = url_2['EURBRL']['name']
        self.euro = url_2['EURBRL']['bid']
        self.nome_btc = url_2['BTCBRL']['name']
        self.btc = url_2['BTCBRL']['bid']
    
    def email2(self):
        host = 'smtp-mail.outlook.com'
        port = 587
        user = User
        password = Password
        # Criando objeto servidor
        server = smtplib.SMTP(host, port)

        # Login com servidor
        server.ehlo()
        server.starttls()
        server.login(user, password)

        # Criando mensagem
        message_html = f"""
                            <p>Olá!<br>
                            <p>Aqui é o Bot de acompanhamento de cotações do dolar...</p>
                            <p>O Valor do {self.nome_dollar} neste momento é de  R${self.dollar}</p></br>
                            <p>O Valor do {self.nome_euro} neste momento é de  R${self.euro}</p></br>
                            <p>O Valor do {self.nome_btc} neste momento é de  R${self.btc}</p></br>
                            <p>Bons investimentos,</p></br> 
                            <p>Abs,</p>
                            <p>Fabio</p><br>
                            Aqui vai um <a href="https://www.linkedin.com/in/fabiomarquesarao/">link do meu perfil do Linkedin</a> Te espero lá..
                            </p>
                        
                        """
        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = 'fabinhoarao@gmail.com'
        email_msg['Subject'] = 'Api de coleta de cotações Dollar, Euro, BitCoin'
        email_msg.attach(MIMEText(message_html, 'html'))
        #email_msg.attach(MIMEText(message, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()
    
    def email_error(self):
        host = 'smtp-mail.outlook.com'
        port = 587
        user = User
        password = Password
        # Criando objeto servidor
        server = smtplib.SMTP(host, port)

        # Login com servidor
        server.ehlo()
        server.starttls()
        server.login(user, password)

        # Criando mensagem
        message_html = f"""
                            <p>Olá!<br>
                            <p>Aqui é o Bot de acompanhamento de cotações do dolar...</p></br></br>
                            <p>Ocorreu algum erro na coleta dos dados...</p>
                            </p>
                        
                        """
        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = 'fabinhoarao@gmail.com'
        email_msg['Subject'] = 'Erro na Coleta!!'
        email_msg.attach(MIMEText(message_html, 'html'))
        #email_msg.attach(MIMEText(message, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()

    def send_txt(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                        .create(
                            body = f"""-\nO Valor do {self.nome_dollar} neste momento é de R${self.dollar},\n\nO Valor do  {self.nome_euro} neste momento é de  R${self.euro},\n\nO Valor do {self.nome_btc} neste momento é de  R${self.btc} ,\n\nBons investimentos....\n\nFabio.""",
                            from_= fromm,
                            to = too
                        )

    def log(self):
        print(self.nome_dollar, "Neste momento...", self.dollar)
        print(self.nome_euro, "Neste momento...", self.euro)
        print(self.nome_btc, "Neste momento...", self.btc)
   