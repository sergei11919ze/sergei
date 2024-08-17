import pika
from base64 import b64encode
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.db import connection


import redis


def main(id):
      
    cursor = connection.cursor()
   
    r = redis.Redis(host='localhost', port=6379, db=0)
    q = '''SELECT new_function();'''
    l = r.llen('hesc')
    print(id)
    if l > 4000:
        return None
    else:
        for i in range(id):
            try:
                
                cursor.execute(q)
                result = cursor.fetchall()
            
                text = str(result[0][0])
                text = text.encode('ascii')
                text_b64 = b64encode(text)
                   
                list_hesch = r.rpush('hesc', text_b64)
            except:
                print('Ошибка запроса')
    cursor = connection.close()
    return None


connections = pika.BlockingConnection(pika.URLParameters('amqps://uebnofyc:hFhiv9SiD_6zOsuhlFfdp_tZGiwC2zcP@shrimp.rmq.cloudamqp.com/uebnofyc'))
channel = connections.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    main(1000)
    

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
