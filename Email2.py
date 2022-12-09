# Import smtplib for the actual sending function
import smtplib
from config import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email2():
    def __init__(self, nome_dollar, dollar, nome_euro, euro, nome_btc, btc):
  
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

                            <p>O Valor do {nome_dollar} neste momento é de  R${dollar}</p></br>
                            <p>O Valor do {nome_euro} neste momento é de  R${euro}</p></br>
                            <p>O Valor do {nome_btc} neste momento é de  R${btc}</p></br>
                            
                            <p>Bons investimentos,</p></br> 
                            <p>Abs,</p>
                            <p>Fabio</p><br>
                            Aqui vai um <a href="https://docs.awesomeapi.com.br/api-de-moedas">link</a> que talvez você goste.
                            </p>
                        
                        """

        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = 'fabinhoarao@gmail.com; diego.norato@turn2c.com; bruno.duarte@turn2c.com'
        email_msg['Subject'] = 'Api de coleta de cotações Dollar, Euro, BitCoin'

        email_msg.attach(MIMEText(message_html, 'html'))
        #email_msg.attach(MIMEText(message, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()


