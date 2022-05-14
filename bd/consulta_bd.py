from bd.bd_conexion_sql_server import conexion

def get(data):
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT id_abonado, usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada FROM registro_llamadas WHERE id_abonado = ?;"
            cursor.execute(consulta, (data))
            datos = cursor.fetchall()
            for i in datos:
                print("Registro llamada ---> ",i)
            return i
    except Exception as err:
        print("Ocurrió un error al consultar con where: ", err)
    finally:
        conexion.close()