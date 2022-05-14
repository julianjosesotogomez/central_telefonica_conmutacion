from msilib.schema import Error
import time
import pygame
import random
from os import system
from marcado import marcado_tono
from conversacion import reproduccion as reproduc
from imprimir_factura import imprimir
from bd.insert_bd import insert
from bd.consulta_bd import get


class CentralTelefonoefonica():
    def __init__(self):
        self.estados_llamada = ['Disponible','Ocupado','Fuera de servicio']
        self.conversaciones = ['conv_one.mp3','conv_two.mp3','conv_three.mp3','conv_four.mp3']
        self.usuarios = []
        self.abonado_disponible = []
        self.abonado_ocupado = []
        self.out_servicio =[]
        
        for i in range(0,20):
            telefono = random.randrange(8000000,9000000)
            self.usuarios.append(telefono)

        for i in range(0,3):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono)
            self.out_servicio.append(telefono)

        for i in range(3,8):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono)
            self.abonado_ocupado.append(telefono)

        for i in range(8,20):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono)
            self.abonado_disponible.append(telefono)
        
        self.Copia = self.abonado_disponible.copy()

        try:
            while(True):
                reproduc("./audios_conmutacion/Ingreso_abonado.mp3")
                print('\nLos usuarios disponibles en este momento son: ')
                for i in range(0,12):
                    print("{:^20}{:^20}".format(self.abonado_disponible[i],self.estados_llamada[0]))
                self.abonado = int(input('Ingrese número de abonado : '))
                self.ind1 = self.Copia.index(self.abonado)
                if self.abonado in self.abonado_disponible:
                    self.abonado_disponible.remove(self.abonado)
                    break
        except Exception as err:
            print("Ha sucedido un error con el ingreso del abonado! ----> ", err)
            reproduc("./audios_conmutacion/Sin_registrar.mp3")
            CentralTelefonoefonica()
                
        while(True):
            CentralTelefonoefonica.menu(self)
            reproduc("./audios_conmutacion/Op_menu.mp3")
            reproduccion = input("\nSi desea realizar otra operación en la Central telefonoefónica \nIngrese la opción : \n Si ( 1 ) \n No ( 0 ) \n Digite: ")
            if (reproduccion == "0"):
                reproduc("./audios_conmutacion/Final.mp3")
                break
            elif (reproduccion == "1"):
                CentralTelefonoefonica.menu(self)
            else:
                reproduc("./audios_conmutacion/Op_invalida.mp3")
               

    def menu(self):
        self.menu="""

        ---------------------MENÚ---------------------

        Opciones de Menú :

        Contactos                 ( 1 )
        Llamar                    ( 2 )
        Registros de llamadas     ( 3 )
        Realizar facturación      ( 4 )


        Para salir del Menú oprima Ctrl+c

        Usted ingresó la opción de Menú : """




        self.op= int(input(self.menu))
        Op_Menu = map(int,str(self.op))
        marcado_tono(Op_Menu)
        while(self.op < 1 or self.op > 5):
            print("La opción de Menú no es correcta.")
            self.op=int(input(self.menu))
        if ( self.op == 1 ):
            print("Para realizar una llamada debe escoger uno de los contactos disponibles, realice la operacion (2) en el menú")
            print("{:^20}{:^20}".format(" Número de abonado", "Estado Actual"))
            for i in range(0,3):
                print("{:^20}{:^20}".format(self.out_servicio[i], self.estados_llamada[2]))
            for i in range(0,5):
                print("{:^20}{:^20}".format(self.abonado_ocupado[i], self.estados_llamada[1]))
            for i in range(0,11):
                print("{:^20}{:^20}".format(self.abonado_disponible[i], self.estados_llamada[0]))

        if (self.op == 2): 
            for i in range(0,3):
                print("{:^20}{:^20}".format(self.out_servicio[i], self.estados_llamada[2]))
            for i in range(0,5):
                print("{:^20}{:^20}".format(self.abonado_ocupado[i], self.estados_llamada[1]))
            for i in range(0,11):
                print("{:^20}{:^20}".format(self.abonado_disponible[i], self.estados_llamada[0]))
            numero = int(input("Ingrese el número a llamar: "))
            if numero in self.out_servicio:
                reproduc("./audios_conmutacion/fuera_servicio.mp3")
                time.sleep(0.8)
            elif numero in self.abonado_ocupado:
                reproduc("./tonos/ocupado.mp3")
                time.sleep(0.8)
            elif numero in self.abonado_disponible:
                num2 = map(int,str(numero))
                marcado_tono(num2)
                reproduc("./tonos/marcando.mp3")
                time.sleep(1)
                random.seed()
                Conv = random.choice(self.conversaciones)
                Cx = "./audios_conmutacion/"+Conv
                tiempo_audio = reproduc(Cx)
                time.sleep(0.5)
                parseo=self.abonado
                id_abonado=str(parseo)
                insert(id_abonado[0:3],self.abonado,numero,tiempo_audio)
            else:
                tiempo_audio = reproduc("./audios_conmutacion/Sin_registrar.mp3")
                time.sleep(0.5)
        
        if (self.op == 3):
            consulta_abonado = str(input("Ingrese los tres primeros digitos del numero del abonado al cual desea consultar el registro de llamadas: "))
            get(consulta_abonado)
        if (self.op == 4):
            factura_abonado=str(input("Ingrese los tres primeros digitos del numero del abonado al cual desea realizar la factura: "))
            imprimir(factura_abonado)
            print("------------> ¡Factura realizada! <-------------")
           
random.seed(0)
pygame.init()
pygame.mixer.init()
Cen = CentralTelefonoefonica()
