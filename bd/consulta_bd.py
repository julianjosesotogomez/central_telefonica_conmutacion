from bd.bd_conexion_sql_server import conexion

def get(data):
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT id_abonado, usuario_abonado, usuario_receptor, duracion_llamada, fecha_llamada FROM registro_llamadas WHERE id_abonado = ?;"#>Consulta base de datos
            cursor.execute(consulta, (data)) # es donde se ejecuta el Query el cual recibe el parametro que trae la funcion
            datos = cursor.fetchall() #Funcion de la libreria que permite traer todos los datos
            for i in datos:
                print("Registro llamada ---> ",i)
            return datos
    except Exception as err:
        print("Ocurrió un error al consultar con where: ", err)
