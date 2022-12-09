import win32com.client as win32


def Email(nome, dollar):

    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um email
    email = outlook.CreateItem(0)

    # configurar as informações do seu e-mail
    email.To = "fabinhoarao@gmail.com"
    email.Subject = "E-mail automático do Python"
    email.HTMLBody = f"""
    <p>Olá, aqui é o Bot de acompanhamento de cotações do dolar,</p>

    <p>O Valor do {nome} neste momento é de  R${dollar}</p>
    
    <p>Abs,</p>
    <p>Código Python</p>
    """

    # anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
    # email.Attachments.Add(anexo)

    email.Send()
    print("Email Enviado")