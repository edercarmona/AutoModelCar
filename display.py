import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Display:
    
    def __init__(self):
        self.DC = 23
        self.RST = 24
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        self.disp = LCD.PCD8544(self.DC, self.RST, spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE, max_speed_hz=4000000))
        self.disp.begin(contrast=40)
        self.disp.clear()
        self.disp.display()
        self.image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        self.fuente = ImageFont.load_default()
        self.contador = 1
        
    def Mensaje(self, text):
        self.draw.text((1,self.contador), text, font=self.fuente)
        self.disp.image(self.image)
        self.disp.display()
        self.contador += 9
    
    def Limpiar(self):
        self.disp.clear()
        self.disp.display()
        self.draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)