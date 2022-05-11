import pyodbc
direccion_servidor = ''
nombre_bd = ''
nombre_usuario = ''
password = ''
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
    print("Conexión exitosa a la base de datos")
except Exception as err:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", err)