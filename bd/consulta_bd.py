from bd_conexion_sql_server import conexion
try:
    with conexion.cursor() as cursor:

        consulta = "SELECT id_llamada, usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada FROM registro_llamadas WHERE id_llamada = ?;"
        registro_llamada=cursor.execute(consulta, (1))
        print(registro_llamada)

        # Con fetchall traemos todas las filas
        #datos = cursor.fetchall()
        # Recorrer e imprimir
        #for i in datos:
            #print(i)

except Exception as err:
    print("Ocurrió un error al consultar con where: ", err)
finally:
    conexion.close()