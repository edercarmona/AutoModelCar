from gpiozero import Button
import threading

class  OnOff:
    
    estado = False
    
    def __init__(self):    
        self.boton = Button(21)
        self.hilo = threading.Thread(target=self.ispressed, name='OnOff')
        self.hilo.start()
        
    def ToggleVal(self):
        self.estado = not self.estado
        print(self.estado)
        
    def ispressed(self):
        while True:
            self.boton.when_pressed = self.ToggleVal