import pygame
from time import sleep
import time

def reproduccion(audio):
    t_inicial=time.time() #Funcion que permite tomar el tiempo de inicio de reproduccion del audio
    pygame.mixer.music.load(audio) #Carga el parametro del audio
    pygame.mixer.music.play() #reproduce la conversacion
    while pygame.mixer.music.get_busy(): #Tiempo de espera que le hace a la conversacion
        sleep(1)
    t_final=time.time()
    duracion_audio = t_final-t_inicial
    return duracion_audio