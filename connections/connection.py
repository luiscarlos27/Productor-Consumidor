import json
import pika

def load_configuration():
   ## load configuration file
    data = ""
    with open('config/config.json') as f:
        data = json.load(f)

    return data

def connexion_rabbitmq():
    file = load_configuration()
    user = file['broker']['connection']['username']
    password = file['broker']['connection']['password']
    host = file['broker']['connection']['host']
    port = file['broker']['connection']['port']

    # Establecer conexión
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', pika.PlainCredentials(username=user,password=password)))
    channel = connection.channel()
    return channel

def connect_rabbitmq():
    file = load_configuration()
    user = str(file['broker']['connection']['username'])
    password = str(file['broker']['connection']['password'])
    host = file['broker']['connection']['host']
    port = file['broker']['connection']['port']
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, '/', pika.PlainCredentials(username=user,password=user)))
    return connection

def send_menssage(message):
    message_final = json.dumps(message)
    connection_send = connect_rabbitmq()
    channel_send = connection_send.channel()
    channel_send.queue_declare(queue='assign_route')
    channel_send.basic_publish(exchange='', routing_key='assign_route', body=message_final)
    connection_send.close()
