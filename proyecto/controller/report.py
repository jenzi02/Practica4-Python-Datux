from config.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
             p.pais, 
            COALESCE(SUM(v.quantity), 0) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p ON v.postal_code = p.code
        GROUP BY 
            p.pais
        ORDER BY 
            total_vendido ASC
        LIMIT 2;
    """
    df=pd.read_sql_query(query,conn)
    fecha="08-02"
    path=f"/workspaces/Practica4-Python-Datux/proyecto/files/data-Huerta3.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com','Reporte de Ventas', 'Adjunto el reporte de ventas actualizado.', data)