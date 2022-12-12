from bot import Bot
from rocketry import Rocketry



app = Rocketry()

@app.task('every 1 hour') #Rodará a aplicação a cada hora
class aplication():
    def __init__(self):
        self.bot = Bot()
        try:
            self.bot.email2()
            self.bot.send_txt()
            self.bot.log()
        except:
            self.bot.email_error()




if __name__ == "__main__":
    app.run()