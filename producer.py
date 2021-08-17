import pika,json

params = pika.URLParameters('amqps://eskzcdmk:FrWuKJdlTfEmBbHZGwc4XKfmihDZNrP9@codfish.rmq.cloudamqp.com/eskzcdmk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
   
    properties = pika.BasicProperties(method)
    #routing key is queue that we want to send the event 
    channel.basic_publish(exchange='',routing_key='admin',body=json.dumps(body),properties=properties)