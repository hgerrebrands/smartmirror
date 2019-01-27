import tkinter as tk
import pytz, datetime
from htu21d import HTU21D
from guizero import Text 
from random import seed, choice
from string import ascii_letters

seed(42)
colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
def do_stuff():
    #s = ''.join([choice(ascii_letters) for i in range(10)])
    s = text=datetime.datetime.now(pytz.timezone ("Europe/Amsterdam")).strftime("%d-%m-%y    %H:%M:%S")
    l.config(text=s)
    root.after(100, do_stuff)
def showTemperature():
    sensor = HTU21D()
    sensor.reset()
    temperature = sensor.get_temp()
    s1 = text="Temperature: %s"%temperature
    temp.config(text=s1)
    root.after(100, showTemperature)
      
root=tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label('', font=("Helvetica", 60), fg='white', bg='black')
l.pack(expand=True)

temp = tk.Label('', font=("Helvetica", 60), fg='white', bg='black')
temp.pack(expand=True)

root.configure(background='black')

app=FullScreenApp(root)
do_stuff()
showTemperature()
root.mainloop()
