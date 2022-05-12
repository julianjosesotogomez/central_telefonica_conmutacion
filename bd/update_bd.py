from bd_conexion_sql_server import conexion

try:
    with conexion.cursor() as cursor:
        consulta="UPDATE registro_llamadas SET usuario_abonado=?, usuario_receptor=?, duracion_llamada=?, fecha_llamada=? WHERE id_llamada=?;"
        usuario_abonado="555555555"
        usuario_receptor="99999999"
        duracion_llamada="56.9210"
        fecha_llamada=""
        id_llamada=3
        cursor.execute(consulta,(usuario_abonado,usuario_receptor, duracion_llamada,fecha_llamada,id_llamada))

        print("Se ha realizado la correción satisfactoriamente! ")
except Exception as err:
    print("Error! Ocurrio un error en el ingreso de los datos ", err)
finally:
    conexion.close()