import mysql.connector

def obtener_imagen_desde_bd():
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sendimage"
    )
    cursor = conn.cursor()

    # Consulta para recuperar la imagen de la base de datos
    cursor.execute("SELECT imagen FROM imagenes")
    imagen_bytes = cursor.fetchone()[0]  # Suponiendo que la imagen está almacenada como bytes en la base de datos

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    return imagen_bytes
