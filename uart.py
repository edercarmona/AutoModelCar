import os
import serial
class UART:    
    alive = False
    def __init__(self):
        try:
            self.port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
            #self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
            self.alive = True
        except:
            self.alive = False
            print("Imposible Inicializar UART")
    
    def control(self, num):
        cmd = str(num)
        self.port.write(cmd.encode())
        try:
            rcv=self.port.read(15)
        except:
            print("UART Lost conection!!!")        