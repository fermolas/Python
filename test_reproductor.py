import pygame
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Reproductor import Reproductor
# Inicializar Pygame
pygame.mixer.init()

musica = Reproductor("musica1.mp3")               
def playMusica():
    musica.play()
    
def pauseMusica():
    musica.pause()
    
def stopMusica():
    musica.stop()    

def ajustar_volumen(valor):
    volumen = float(valor) / 100  # Convertir de 0-100 a 0.0-1.0
    pygame.mixer.music.set_volume(volumen)

#master = Tk()
master = tk.Tk()
master.geometry("200x200")

display = Label(master, text="WINAMP")
display.pack(pady=10)

bplay = Button(master, text="Play", command=playMusica)
bplay.pack(pady=10)

bPause = Button(master, text= "Pause", command=pauseMusica)
bPause.pack(pady=10)

bStop = Button(master, text= "Stop", command=stopMusica)
bStop.pack(pady=10)

# Función para ajustar el volumen
volumen_slider = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, label="Volumen", command=ajustar_volumen)
volumen_slider.set(50)  # Establece el valor inicial del volumen al 50%
volumen_slider.pack(pady=10)

master.mainloop()