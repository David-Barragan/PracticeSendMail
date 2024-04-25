import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
from consulta_bd import obtener_imagen_desde_bd

def enviar_correo_con_imagen():
    # Obtener la imagen desde la base de datos
    imagen_bytes = obtener_imagen_desde_bd()

    # Codificar la imagen en base64
    imagen_codificada = base64.b64encode(imagen_bytes).decode('utf-8')

    # Configurar el correo electrónico
    correo_emisor = 'da_evo@hotmail.com' #correo emisor
    correo_receptor = 'daevo14@gmail.com' #correo receptor 
    mensaje = MIMEMultipart()
    mensaje['From'] = correo_emisor
    mensaje['To'] = correo_receptor
    mensaje['Subject'] = 'Imagen adjunta desde la base de datos'

    # Adjuntar la imagen al correo electrónico
    imagen_adjunta = MIMEImage(base64.b64decode(imagen_codificada), name='zorro.jpg')
    mensaje.attach(imagen_adjunta)

    # Conexión al servidor SMTP y envío del correo electrónico
    servidor_smtp = smtplib.SMTP('smtp.outlook.com', 587)  # Cambia esto según tu proveedor de correo en este caso hotmail que es outlook
    servidor_smtp.starttls()
    servidor_smtp.login(correo_emisor, 'password email') # aca se coloca la contraseña el hotmail
    servidor_smtp.sendmail(correo_emisor, correo_receptor, mensaje.as_string())
    servidor_smtp.quit()

if __name__ == "__main__":
    enviar_correo_con_imagen()
