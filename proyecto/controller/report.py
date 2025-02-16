from config.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
            c.categoria,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
             PRODUCTOS p ON v.product_id = p.product_id
        JOIN 
            CATEGORIAS c ON p.categoria_id = c.categoria_id
        GROUP BY 
            c.categoria
        ORDER BY 
            total_vendido DESC;

    """
    df=pd.read_sql_query(query,conn)
    fecha="08-02"
    path=f"/workspaces/Practica4-Python-Datux/proyecto/files/data-HuertaCarrasco.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com','Reporte de Ventas', 'Adjunto el reporte de ventas actualizado.', data)