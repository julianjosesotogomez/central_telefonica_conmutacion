import pyodbc
direccion_servidor = 'LOCALHOST'
nombre_bd = 'CENTRAL_TELEFONICA'
nombre_usuario = 'sa'
password = ''
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
    print("OK! Conexión exitosa a la base de datos  ----> ", nombre_bd)
except Exception as err:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", err)