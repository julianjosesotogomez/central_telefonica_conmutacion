
from bd.consulta_bd import get

def imprimir(factura_abonado):
    try:
        data= get(factura_abonado)
        parseo=str(data)
        file = open("C:/Users/julia/OneDrive/Documentos/DocumentosPersonales/Archivos Universitarios/2022-1/Conmutacion\central_telefonica/facturas/factura.txt", "w")
        file.write("Registro de los datos ----> " + parseo)
        file.close()

    except Exception as err:
        print("Ocurrió un error al construir la factura: ", err)

 