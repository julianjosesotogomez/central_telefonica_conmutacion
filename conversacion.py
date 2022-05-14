import pygame
from time import sleep
import time

def reproduccion(audio):
    t_inicial=time.time()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)
    t_final=time.time()
    duracion_audio = t_final-t_inicial
    return duracion_audio