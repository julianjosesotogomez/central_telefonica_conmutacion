from bd.bd_conexion_sql_server import conexion
from datetime import datetime

def insert(id_abonado, dataOne, dataTwo, dataThree):
    try:
        with conexion.cursor() as cursor:
            consulta="INSERT INTO registro_llamadas(id_abonado, usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada) VALUES (?,?,?,?,?);"
            cursor.execute(consulta,(id_abonado,dataOne,dataTwo,dataThree,datetime.now()))
            print("Llamada registrada correctamente! -> Origen: ",dataOne, " Destino: ", dataTwo, " Tiempo: ",  dataThree, " Fecha: ", datetime.now())
    except Exception as err:
        print("Error! Ocurrio un error en el ingreso de los datos ", err)
    finally:
        conexion.close()