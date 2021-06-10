import sys, os
import json
sys.path.append("/opt/lampp/htdocs/Productor-Consumidor/")
from connections.connection import connexion_rabbitmq

def main():

    channel = connexion_rabbitmq()
    channel.queue_declare(queue='microservicio')
    channel.basic_consume(queue='microservicio', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    data = json.loads(body)
    print(data)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
