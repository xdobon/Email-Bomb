import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, cuerpo,servidor,remitente,password):

    # Crear un objeto MIMEMultipart para el correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Crear un objeto MIMEMultipart para el correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Iniciar la conexión SMTP
    servidor_smtp = smtplib.SMTP(servidor, 587)
    servidor_smtp.starttls()

    # Iniciar sesión en el servidor SMTP
    servidor_smtp.login(remitente, password)

    # Enviar el correo electrónico y obtener el código de respuesta
    codigo_respuesta = servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())

    # Cerrar la conexión SMTP
    servidor_smtp.quit()

    # Devolver el código de respuesta
    return codigo_respuesta

    # Ejemplo de uso
remitente = input("Correo electronico:")  # Tu dirección de correo electrónico real
password = input("Contraseña:")  # Tu contraseña de correo electrónico
servidor = input("Indica tu servidor SMTP:")
destinatario = input("Indica destinatario:")  # Dirección de correo electrónico del destinatario
asunto = input("Asunto de correo:")
cuerpo = input("Texto:")
num_correos = int(input("Cantidad de correos:"))

# Bucle para enviar múltiples correos electrónicos con asuntos secuenciales
for i in range(1, num_correos + 1):
    asunto = f'Correo {i}'  # Asunto secuencial
    codigo_respuesta = enviar_correo(destinatario, asunto, cuerpo,servidor,remitente,password)
    print(f"Correo electrónico {i} enviado a {destinatario} con código de respuesta: {codigo_respuesta}")

