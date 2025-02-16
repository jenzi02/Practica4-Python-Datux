from config.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
       SELECT 
            proveedor_id, 
            nombre_comercial, 
            contacto_comercial, 
            correo_electronico, 
            telefono, 
            saldo_pendiente, 
            fecha_ultima_compra
        FROM 
             PROVEEDORES
        WHERE 
            saldo_pendiente > 0
        ORDER BY 
            saldo_pendiente DESC;
    """
    df=pd.read_sql_query(query,conn)
    path=f"/workspaces/Practica4-Python-Datux/proyecto/files/datafuente.xls"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example','Reporte','Reporte',data)