

<h1 align ="center "> Cotação de Moedas!!!</h1>


- A aplicação busca de hora em hora ou minuto a minuto a cotação das moedas escolhidas e manda um sms com as informações coletadas para o numero de celular programado e ou email escolhido.


## Referência
 - [awesomeapi](https://docs.awesomeapi.com.br/)

 - [Rocketry](https://rocketry.readthedocs.io/en/stable/)
 
 - [Twilio](https://www.twilio.com/pt-br/)
 
 - [smtplib](https://docs.python.org/3/library/smtplib.html)

 

## Apêndice
- O Bot utiliza como principal ferramenta a api [awesomeapi](https://docs.awesomeapi.com.br/), que faz a busca da cotação de ate 150 moedas diferentes... Em nosso caso utilizamos as moedas Dollar, Euro, e Bitcoin.
- Através do agendador de tarefas [Rocketry](https://rocketry.readthedocs.io/en/stable/) do próprio Python, podemos escolher a frequência que queremos executar a aplicação, no nosso caso de hora em hora, más o [Rocketry](https://rocketry.readthedocs.io/en/stable/) nos dá infinitas possibilidades de execussão. Confira a documentação em [Documentation Rocketry](https://rocketry.readthedocs.io/en/stable/).
- Utilizei a [Twilio](https://www.twilio.com/pt-br/) conta gratuita para fins de teste e atravéz dela, conseguimos enviar um sms com o valor da cotação obtido.
- O [smtplib](https://docs.python.org/3/library/smtplib.html) foi utilizado para enviar o email com as informações trazendo uma opção sem custo caso nao queira pagar a [Twilio](https://www.twilio.com/pt-br/) pelo envio de sms.

## Uso/Exemplos
#### Para funcionar você deverá adicionar suas credenciais Twilio e de email como descrito abaixo:
```Python
class Bot():
    def __init__(self):
        self.url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
        self.account_sid = ****SUA CHAVE TWILIO*****
        self.auth_token =  ****SEU TOKEN****


    def email2(self):
        host = 'smtp-mail.outlook.com'
        port = 587
        user = ****SEU USUÁRIO*****
        password = ****SUA SENHA*****
        # Criando objeto servidor
        server = smtplib.SMTP(host, port)
        ...

        email_msg = MIMEMultipart()
        email_msg['From'] = ****EMAIL QUE UTILIZARÁ PARA ENVIAR****
        email_msg['To'] = ****PARA QUEM QUER ENVIAR****
        email_msg['Subject'] = ****TITULO DA MENSAGEM****
        email_msg.attach(MIMEText(message_html, 'html'))
    
    def send_txt(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                        .create(
                            body = f""" MESAGEM """
                            from_= ****SEU NUMERO TWILIO****,
                            to = ****NUMERO QUE VAI RECEBER A MSG****
                        )

        

```
## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de fabinhoarao@gmail.com

