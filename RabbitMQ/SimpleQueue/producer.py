"""
* Assignment: Centralized Alert System *
This program represents the mobile app, that creates
a Connection, declares queue if not exist already,
and sends a message to queue. Currently this program
only runs once and terminates. Currently the queue still
persists once created, and is not cleaned up.
"""

import pika

# Create a connection, say CN
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

# Create a channel in CN, say CH
channel = connection.channel()

# [Optional] Create an Exchange ans specify bindings
# (Skipping this step, as working with Default Exchange)

# If the queue does not exist already, create a queue and associate with the channel
# (does nothing if already existing)
channel.queue_declare(queue="hello")

# Publish the message
channel.basic_publish(exchange="", routing_key="hello", body="Hello World msg #3")
print("[x] Sent message")

# Close the connection
# Automatically closes the channel
connection.close()
