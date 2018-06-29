import telepot

class bot:

    def __init__(self):
        self.token = telepot.Bot(" ")

    def msg(self, msg):
        try:
            self.token.sendMessage( , msg)

        except Exception as ex:
            print(ex)

    def img(self, img):
        try:
            self.token.sendPhoto( , open(img, 'rb'))

        except Exception as ex:
            print(ex)
