import os
import serial
class UART:
    def __init__(self):
        try:
            self.port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
            #self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        except:
            print("Imposible Inicializar UART")
    
    def control(self, num):
        cmd = str(num)
        self.port.write(cmd.encode())
        try:
            rcv=self.port.read(15)
            print(rcv.decode())
        except:
            print("Sin Dato")
    
        
    #def keypress(self,event):
    #    keyPressed = event.char 
    #    if event.keysym == 'Up':
    #        self.hilo_control = threading.Thread(target=self.control, args=(1,))
    #        self.hilo_control.start()
    #    elif event.keysym == 'Down':
    #        self.hilo_control = threading.Thread(target=self.control, args=(2,))
    #        self.hilo_control.start()
    #    elif event.keysym == 'Right':
    #      self.hilo_control = threading.Thread(target=self.control, args=(3,))
    #      self.hilo_control.start()
    #    elif event.keysym == 'Left':
    #        self.hilo_control = threading.Thread(target=self.control, args=(4,))
    #        self.hilo_control.start()
    #    elif event.keysym == '0':
    #        self.hilo_control = threading.Thread(target=self.control, args=(0,))
    #        self.hilo_control.start()
    #    elif event.keysym == '5':
    #        self.hilo_control = threading.Thread(target=self.control, args=(5,))
    #        self.hilo_control.start()
    #    elif event.keysym == '6':
    #        self.hilo_control = threading.Thread(target=self.control, args=(6,))
    #        self.hilo_control.start()
    #    elif event.keysym == '7':
    #        self.hilo_control = threading.Thread(target=self.control, args=(7,))
    #        self.hilo_control.start()
    #def keyrelease(self,event):
    #    keyPressed = event.char 
    #    if event.keysym == 'Up':
    #        self.hilo_control.deamon()
    #    elif event.keysym == 'Down':
    #        self.hilo_control.stop()
    #    elif event.keysym == 'Right':
    #        self.hilo_control.stop()
    #    elif event.keysym == 'Left':
    #        self.hilo_control.stop()
    #    elif event.keysym == '0':
    #        self.hilo_control.stop()