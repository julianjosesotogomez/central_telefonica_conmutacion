from bd.bd_conexion_sql_server import conexion
from datetime import datetime

def insert(id_abonado, dataOne, dataTwo, dataThree): #Funcion permite insertar los datos en la tabla de la base de datos
    try:
        with conexion.cursor() as cursor: #Constructor: Define una variable como una función
            consulta="INSERT INTO registro_llamadas(id_abonado, usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada) VALUES (?,?,?,?,?);"
            cursor.execute(consulta,(id_abonado,dataOne,dataTwo,dataThree,datetime.now())) #datetime.now=para que se guarde la información en el momento exacto que se hace la llamada
            print("Llamada registrada correctamente! -> Origen: ",dataOne, " Destino: ", dataTwo, " Tiempo: ",  dataThree, " Fecha: ", datetime.now())
    except Exception as err:
        print("Error! Ocurrio un error en el ingreso de los datos ", err)