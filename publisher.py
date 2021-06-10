import json
import secrets
import sys
sys.path.append("/opt/lampp/htdocs/Productor-Consumidor/")
from connections.connection import connect_rabbitmq

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    for i in range(10000):
        print("mensaje ...."+str(i))
        message = {}
        message['token'] = secrets.token_hex(16)
        message['descripcion'] = 'prueba'
        message['info'] = "Hi"
        message['secuencia'] = i

        conn = connect_rabbitmq()
        channel = conn.channel()
        channel.queue_declare(queue='microservicio')
        data = json.dumps(message)
        channel.basic_publish(exchange='', routing_key='microservicio', body=data)
        conn.close()


