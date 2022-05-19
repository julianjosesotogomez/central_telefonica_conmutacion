import pygame 
import time
pygame.init()
pygame.mixer.init()

def marcado_tono(numero):
    for digito in numero:
        if digito == 0:
            pygame.mixer.music.load("./tonos/t0.mp3") #Esta funcionalidad de pygame me permite cargar el tono en la direccion que especificamos 
            pygame.mixer.music.play() #Luego de haber cargado el archivo del tono lo reproduce gracias a la funcion .play()
            time.sleep(0.25)#Me da un tiempo de espera. 
        if digito == 1:
            pygame.mixer.music.load("./tonos/t1.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 2:
            pygame.mixer.music.load("./tonos/t2.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 3:
            pygame.mixer.music.load("./tonos/t3.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 4:
            pygame.mixer.music.load("./tonos/t4.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 5:
            pygame.mixer.music.load("./tonos/t5.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 6:
            pygame.mixer.music.load("./tonos/t6.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 7:
            pygame.mixer.music.load("./tonos/t7.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 8:
            pygame.mixer.music.load("./tonos/t8.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)
        if digito == 9:
            pygame.mixer.music.load("./tonos/t9.mp3")
            pygame.mixer.music.play()
            time.sleep(0.25)