from msilib.schema import Error #Es una libreria para leer y escribir en archivos de Microsoft
import time #Es una librería que proporciona varias funciones relacionadas con el tiempo
import pygame #Libreria para cargar y reproducir sonidos
import random #Libreria para generar los abonados
from os import system #Libreria para abrir documentos
from marcado import marcado_tono #Funcion que reproduce los audios de los tonos para las llamadas
from conversacion import reproduccion as reproduc #Funcion que procesa el tiempo de la conversacion y su reproduccion
from imprimir_factura import imprimir
from bd.insert_bd import insert #Funcion para agregar los datos de cada llamada en la base de datos
from bd.consulta_bd import get #Funcion extraer los registros de la llamada de determinado abonado


class CentralTelefonoefonica():
    def __init__(self):
        self.estados_llamada = ['Disponible','Ocupado','Fuera de servicio']
        self.conversaciones = ['conv_one.mp3','conv_two.mp3','conv_three.mp3','conv_four.mp3', 'conv_five.mp3']
        self.usuarios = [] #Se crea una lista
        self.abonado_disponible = []
        self.abonado_ocupado = []
        self.out_servicio =[]
        
        for i in range(0,100):
            telefono = random.randrange(8000000,9000000)
            self.usuarios.append(telefono) #.append() me permite agregar al final de la lista los numeros random. 

        for i in range(0,10):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono) #.remove()  me permite eliminar objetos de una lista.
            self.out_servicio.append(telefono)

        for i in range(10,30):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono)
            self.abonado_ocupado.append(telefono)

        for i in range(30,100):
            telefono = random.choice(self.usuarios)
            self.usuarios.remove(telefono)
            self.abonado_disponible.append(telefono)
        
        self.Copia = self.abonado_disponible.copy() #guarda la lista de abonados disponibles, gracias a .copy()

        try:
            while(True):
                reproduc("./audios_conmutacion/Ingreso_abonado.mp3")
                print('\nLos usuarios disponibles en este momento son: ')
                for i in range(0,70):
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
        Op_Menu = map(int,str(self.op))#Me permite recorrer el listado obtenido en self.op
        marcado_tono(Op_Menu)
        while(self.op < 1 or self.op > 5):
            print("La opción de Menú no es correcta.")
            self.op=int(input(self.menu))
        #Los condicional a continuación me permite acceder a cada una de las funciones presentadas en el menú 
        if ( self.op == 1 ):
            print("Para realizar una llamada debe escoger uno de los contactos disponibles, realice la operacion (2) en el menú")
            print("{:^20}{:^20}".format(" Número de abonado", "Estado Actual"))
            for i in range(0,10):
                print("{:^20}{:^20}".format(self.out_servicio[i], self.estados_llamada[2]))
            for i in range(0,20):
                print("{:^20}{:^20}".format(self.abonado_ocupado[i], self.estados_llamada[1]))
            for i in range(0,69):
                print("{:^20}{:^20}".format(self.abonado_disponible[i], self.estados_llamada[0]))

        if (self.op == 2): 
            for i in range(0,10):
                print("{:^20}{:^20}".format(self.out_servicio[i], self.estados_llamada[2]))
            for i in range(0,20):
                print("{:^20}{:^20}".format(self.abonado_ocupado[i], self.estados_llamada[1]))
            for i in range(0,69):
                print("{:^20}{:^20}".format(self.abonado_disponible[i], self.estados_llamada[0]))
            numero = int(input("Ingrese el número a llamar: "))
            if numero in self.out_servicio:
                reproduc("./audios_conmutacion/fuera_servicio.mp3") #Se llama la funcion reproduccion llamada como reproduc, del archivo conversacion.py 
                time.sleep(0.8) #time.sleep() Me permite esperar determinado tiempo para que en este caso se ejecute una instrucción luego de otra. 
            elif numero in self.abonado_ocupado:
                reproduc("./tonos/ocupado.mp3")
                time.sleep(0.8)
            elif numero in self.abonado_disponible:
                num2 = map(int,str(numero))
                marcado_tono(num2)
                reproduc("./tonos/marcando.mp3")
                time.sleep(1)
                random.seed()#  Me permite inicializar los numeros aleatorios ya obtenidos  
                Conv = random.choice(self.conversaciones)
                Cx = "./audios_conmutacion/"+Conv
                tiempo_audio = reproduc(Cx)
                time.sleep(0.5)
                parseo=self.abonado
                id_abonado=str(parseo) #Convertimos a string el numero del abonado, para poderlo procesar en la base de datos. 
                insert(id_abonado[0:3],self.abonado,numero,tiempo_audio) #Invocamos la funcion insert() de bd/insert_bd.py, la cual nos registra la llamada en la base de datos de la central. 
            else:
                tiempo_audio = reproduc("./audios_conmutacion/Sin_registrar.mp3")
                time.sleep(0.5)
        
        if (self.op == 3):
            consulta_abonado = str(input("Ingrese los tres primeros digitos del numero del abonado al cual desea consultar el registro de llamadas: "))
            get(consulta_abonado)#Invocamos la funcion get() de bd/consulta_bd.py la cual nos permite obtener el registro del abonado el cual estamos enviando como parametro. 

        if (self.op == 4):
            factura_abonado=str(input("Ingrese los tres primeros digitos del numero del abonado al cual desea realizar la factura: "))
            imprimir(factura_abonado)#Invocamos la funcion imprimir() de imprimir_factura.py la cual nos permite obtener y crear la factura del abonado el cual estamos enviando como parametro. 
            print("------------> ¡Factura realizada! <-------------")
           
random.seed(0) #Me inicializa los numeros random desde cero
pygame.init() #Inicializa la libreria pygame
pygame.mixer.init()
Cen = CentralTelefonoefonica() #Declara como una variable la funcion, para luego ser invocada con facilidad
