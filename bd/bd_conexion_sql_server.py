import pyodbc #Libreria que permite conectarse a SQL server

direccion_servidor = 'LOCALHOST'
nombre_bd = 'CENTRAL_TELEFONICA' #Nombre de la base de datos ya creada en SQL
nombre_usuario = 'sa'
password = '*********'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password) #Se crea la conexion con sus parametros a SQL server
    # OK! conexión exitosa
    print("OK! Conexión exitosa a la base de datos  ----> ", nombre_bd)
except Exception as err:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", err)
