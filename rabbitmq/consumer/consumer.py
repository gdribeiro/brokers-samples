#!/usr/bin/env python
import pika
import time

time.sleep(20)

log = open('./log.txt', '+w')
log.write('Messages\n')



connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    log.write('Received: ' + str(body) + '\n')
    print(body)
    log.flush()


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

log.close()