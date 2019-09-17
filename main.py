#LIBRERRIAS
import threading

#CLASES
from vl53l0x import VL5310X
from uart import UART
from OnOff import OnOff

class AutoModelCar():
    
    def __init__(self):
        self.encendido = False
        self.boton = OnOff()
        self.distFrontal = VL5310X()
        self.car = UART()
        self.on = threading.Thread(target=self.On, name='On')
        self.on.start()
        self.off = threading.Thread(target=self.Off, name='Off')
        self.off.start()
                       
    def On(self):
        while True:
            if self.boton.estado == True:
                if self.distFrontal.alive == True:
                    self.d = threading.Thread(target=self.Distancia, name='Mide Distancia Frente')
                    self.d.start()
                if self.car.alive == True:
                    self.car.control(1)
                if self.car.alive == True and self.distFrontal.alive == True:
                    self.encendido = not self.encendido
                break
    def Off(self):
        while True:
            if self.boton.estado == False and self.encendido == True:
                self.car.control(0)
                break
            
    def Distancia(self):
        while True:
            if self.distFrontal.mideDistancia() <= 60:
                self.ControlCar(0,)
            elif self.boton.estado==True and self.distFrontal.mideDistancia() > 60:
                self.ControlCar(1,)
            else:
                self.ControlCar(0,)

    def ControlCar(self,num):
        self.car.control(num,)
        
auto = AutoModelCar()