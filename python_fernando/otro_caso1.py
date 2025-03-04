from tkinter import *
from tkinter.ttk import *
from Reproductor import Reproductor

musica = Reproductor("musica1.mp3")
                     
def playMusica():
    musica.play()
    
def pauseMusica():
    musica.pause()
    
def stopMusica():
    musica.stop()    

master = Tk()
master.geometry("200x200")

display = Label(master, text="WINAMP")
display.pack(pady=10)

bplay = Button(master, text="Play", command=playMusica)
bplay.pack(pady=10)

bPause = Button(master, text= "Pause", command=pauseMusica)
bPause.pack(pady=10)

bStop = Button(master, text= "Stop", command=stopMusica)
bStop.pack(pady=10)

master.mainloop()