import threading
from vl53l0x import VL5310X
from uart import UART

class AutoModelCar():
    
    def __init__(self):
        self.distFrontal = VL5310X()
        self.d = threading.Thread(target=self.Distancia, name='Mide Distancia Frente') 
        self.d.start()
        self.car = UART()
        self.c = threading.Thread(target=self.ControlCar, name='Carro Avanza', args=(1,))
        self.c.start()
    
    def Distancia(self):
        while True:
            print(self.distFrontal.mideDistancia())
            if self.distFrontal.mideDistancia() <= 60:
                self.ControlCar(0,)
            else:
                self.ControlCar(1,)

    def ControlCar(self,num):
        self.car.control(num,)
        
auto = AutoModelCar()
