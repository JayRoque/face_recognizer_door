import telepot

class bot:

    def __init__(self):
        self.token = telepot.Bot("516085535:AAHhUYJPdnX96_L17ysCYI23g47HuRH1-gg")

    def msg(self, msg):
        try:
            self.token.sendMessage(131443674, msg)

        except Exception as ex:
            print(ex)

    def img(self, img):
        try:
            self.token.sendPhoto(131443674, open(img, 'rb'))

        except Exception as ex:
            print(ex)