import serial

class arduino:

    def __init__(self):
        self.conection = serial.Serial('COM8', 9600)

    def led(self, num):
        self.conection.write(num.encode())