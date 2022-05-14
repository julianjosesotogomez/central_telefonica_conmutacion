import os
import re
from bd.bd_conexion_sql_server import conexion
from bd.consulta_bd import get

def imprimir(factura_abonado):
    try:
        with conexion.cursor() as cursor:
            consulta_usuario_abonado = "SELECT usuario_abonado, usuario_receptor FROM registro_llamadas WHERE id_abonado = ?;"
            cursor.execute(consulta_usuario_abonado, (factura_abonado))
            row = cursor.fetchone()
            abonado=str(row.usuario_abonado)

            consulta_usuario_receptor = "SELECT  usuario_receptor FROM registro_llamadas WHERE id_abonado = ?;"
            cursor.execute(consulta_usuario_receptor, (factura_abonado))
            rows = cursor.fetchall()
            rows_s=str(rows)
            rows_c = re.sub("\[|\]|\,|\(|\)|\'|\'","",rows_s) 

            consulta_usuario_tiempo = "SELECT  duracion_llamada FROM registro_llamadas WHERE id_abonado = ?;"
            cursor.execute(consulta_usuario_tiempo, (factura_abonado))
            time = cursor.fetchall()
            time_s=str(time)
            time_c = re.sub("\[|\]|\,|\(|\)|\'|\'","",time_s)
                

            consulta_usuario_fecha = "SELECT  fecha_llamada FROM registro_llamadas WHERE id_abonado = ?;"
            cursor.execute(consulta_usuario_fecha, (factura_abonado))
            fecha = cursor.fetchall()
            fecha_s=str(fecha)
            fecha_c = re.sub("\[|\]|\,|\(|\)|\'|\'","",fecha_s)

            consulta_usuario_saldo = "SELECT (SUM(duracion_llamada)*3600)+(SUM(duracion_llamada)*60) FROM registro_llamadas WHERE id_abonado=?;"
            cursor.execute(consulta_usuario_saldo, (factura_abonado))
            saldo=cursor.fetchone()
            saldo_s=str(saldo)
            saldo_c=re.sub("\[|\]|\,|\(|\)|\'|\'","",saldo_s) 

            factura=open("C:/Users/julia/OneDrive/Documentos/DocumentosPersonales/Archivos Universitarios/2022-1/Conmutacion\central_telefonica/facturas/factura.txt",'w')
            factura.write('\t'*4 + 'FACTURA ELECTRONICA CON REGISTROS ' + os.linesep)
            factura.write('\t'*4 + 'NUMERO LINEA:' + str(abonado) + os.linesep)
            factura.write('\t' + 'NUMERO' + os.linesep)
            factura.write('\t' + str(rows_c) +  os.linesep)
            factura.write('\t' + 'TIEMPO'+ os.linesep)
            factura.write('\t' + str(time_c) +  os.linesep)
            factura.write('\t' + 'FECHA LLAMADA'+ os.linesep)
            factura.write('\t' + str(fecha_c) +  os.linesep)
            factura.write('\t' + 'SALDO LLAMADA:'+ os.linesep)
            factura.write('\t' + str(saldo_c) +  os.linesep)
            factura.close()
    except Exception as err:
        print("Ocurrió un error al construir la factura: ", err)

 