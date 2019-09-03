import tkinter as tk
from tkinter import ttk
import sys
import RPi.GPIO as GPIO
import time
import threading
from PIL import Image
from PIL import ImageTk
import datetime
import os
import numpy as np
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Application(ttk.Frame):
        
    def __init__(self, main_window):
        super().__init__(main_window)
        self.thread = None
        self.panel = None
        self.frame = None
        self.port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
        #self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        main_window.title("Control de Carro")
        main_window.wm_protocol("WM_DELETE_WINDOW", self.onClose)
        main_window.configure(width=820, height=640)
        self.bind_all('<Any-KeyPress>', self.keypress)
        #self.bind_all('<Any-KeyRelease>', self.keyrelease)
        self.place(relwidth=1, relheight=1)
        self.stopEvent = threading.Event()
        

    def onClose(self):      
        print("[INFO] closing...")
        self.stopEvent.set()
        main_window.quit()
        
    def keypress(self,event):
        keyPressed = event.char 
        if event.keysym == 'Up':
            self.hilo_control = threading.Thread(target=self.control, args=(1,))
            self.hilo_control.start()
        elif event.keysym == 'Down':
            self.hilo_control = threading.Thread(target=self.control, args=(2,))
            self.hilo_control.start()
        elif event.keysym == 'Right':
          self.hilo_control = threading.Thread(target=self.control, args=(3,))
          self.hilo_control.start()
        elif event.keysym == 'Left':
            self.hilo_control = threading.Thread(target=self.control, args=(4,))
            self.hilo_control.start()
        elif event.keysym == '0':
            self.hilo_control = threading.Thread(target=self.control, args=(0,))
            self.hilo_control.start()
        elif event.keysym == '5':
            self.hilo_control = threading.Thread(target=self.control, args=(5,))
            self.hilo_control.start()
        elif event.keysym == '6':
            self.hilo_control = threading.Thread(target=self.control, args=(6,))
            self.hilo_control.start()
        elif event.keysym == '7':
            self.hilo_control = threading.Thread(target=self.control, args=(7,))
            self.hilo_control.start()
    def keyrelease(self,event):
        keyPressed = event.char 
        if event.keysym == 'Up':
            self.hilo_control.deamon()
        elif event.keysym == 'Down':
            self.hilo_control.stop()
        elif event.keysym == 'Right':
            self.hilo_control.stop()
        elif event.keysym == 'Left':
            self.hilo_control.stop()
        elif event.keysym == '0':
            self.hilo_control.stop()
    def control(self, num):
        cmd = str(num)
        self.port.write(cmd.encode())
        try:
            rcv=self.port.read(15)
            print(rcv.decode())
        except:
            print("Sin Dato")
        
main_window = tk.Tk()
a=0
time.sleep(2.0)
app = Application(main_window)
app.mainloop()
