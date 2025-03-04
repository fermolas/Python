import pygame
import tkinter as tk
from tkinter import filedialog

# Inicializar Pygame
pygame.mixer.init()

# Función para abrir un archivo de audio
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("musica1.mp3", "*.mp3")])
    if archivo:
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()

# Función para pausar la música
def pausar_musica():
    pygame.mixer.music.pause()

# Función para reanudar la música
def reanudar_musica():
    pygame.mixer.music.unpause()

# Función para detener la música
def detener_musica():
    pygame.mixer.music.stop()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reproductor de Música")

# Botones de control
btn_abrir = tk.Button(ventana, text="Abrir", command=abrir_archivo)
btn_abrir.pack(pady=10)

btn_pausar = tk.Button(ventana, text="Pausar", command=pausar_musica)
btn_pausar.pack(pady=10)

btn_reanudar = tk.Button(ventana, text="Reanudar", command=reanudar_musica)
btn_reanudar.pack(pady=10)

btn_detener = tk.Button(ventana, text="Detener", command=detener_musica)
btn_detener.pack(pady=10)

# Ejecutar la interfaz de usuario
ventana.mainloop()
