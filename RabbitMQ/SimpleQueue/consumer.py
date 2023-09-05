"""
Program which is essentially a consumer that waits for messages
on a queue, and then consumes them with callback when they appear.
Defines the queue if not existing already.
start_consuming() creates a blocking call loop running continually,
so needs a break out of.
* Assignment: Centralized Alert System *
This would be the centralized system that waits continuously for the
alert messages on it's queue, and then consumes the message and displays it
on it's output.
Currently the queue still persists once created, and is not cleaned up.
"""

import pika
import sys
import os


def main():
    # Create a connection, say CN
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    # Create a channel in CN, say CH
    channel = connection.channel()

    # If the queue does not exist already, create a queue and associate with the channel CH
    # (does nothing if already existing)
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        # In this case body is raw format (binary)
        print("[x] received %r" % body)

    # Associate a callback function with the message queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    # Start consuming the messages
    print("[*] waiting for the messages. To exit press Ctrl-C")
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
