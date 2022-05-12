from bd_conexion_sql_server import conexion

try:
    with conexion.cursor() as cursor:
        consulta="INSERT INTO registro_llamadas(usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada) VALUES (?,?,?,?);"
        cursor.execute(consulta,("1246565743","2354534533","34.64543",""))
except Exception as err:
    print("Error! Ocurrio un error en el ingreso de los datos ", err)
finally:
    conexion.close()