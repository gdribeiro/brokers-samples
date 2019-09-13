#!/usr/bin/env python
import pika
import time

time.sleep(20)


connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))

channel = connection.channel()

channel.queue_declare(queue='hello')


log = open('log.txt','w+')
log.write('Messages\n')

i = 'hello'

while True:
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body= i)
    log.write( i + '\n')
    log.flush()
    print(i)


    time.sleep(5)

log.close()
connection.close()
