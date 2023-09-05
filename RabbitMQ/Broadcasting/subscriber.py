"""
Broadcast
"""

import pika
import sys
import os


def main():
    # Create a connection, say CN
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    # Create a channel in CN, say CH
    channel = connection.channel()

    # Create the Exchange (will have no effect if Exchange is already existing)
    channel.exchange_declare(exchange="br_exchange", exchange_type="fanout")

    # Create the Temporary Queue and associate it with the channel CH exclusively
    temp_queue = channel.queue_declare(queue="", exclusive=True)

    queue_name = temp_queue.method.queue

    print(f"Subscriber queue_name is: {queue_name}")

    # Bind the Queue with the Exchange using the Queue name
    channel.queue_bind(exchange="br_exchange", queue=queue_name)

    print("[*] waiting for messages. To exit press Ctrl-C")

    def callback(ch, method, properties, body):
        # In this case body is raw format (binary)
        print("[x] received %r" % body)

    # Associate a callback function with the message queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    # Start consuming the messages
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
