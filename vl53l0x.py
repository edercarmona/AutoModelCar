import time
import board
import busio
import adafruit_vl53l0x

class VL5310X:
    alive = False
    def __init__(self):
            try:
                self.i2c = busio.I2C(board.SCL, board.SDA)
                self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)
                self.alive = True
            except:
                self.alive = False
                print("No se puede Inicializar VL5310X")
    
    def mideDistancia(self):
        time.sleep(1.0)
        return self.vl53.range