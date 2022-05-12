from bd_conexion_sql_server import conexion
try:
    with conexion.cursor() as cursor:

        consulta = "DELETE FROM registro_llamadas WHERE id_llamada = ?;"
        registro_llamada=cursor.execute(consulta, (1))
        print("Se ha eliminado el registro de la llamada correctamente!")

except Exception as err:
    print("Ocurrió un error al consultar con where: ", err)
finally:
    conexion.close()