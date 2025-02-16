from config.app import *
import pandas as pd

import os

from datetime import datetime
from config.app import App  # Asegúrate de importar la clase App

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    
    # Consulta SQL para obtener el país con menos productos comprados
    query = """
        SELECT 
            p.pais,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p ON v.postal_code = p.code
        GROUP BY 
            p.pais
        ORDER BY 
            total_vendido ASC  -- Ordenado de menor a mayor
        LIMIT 1;  -- Solo el país con menos compras
    """
    
    df = pd.read_sql_query(query, conn)

    # Formatear la fecha actual para el nombre del archivo
    fecha = datetime.now().strftime("%Y-%m-%d")
    folder_path = "/workspaces/Practica4-Python-Datux/proyecto/files/data.H.csv"
    file_path = f"{folder_path}/reporte_menor_ventas_{fecha}.csv"

    # Crear carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Guardar reporte en CSV
    df.to_csv(file_path, index=False)
    
    # Enviar el reporte por correo
    sendMail(app, file_path)

def sendMail(app: App, file_path):
    app.mail.send_email(
        'from@example.com', 
        'Reporte de Ventas (País con Menos Compras)', 
        'Adjunto el reporte del país con menos compras.', 
        file_path
    )
